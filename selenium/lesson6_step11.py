from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import os

#link = "http://suninjuly.github.io/wait1.html"
try:
    browser = webdriver.Chrome()
    # говорим WebDriver ждать все элементы в течение 5 секунд

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    cost = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//h5[text()='$100']")))
    browser.find_element_by_xpath('//button[text()="Book"]').click()


    #browser.find_element_by_xpath("//button[text()='I want to go on a magical journey!']").click()
    #browser.switch_to.window(browser.window_handles[1])

    x = int(browser.find_element_by_id("input_value").text)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))


    browser.find_element_by_id("answer").send_keys(calc(x))
    browser.find_element_by_xpath("//button[text()='Submit']").click()


    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

