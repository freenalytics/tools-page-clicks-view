import os
from utils.web import screenshot_page
from utils.data import get_page_click_normal_coordinates, PageData
from utils.image import overlay_page_clicks


URL = 'http://127.0.0.1:5500'
DATA_AS_CSV = 'FD-107hpuco5lbd37lfa-data.csv'
OUT_DIR = os.path.abspath(os.path.join(os.getcwd(), 'out'))


def main():
  if not os.path.exists(OUT_DIR):
    os.mkdir(OUT_DIR)

  pages = [
    PageData('/article/', os.path.join(OUT_DIR, 'article_raw.png'), os.path.join(OUT_DIR, 'article_clicks.png')),
    PageData('/', os.path.join(OUT_DIR, 'home_raw.png'), os.path.join(OUT_DIR, 'home_clicks.png')),
    PageData('/about/', os.path.join(OUT_DIR, 'about_raw.png'), os.path.join(OUT_DIR, 'about_clicks.png'))
  ]

  for page in pages:
    print(f'Processing {page.path}...')

    screenshot_page(f'{URL}{page.path}', page.raw_screenshot_path, width=1920)
    normal_page_coordinates = get_page_click_normal_coordinates(DATA_AS_CSV, page.path)
    overlay_page_clicks(page.raw_screenshot_path, normal_page_coordinates, page.clicks_screenshot_path)

    print(f'Done with {page.path}.')

  print('Finished.')


if __name__ == '__main__':
  main()
