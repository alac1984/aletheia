import os
import httpx
from bs4 import BeautifulSoup as Soup

r = httpx.get(
    "http://pesquisa.doe.seplag.ce.gov.br/doepesquisa/sead.do?page=AjaxXML&cmd=1&action=AjaxData&dataAjax=2025"
)

xml_content = Soup(r.content, "lxml")

xml_dates = xml_content.find_all('atividade')

files = os.listdir("files/")

for date in xml_dates:
    date_list = date.get('id').split("/")
    converted = date_list[2] + date_list[1] + date_list[0]
    r = httpx.get(
        f"http://pesquisa.doe.seplag.ce.gov.br/doepesquisa/sead.do?page=ultimasDetalhe&cmd=10&action=Cadernos&data={converted}"
    )
    html_content = Soup(r.content, "lxml")
    links = html_content.find_all("a")
    for link in links:
        href = link.get("href")
        filename = href.split("/")[-1]
        if filename not in files:
            r = httpx.get(href, follow_redirects=True)
            if r.status_code == 200:
                with open("files/" + filename, "wb") as f:
                    f.write(r.content)
