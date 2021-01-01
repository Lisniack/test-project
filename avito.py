from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path='C:\\Users\\Ольга\\Downloads\\питон\\geckodriver.exe')
driver.get("https://www.avito.ru")
element = driver.find_element_by_id("search")
element.send_keys('модем роутер') #вписать в поисковик

elemen = driver.find_element_by_class_name("suggest_item")
elemen.click()

knop = driver.find_element_by_class_name("main-select-2pf7p.main-location-3j9by") #нажимать на выбор города
knop.click()

cities = driver.find_element_by_class_name("suggest-input-3p8yi") #строчка с городом
cities.send_keys('Барнаул')
time.sleep(5)
cities.click()

new = driver.find_element_by_class_name("suggest-suggest_content-3ZSEd")
new.click()

act = driver.find_element_by_class_name("button-button-2Fo5k.button-size-m-7jtw4.button-primary-1RhOG") #строчка найти
act.click()


driver.quit()
