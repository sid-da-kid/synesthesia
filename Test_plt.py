import cv2
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

x = np.random.random(200)
y = np.random.random(200)
classes = np.random.randint(0, 3, 200)

# Presets:
#plt.scatter(x, y, c=classes, cmap= "gray")
#plt.scatter(x, y, c=classes, cmap= "Set1")
#plt.scatter(x, y, c=classes, cmap= "Spectral")

# Custom:
custom_cmap = matplotlib.colors.ListedColormap(["red", "purple", "green"])
plt.scatter(x, y, c=classes, cmap=custom_cmap)

plt.show()

