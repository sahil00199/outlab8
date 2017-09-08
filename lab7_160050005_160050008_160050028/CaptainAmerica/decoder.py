import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
import pylab

arr=np.load("message.npy")
c=np.amin(arr)
d=np.amax(arr)
output=np.multiply(np.subtract(arr,c),(255/(d-c)))
imgplot=plt.imshow(output)
pylab.savefig("processed_image.png")
plt.show()