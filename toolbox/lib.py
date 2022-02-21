# toolbox/lib.py

import numpy as np
import re

def euclidean_distance(coor_a, coor_b):
    """
    coor_a and coor_b are two ndarray of shape (n,), where n is the number of dimension of the vectorial space
    It returns the euclidean distance between these 2 points
    """
    mse= (coor_a- coor_b)** 2
    return np.sqrt(mse.sum())

def extract_digits(str):
    pattern = "(?:0|[1-9]\d{0,2}(?:,?\d{3})*)(?:\.\d+)?"
    matches = re.findall(pattern,str)
    if len(matches) == 0:
        return False
    return matches[0]
