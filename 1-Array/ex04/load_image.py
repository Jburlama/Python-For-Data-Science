from PIL import Image
import numpy as np


def ft_load(path: str):
    try:
        img = Image.open(path)

        img_arr = np.array(img)
        slice_arr = img_arr[:400, :400, :1]

        print("The shape of image is:", slice_arr.shape, end="")
        return slice_arr

    except (FileNotFoundError and AttributeError) as e:
        print(f"{e}")
