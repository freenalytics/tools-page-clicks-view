import os
from utils.web import screenshot_page
from utils.data import get_page_click_normal_coordinates
from utils.image import overlay_page_clicks


URL = 'http://127.0.0.1:5500/article'
DATA_AS_CSV = 'FD-107hpuco5lbd37lfa-data.csv'
ROUTE_FILTER = '/article/'

OUT_DIR = os.path.abspath(os.path.join(os.getcwd(), 'out'))
RAW_SCREENSHOT_PATH = os.path.join(OUT_DIR, 'raw_screenshot.png')
CLICKS_SCREENSHOT_PATH = os.path.join(OUT_DIR, 'clicks_screenshot.png')


def main():
  if not os.path.exists(OUT_DIR):
    os.mkdir(OUT_DIR)

  # screenshot_page(URL, RAW_SCREENSHOT_PATH, width=1920)
  normal_page_coordinates = get_page_click_normal_coordinates(DATA_AS_CSV, ROUTE_FILTER)
  overlay_page_clicks(RAW_SCREENSHOT_PATH, normal_page_coordinates, CLICKS_SCREENSHOT_PATH)


if __name__ == '__main__':
  main()
