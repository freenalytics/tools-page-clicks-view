from dataclasses import dataclass
import pandas as pd
import numpy as np


@dataclass
class PageData:
  path: str
  raw_screenshot_path: str
  clicks_screenshot_path: str


def get_page_click_normal_coordinates(csv_data: str, route_filter: str) -> np.array:
  df = pd.read_csv(csv_data)
  filtered_df = df.loc[df['element_clicked.url_route'] == route_filter]

  page_x = filtered_df['element_clicked.page_x'].to_numpy()
  page_width = filtered_df['element_clicked.page_width'].to_numpy()
  page_y = filtered_df['element_clicked.page_y'].to_numpy()
  page_height = filtered_df['element_clicked.page_height'].to_numpy()

  normal_x = page_x / page_width
  normal_y = page_y / page_height

  return np.array(list(zip(normal_x, normal_y)))
