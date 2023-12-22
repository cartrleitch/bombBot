# from selenium import webdriver as wd
# from  selenium.webdriver.chrome.options import Options
# import time

# opt = wd.ChromeOptions()
# opt.headless = True
# driver = wd.Chrome(options=opt)
# driver.get("https://www.cnn.com/markets/fear-and-greed")

# time.sleep(1)


# S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
# driver.set_window_size(S('Width'),S('Height'))
# driver.find_element_by_tag_name('body').screenshot('screenshot.png')
# # driver.get_screenshot_as_file("screenshot.png")
# driver.quit()
# print("done")

# https://www.cnn.com/markets/fear-and-greed

# import webbrowser
# webbrowser.open("https://www.tradingview.com/chart/6QVeuDl7/?symbol=AMEX%3ASPY", new=1, autoraise=True)

# from selenium import webdriver as wd
# import time

# stock = input("Enter stock: ")

# driver = wd.Firefox()
# driver.maximize_window()
# time.sleep(1)

# driver.get(f"https://www.tradingview.com/chart/?symbol={stock}")
# time.sleep(1)
# driver.get_screenshot_as_file("screenshot.png")

# driver.quit()
# print("done")

import pyautogui as pg
pg.moveTo(1892, 12)            

