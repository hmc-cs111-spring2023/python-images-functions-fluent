from image import *

pic = load_image('../pictures/bird.png')

result = rotateLeft(grayscale(flipHorizontal(pic)))

save_image(result, "output.png")
