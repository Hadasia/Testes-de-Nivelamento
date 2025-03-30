import requests
from bs4 import BeautifulSoup 
import wget
from zipfile import ZipFile


Site = requests.get('https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/')

#Acessando os arquivos do site 

link = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
link_dois = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf"

#Fazendo download dos arquivos

wget.download(link, "Anexo I.pdf")
wget.download(link_dois, "Anexo II.pdf")

# Compactando os dois Anexos

with ZipFile("Web Scraping Python.zip", "w") as zip:
    zip.write("Anexo I.pdf")
    zip.write("Anexo II.pdf")

