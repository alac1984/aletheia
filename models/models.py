import re
from datetime import date
from pydantic import BaseModel, field_validator, model_validator

class DOECreate(BaseModel):
    filename: str
    data_publicacao: date | None = None
    caderno: int | None = None

    # 1) Valida o campo filename individualmente
    @field_validator("filename")
    def valida_formato_filename(cls, valor):
        """
        Verifica se o nome do arquivo segue o formato "doYYYYMMDDpNN.pdf".
        Exemplo: "do20250212p02.pdf".
        """
        padrao = r"^do(\d{4})(\d{2})(\d{2})p(\d{2})\.pdf$"
        if not re.match(padrao, valor):
            raise ValueError(
                "Nome do arquivo inválido. Formato esperado: 'doYYYYMMDDpNN.pdf'"
            )
        return valor

    # 2) Depois da validação de todos os campos, extrai data_publicacao e caderno
    @model_validator(mode="after")
    def extrai_campos_do_filename(self):
        """
        Extrai data e caderno do filename e preenche os campos do modelo.
        Rode 'depois' das validações de campo.
        """
        padrao = r"^do(\d{4})(\d{2})(\d{2})p(\d{2})\.pdf$"
        match = re.match(padrao, self.filename)
        if match:
            ano, mes, dia, caderno_str = match.groups()
            self.data_publicacao = date(int(ano), int(mes), int(dia))
            self.caderno = int(caderno_str)
        return self
