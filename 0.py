import requests
from bs4 import BeautifulSoup

quotes = "термопот"
stat = "krasnoyarsk"
url = f'https:/otes}/www.avito.ru/{stat}?q={qu'
popul = requests.get(url)
dod = BeautifulSoup(popul.text, 'html.parser' )
pmax = 2300
pmin = 1000
url = f'https://www.avito.ru/{stat}?pmax={pmax}&pmin={pmin}&q={quotes}'
soup = requests.get(url)
dods = BeautifulSoup(soup.text, 'html.parser' )

count = dods.find_all(class_= "page-title-count-1oJOc")
Name = dods.find_all(class_= "iva-item-titleStep-2bjuh")
cost = dods.select("span.price-text-1HrJ_.text-text-1PdBw.text-size-s-1PUdo")
links = dods.select("a.link-link-39EVK.link-design-default-2sPEv.title-root-395AQ.iva-item-title-1Rmmj.title-list-1IIB_.title-root_maxHeight-3obWc")

for pom in count: #число объявлений
    wow = int(pom.text)
site = []
count = 0 
for nam in Name:
    count += 1
    if count > wow:
        break
    site.append(nam.get_text())
price = []
count = 0
for cos in cost:
    count += 1
    if count > wow:
        break
    price.append(cos.get_text())
links = []
count = 0
for link in links:
    count += 1
    if count > wow:
        break
    links.append(link.get("href"))
print(len(Name), wow)
Name1 = []
i = 0
for nam in Name:
    i += 1
    
#set = (Name, cost, links)
#def unif():
#    Name, cost, links = 
    
#print(type(Name))
#for i in range(wow):
 #   print(f'{site[i]} // {price[i]} // avito.ru{links[i]}')
  #  print()
