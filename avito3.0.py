from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='C:\\Users\\Lenovo\\Downloads\\драйвера питон\\chromedriver.exe')
driver.get('https://www.avito.ru')
element = driver.find_element_by_id("search")               
element.send_keys("мейзу")

elemen = driver.find_element_by_class_name("suggest_item") #нажать на окно поиска
elemen.click()

time.sleep(3)
knop = driver.find_element_by_class_name("main-select-2pf7p.main-location-3j9by") #нажимать на выбор города
knop.click()

cities = driver.find_element_by_class_name("suggest-input-3p8yi") #строчка с городом
cities.send_keys("Красноярск")
time.sleep(3)
cities.click()

new = driver.find_element_by_class_name("suggest-suggest_content-3ZSEd") #выбор города
new.click()

act = driver.find_element_by_class_name("button-button-2Fo5k.button-size-m-7jtw4.button-primary-1RhOG") #строчка найти
act.click()

#изменение цены
price = driver.find_element_by_css_selector("body > div.js-single-page.single-page > div.index-center-2ZEUx.index-center_withTitle-3Ne4c > div.index-inner-LCNXs.index-innerCatalog-mLDlZ > div.index-side-VRBfr.index-sideCatalog-1gq0P > div > div:nth-child(2) > div:nth-child(1) > form > div:nth-child(4) > div > div:nth-child(2) > div > div > div > div > div > div > label.input-layout-input-layout-eKhsI.input-layout-size-s-UjNk6.input-layout-text-align-left-IDAPR.width-width-12-2VZLz.input-layout-stick-after-2gOSb.formatted-input-root-1EvH0")
time.sleep(5)
price.send_keys("3000")
price.click()


pric = driver.find_element_by_css_selector("body > div.js-single-page.single-page > div.index-center-2ZEUx.index-center_withTitle-3Ne4c > div.index-inner-LCNXs.index-innerCatalog-mLDlZ > div.index-side-VRBfr.index-sideCatalog-1gq0P > div > div:nth-child(2) > div:nth-child(1) > form > div:nth-child(4) > div > div:nth-child(2) > div > div > div > div > div > div > label.input-layout-input-layout-eKhsI.input-layout-size-s-UjNk6.input-layout-text-align-left-IDAPR.width-width-12-2VZLz.input-layout-stick-before-D-lLx.formatted-input-root-1EvH0")
time.sleep(5)
pric.send_keys("15000")
pric.click()

#выбор состояние товара
state = driver.find_element_by_class_name("checkbox-filter-item-jVGLX")
state.click()

#нажатие на кнопку "показать объявление"
knop_2 = driver.find_element_by_class_name("button-button-2Fo5k.button-size-s-3-rn6.button-primary-1RhOG.width-width-12-2VZLz")
time.sleep(2)
knop_2.click()


POMOGITE = driver.find_elements_by_class_name("page-title-count-1oJOc")
names = driver.find_elements_by_class_name("title-root-395AQ.iva-item-title-1Rmmj.title-list-1IIB_.title-root_maxHeight-3obWc.text-text-1PdBw.text-size-s-1PUdo.text-bold-3R9dt")
citu = driver.find_elements_by_class_name("price-price-32bra")
#elems = driver.find_elements_by_class_name("iva-item-body-NPl6W")
links = driver.find_elements_by_class_name("link-link-39EVK.link-design-default-2sPEv.title-root-395AQ.iva-item-title-1Rmmj.title-list-1IIB_.title-root_maxHeight-3obWc")

for pom in POMOGITE: #количество товара
    wow = int(pom.text)
site = []
count = 0
for link in links: #показать все ссылки
    count += 1
    if count > wow:
        break
    site.append(link.get_attribute("href"))
    
name = []
count = 0
for nam in names: #показать название товара
    count += 1
    if count > wow:
        break
    name.append(nam.text)

cost = []
count = 0
for cit in citu: #показать название товара
    count += 1
    if count > wow:
        break
    cost.append(cit.text)
    
for i in range(wow): # решение при помощи цикла с range
    print(f'{name[i]} - {cost[i]}: {site[i]}')
    print()

#result = list(zip(name, site)) решение при помоши соединения 2 списков в 1 (методом zip)
#for i in result:
#    print(i)

  
driver.quit()
