import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


DEFAULT_CIRCLE_RADIUS = 10
DEFAULT_COLOR = 'red'
DEFAULT_ALPHA = 0.5


def overlay_page_clicks(raw_screenshot_path: str, normal_coordinates: np.array, output_path: str, **kwargs):
  radius = kwargs.get('radius') or DEFAULT_CIRCLE_RADIUS
  color = kwargs.get('color') or DEFAULT_COLOR
  alpha = kwargs.get('alpha') or DEFAULT_ALPHA

  img = plt.imread(raw_screenshot_path)
  img_width = img.shape[1]
  img_height = img.shape[0]
  px = 1 / plt.rcParams['figure.dpi']

  fig, ax = plt.subplots(figsize=(img_width * px, img_height * px))
  ax.set_aspect('equal')

  for page_x, page_y in normal_coordinates:
    x = page_x * img_width
    y = page_y * img_height

    circle = Circle((x, y), radius, facecolor=color, alpha=alpha)
    ax.add_patch(circle)

  ax.imshow(img)
  plt.axis('off')
  plt.savefig(output_path, bbox_inches='tight', pad_inches=0)
