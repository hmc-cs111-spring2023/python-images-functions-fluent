from PIL import Image

################################################################################
# Flipping
################################################################################


def flipHorizontal(image):
    '''Flip an image horizontally'''
    width, height = image.size
    result = Image.new('RGB', (width, height))

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            result.putpixel((width - x - 1, y), pixel)

    return result


def flipVertical(image):
    '''Flip an image vertically'''
    width, height = image.size
    result = Image.new('RGB', (width, height))

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            result.putpixel((x, height - y - 1), pixel)

    return result

################################################################################
# Rotating
################################################################################


def rotateLeft(image):
    '''Rotate an image 90 degrees counter-clockwise'''
    width, height = image.size
    result = Image.new('RGB', (height, width))

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            result.putpixel((y, width - x - 1), pixel)

    return result


def rotateRight(image):
    '''Rotate an image 90 degrees clockwise'''
    width, height = image.size
    result = Image.new('RGB', (height, width))

    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            result.putpixel((height - y - 1, x), pixel)

    return result

################################################################################
# Grayscale
################################################################################


def grayscale(image):
    '''Convert an image to grayscale'''
    width, height = image.size
    result = Image.new('RGB', (width, height))

    for x in range(width):
        for y in range(height):
            (r, g, b) = image.getpixel((x, y))
            gray = int((r + g + b) / 3)
            result.putpixel((x, y), (gray, gray, gray))

    return result

################################################################################
# Loading and saving
################################################################################


def load_image(path):
    '''Load an image from file'''
    return Image.open(path)


def save_image(image, path):
    '''Save an image to file'''
    image.save(path)
