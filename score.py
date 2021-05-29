
from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://in.global.nba.com/scores/")
driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div[2]/div/div/button").click()
scores=[]
for i in driver.find_elements_by_class_name("final-game-table-wrapper"):
    scores.append(i.text)
driver.close()
for i in scores:
    scores[scores.index(i)]=i.split('\n')
for i in scores:
    if(i[3].split(' ')[4]>i[6].split(' ')[4]):
        print('----------')
        print(i[1],'VS',i[4].lower())
    else:
        print('----------')
        print(i[1].lower(),'VS',i[4])
    print(i[3].split(' ')[4],'   ',i[6].split(' ')[4])

