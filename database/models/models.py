from typing import Optional
from datetime import date
from sqlmodel import SQLModel, Field, Relationship

class Regional(SQLModel, table=True):
    """
        Representa a regional (CREDE ou SEFOR)
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    cidade: str = Field(foreign_key="cidade.id")


class Extrato(SQLModel, table=True):
    """
        Representa um Extrato aos Termos dos Contratos Temporários de Professores
        Temporários, que aparece sempre ligado a um processo e dividido em lotes
        no DOE. Dentro deles há várias contratações, divididas por escolas.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    regional_id: int = Field(foreign_key="regional.id")
    processo: str
    data_publicacao: date


class Contrato(SQLModel, table=True):
    """
        Representa o contrato de um Professor Temporário do Estado do Ceará, tal
        como exposto no DOE em algum Extract.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    extrato_id: int = Field(foreign_key="extrato.id")
    escola_id: int = Field(foreign_key="escola.id")
    turno: str
    matricula: str
    professor: int = Field(foreign_key="professor.id")
    cargo: int = Field(foreign_key="cargo.id")
    substituido: int = Field(foreign_key="professor.id")
    justificativa: str
    inicio: date
    fim: date
    motivo: int = Field(foreign_key="motivo.id")
    criterio: int = Field(foreign_key="criterio.id")
    ch_semanal: int
    ch_mensal: int
    hora_aula: float
    valor_mensal: float


class Motivo(SQLModel, table=True):
    """
        Representa os distintos motivos encontrados no sistema.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    descricao: str


class Criterio(SQLModel, table=True):
    """
        Representa os critóerios distintos encontrados.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    descricao: str


class Professor(SQLModel, table=True):
    """
        Representa um professor encontrado pelo sistema.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str


class Cargo(SQLModel, table=True):
    """
        Representa os distintos cargos encontrados pelo sistema.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str


class Escola(SQLModel, table=True):
    """
        Representa uma escola no sistema.
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    inep: str
    nome: str
    cidade_id: Optional[str] = Field(foreign_key="cidade.id")


class Cidade(SQLModel, table=True):
    """
        Uma lista das cidades do Ceará.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
