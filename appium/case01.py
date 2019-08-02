import time
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

server = 'http://localhost:4723/wd/hub'

desired_caps = {
    "platformName": "Android",
    "deviceName": "MIX_2S",
    "appPackage": "com.android36kr.app",
    "appActivity": ".ui.MainActivity"
}

driver = webdriver.Remote(server, desired_caps)
wait = WebDriverWait(driver,30)
kuaixun = wait.until(EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.TextView[3]')))
kuaixun.click()

FLICK_START_X = 300
FLICK_START_Y = 300
FLICK_DISTANCE = 700

while True:
    driver.swipe(FLICK_START_X, FLICK_START_Y + FLICK_DISTANCE, FLICK_START_X, FLICK_START_Y)
    time.sleep(2)