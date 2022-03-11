import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

cssSelectorBtPlay = "#movie_player > div.ytp-cued-thumbnail-overlay > button"

WIN_SIZE = 100

url = "https://youtu.be/D7sc9g25oV8"

url2 = "https://youtu.be/EH2Lbr9T7UI"

driver1 = webdriver.Chrome()
driver1.set_window_size(WIN_SIZE, WIN_SIZE)
driver1.set_window_position(0, 0)
driver1.get(url)
elem1 = driver1.find_element_by_css_selector(cssSelectorBtPlay)
elem1.click()
print (driver1.current_window_handle)

time.sleep(1)

driver2 = webdriver.Chrome()
driver2.set_window_size(100, 100)
driver2.set_window_position(driver1.get_window_rect()['width'], 0)
driver2.get(url2)
elem2 = driver2.find_element_by_css_selector(cssSelectorBtPlay)
elem2.click()
print (driver2.current_window_handle)

time.sleep(1)

driver3 = webdriver.Chrome()
driver3.set_window_size(100, 100)
driver3.set_window_position(0, driver1.get_window_rect()['height'])
driver3.get(url2)
elem3 = driver3.find_element_by_css_selector(cssSelectorBtPlay)
elem3.click()

time.sleep(1)

driver4 = webdriver.Chrome()
driver4.set_window_size(100, 100)
driver4.set_window_position(driver1.get_window_rect()['width'], driver1.get_window_rect()['height'])
driver4.get(url2)
elem4 = driver4.find_element_by_css_selector(cssSelectorBtPlay)
elem4.click()

count = 0;
while True:
    count = (count + 1) % 2;
    if count == 0:
        driver2.get(url2)
    else:
        driver1.get(url2)

    time.sleep(5);
