import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


path = "data/2dsig.dat"  # Path of the 2d signal
with open(path, encoding="utf-8") as fp:  # Open and read the signal
    line = fp.readline()
# A comprehension:
# Convert the text into floating values for every value in the split line
data = np.array([float(i) for i in line.split(",")])
mat = data.reshape(358, -1).transpose()  # Reshape into matrix

f = plt.figure(figsize=(16, 10))  # Create a pyplot figure, size in inches
plt.imshow(mat, origin='lower')  # Show image from matrix
plt.show()  # Show figure

x = np.mean(mat, axis=0)  # Take mean over one dimension
# Create a linear space for the time, from 0 to the length of x:
t = np.linspace(0, mat.shape[1], len(x))

f = plt.figure(figsize=(16, 10))
plt.plot(t, x)
plt.show()

df = pd.DataFrame(x, index=t)  # Create a pandas DataFrame
df.columns = ["voltage"]  # Name the columns
df.index.name = "time"  # Name the index
df.head()  # See the first elements of the DataFrame
df.to_csv("./data/sig.csv")  # Write the DataFrame to a csv file
