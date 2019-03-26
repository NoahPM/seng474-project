import matplotlib.pyplot as plt
import os
from PIL import Image
import numpy as np
import json
from skimage.feature import hog
from skimage import data, exposure



def main():
	path = "C:\\Users\\noahp\\Documents\\reddit-memes-dataset\\memes"
	hogs = []
	fnames = []
	db = json.loads(open("dp_fixed.json", encoding='utf-8').read())
	print(json.dumps(db))
	for r, d, f in os.walk(path):
		for name in f:
			print(os.path.join(r, name))
			img = Image.open(os.path.join(r, name))
			fd= hog(img, multichannel=True, block_norm = "L2-Hys")
			hogs.append(fd)
			fnames.append(name)

			#visualization (remove later)
			# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)

			# ax1.axis('off')
			# ax1.imshow(img, cmap=plt.cm.gray)
			# ax1.set_title('Input image')

			# # Rescale histogram for better display
			# hogi_rescaled = exposure.rescale_intensity(hogi, in_range=(0, 10))

			# ax2.axis('off')
			# ax2.imshow(hogi_rescaled, cmap=plt.cm.gray)
			# ax2.set_title('Histogram of Oriented Gradients')
			# plt.show()
			# input()
			#end visualization








if __name__ == '__main__':
	main()
