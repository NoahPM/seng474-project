import matplotlib.pyplot as plt
import os
from PIL import Image

from skimage.feature import hog
from skimage import data, exposure
path = "C:\\Users\\noahp\\Documents\\reddit-memes-dataset\\memes"


def main():

	for r, d, f in os.walk(path):
		for name in f:
			print(os.path.join(r, name))
			img = Image.open(os.path.join(r, name))
			fd, hogi= hog(img, multichannel=True, cells_per_block=(1, 1),  visualize = True, block_norm = "L2-Hys")
			fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)

			ax1.axis('off')
			ax1.imshow(img, cmap=plt.cm.gray)
			ax1.set_title('Input image')

			# Rescale histogram for better display
			hogi_rescaled = exposure.rescale_intensity(hogi, in_range=(0, 10))

			ax2.axis('off')
			ax2.imshow(hogi_rescaled, cmap=plt.cm.gray)
			ax2.set_title('Histogram of Oriented Gradients')
			plt.show()
			input()



if __name__ == '__main__':
	main()
