import imageio
from imgaug import augmenters as aug
from os import listdir
from os import rename

color = aug.Add((-40, 40), per_channel=0.5)
blur = aug.GaussianBlur(sigma=(0.0, 1.0))
contrast = aug.GammaContrast((0.7, 2))
perspective = aug.PerspectiveTransform(scale=(0.01, 0.15))

augmenter = aug.SomeOf((2, 4), [
      color, blur, contrast, perspective
], random_order=True)


for img in listdir("images/"):
	image = imageio.imread("images/" + img)
	image_aug = augmenter(image = image)
	imageio.imwrite("images/" + img, image_aug)
	rename("images/" + img, "images/" + img[:-5] + '_3.jpeg')