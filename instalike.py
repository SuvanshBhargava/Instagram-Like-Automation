
import time
from selenium import webdriver
user= input("Enter Username:")
pas= input('Enter Password:')
instaID= input('Enter InstaID:')
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.implicitly_wait(15)
driver.get('https://www.instagram.com/')
time.sleep(5)

driver.find_element_by_name("username").send_keys(user)
driver.find_element_by_name("password").send_keys(pas)

driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[3]/button').click()
time.sleep(5)
driver.find_element_by_class_name("sqdOP.yWX7d.y3zKF").click()
time.sleep(2)
driver.find_element_by_class_name("aOOlW.HoLwm").click()
time.sleep(2)
driver.find_element_by_class_name("XTCLo.x3qfX").send_keys(instaID)
time.sleep(2)
driver.find_element_by_partial_link_text(instaID).click()
time.sleep(2)
element=driver.find_element_by_class_name("g47SY").text
driver.find_element_by_class_name("v1Nh3.kIKUG._bz0w").click()
time.sleep(2)

driver.find_element_by_class_name('fr66n').click()


i=1
while i<int(element.replace(',','')):

    driver.find_element_by_class_name("_65Bje.coreSpriteRightPaginationArrow").click()
    time.sleep(2)
    
    driver.find_element_by_class_name('fr66n').click()



