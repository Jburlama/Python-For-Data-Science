from PIL import Image
import numpy as np


def ft_load(path: str):
    img = Image.open(path)

    img_array = np.array(img)
    print("The shape of image is:", img_array.shape)
    return img_array
