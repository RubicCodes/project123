import pandas as pd
import numpy as np
x = np.load('image.npz')['arr_0']
y = pd.read_csv("labels.csv")["labels"]

print(pd.Series(y).value_counts())


classes = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

nclasses = len(classes)

roi = gray[upper_left[1]:bottom_right[1],upper_left[0]:bottom_right[0]]









