# import the libs
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

# create the initial window
driver = webdriver.Chrome()

# go to the home page
driver.get('https://toeic-center.herokuapp.com/')

# storing the current window handle to get back to dashboard
main_page = driver.current_window_handle

# click on the sign in tab
driver.find_element_by_xpath('/html[1]/body[1]/div[2]/div[1]/div[1]/button[1]/span[1]/span[1]').click()
sleep(1)

#  handle windows
pages=driver.window_handles
for handle in pages:
    if handle not in main_page:
        #change the control to singin page
        driver.switch_to.window(handle)
        # enter the email
        driver.find_element_by_id("identifierId").send_keys("toeic@novahub.vn")
        driver.find_element_by_id("identifierId").send_keys(Keys.ENTER)
        sleep(4)
        # enter the password
        driver.find_elements_by_class_name("zHQkBf")[0].send_keys("toeic123")
        driver.find_elements_by_class_name("zHQkBf")[0].send_keys(Keys.ENTER)

# change control to main page
driver.switch_to.window(main_page)
sleep(10)


