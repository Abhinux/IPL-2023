from bs4 import BeautifulSoup
url="https://www.iplt20.com/auction/2023"
soup=BeautifulSoup(url)
print(soup.prettify())
