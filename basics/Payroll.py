from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
class Login():
    def access(self):
        driver=webdriver.Chrome()
        driver.get("https://pay.wisami.com/")
        sleep(2)
        #input username and password
        inputs = driver.find_elements(By.TAG_NAME, "input")
        email= inputs[0]
        password = inputs[1]
        email.send_keys("frank@wisami.com")
        password.send_keys("12345678")
        driver.find_elements_by_tag_name("button")[1].click()
        sleep(10)



a=Login()
a.access()


