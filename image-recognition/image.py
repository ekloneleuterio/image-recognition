#Libraries import for Image Recognition

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imshow
from skimage.color import rgb2gray
from skimage.feature import match_template, peak_local_max
from skimage import transform