from selenium import webdriver
class findelement():
    def byName(self):
        driver=webdriver.Chrome()
        main_page = driver.current_window_handle
        url="https://toeic-center.herokuapp.com/"
        driver.get(url)
        login=driver.find_element_by_xpath("//button[contains(@class,'')]").click()

        for handle in driver.window_handles:
            if handle != main_page:
                login_page = handle

                # change the control to signin page
        driver.switch_to.window(login_page)
        novahub=driver.find_element_by_xpath("//body[@id='yDmH0d']/div[@class='H2SoFe LZgQXe TFhTPc']/div[@id='initialView']/div[@class='xkfVF']/div[@id='view_container']/div[@class='zWl5kd']/div[@class='DRS7Fe bxPAYd k6Zj8d']/div[@class='pwWryf bxPAYd']/div[@class='Wxwduf Us7fWe JhUD8d']/div[@class='WEQkZc']/div[@class='bCAAsb']/form/span/section[@class='TgkVnd']/div[@class='dMArKd bxPAYd k6Zj8d']/span/div[@class='zeRELc']/div[@class='bUk9Ve']/ul[@class='FPFGmf']/li[6]/div[1]/div[1]/div[1]").click()
        driver.switch_to.window(main_page)
        whsOnd
        zHQkBf
        whsOnd
        zHQkBf

class="RveJvd snByac"


ff=findelement()
ff.byName()
