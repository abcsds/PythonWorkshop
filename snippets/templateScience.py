import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


path = "data/sig.csv"
data = pd.read_csv(path, index_col=0)

data.plot()
data.describe()

x = data.to_numpy
