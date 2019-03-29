import matplotlib.pyplot as plt
import os
from PIL import Image
import numpy as np
import json
from skimage.feature import hog
from skimage import data, exposure
import nltk
import re

#trains based on features X and scores Y
def train(X, Y):
	clf = SVR(gamma='scale', C=1.0, epsilon=0.2)
	clf.fit(X, y)
	return clf

def tag(s):
	s = re.sub('[^A-Za-z]', ' ', s)
	s = s.lower()
	out = {}
	tags = ["ADJ","ADP","ADV","CONJ","DET","NOUN","NUM","PRT","PRON","VERB","X"]
	for i in tags:
		out[i] = 0
	for i in nltk.pos_tag(nltk.word_tokenize(s), tagset = 'universal'):
		out[i[1]] += 1
	return out



def main():
	path = "C:\\Users\\noahp\\Documents\\reddit-memes-dataset\\memes\\"
	X = []
	scores = []
	db = json.loads(open("db.json", encoding='utf-8').read())
	#print(json.dumps(db))
	print(db['_default']['1']['title'])
	for index in db['_default']:
		na_img = Image.open('na.jpg')
		fname = db['_default'][index]['id']
		try:
			img = Image.open(path + fname + '.jpg')
		except:
			try:
				img = Image.open(path + fname + '.png')
			except:
				print("missing file:" + fname)
				continue
		if img == na_img:
			continue
		size = 32, 32
		try:
			fd= hog(img.resize(size), multichannel=True, block_norm = "L2-Hys")
		except:
			fd= hog(img.resize(size), block_norm = "L2-Hys")

		title = db['_default'][index]['title']
		for key, value in tag(title).items():
			np.append(fd, value)
		#print(fd.shape)
		X.append(fd)
		scores.append(db['_default'][index]['ups'])
	print(np.asarray(X).shape)
	print(np.asarray(scores).shape)



	# for r, d, f in os.walk(path):
	# 	for name in f:
	# 		print(os.path.join(r, name))
	# 		img = Image.open(os.path.join(r, name))
	# 		fd= hog(img, multichannel=True, block_norm = "L2-Hys")
	# 		print(fd.shape)
	# 		X.append(fd)
			#fnames.append(name)


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
