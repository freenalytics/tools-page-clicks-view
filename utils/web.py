from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.headless = True


def screenshot_page(url: str, screenshot_destination: str, **kwargs):
  force_width = kwargs.get('width')
  force_height = kwargs.get('height')

  driver = webdriver.Chrome(options=options)
  driver.get(url)

  width, height = get_page_dimensions(driver)
  driver.set_window_size(force_width or width, force_height or height)
  
  driver.find_element(By.TAG_NAME, 'body').screenshot(screenshot_destination)
  driver.quit()


def get_page_dimensions(driver: webdriver.Chrome) -> 'tuple[int, int]':
  width = driver.execute_script('return document.documentElement.scrollWidth')
  height = driver.execute_script('return document.documentElement.scrollHeight')

  return int(width), int(height)
