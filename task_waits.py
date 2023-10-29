from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")
button = browser.find_element(By.CSS_SELECTOR, "#book")


WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100")
)

button.click()

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


y = calc(x)

input = browser.find_element(By.CSS_SELECTOR, "#answer")
input.send_keys(y)

button = browser.find_element(By.CSS_SELECTOR, "#solve")
button.click()

time.sleep(10)


