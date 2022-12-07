import os
from utils.web import screenshot_page


URL = 'http://127.0.0.1:5500/article'
OUT_DIR = os.path.abspath(os.path.join(os.getcwd(), 'out'))
RAW_SCREENSHOT_PATH = os.path.join(OUT_DIR, 'raw_screenshot.png')


def main():
  if not os.path.exists(OUT_DIR):
    os.mkdir(OUT_DIR)

  screenshot_page(URL, RAW_SCREENSHOT_PATH, width=1920)


if __name__ == '__main__':
  main()
