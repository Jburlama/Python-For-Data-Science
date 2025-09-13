from load_image import ft_load
from PIL import Image
import numpy as np


def transpose(img_arr: np.ndarray):
    height, width = img_arr.shape
    transpose_arr = np.zeros((width, height), dtype=img_arr.dtype)

    for y in range(height):
        for x in range(width):
            transpose_arr[x][y] = img_arr[y][x]

    return transpose_arr


def main():
    path = "../imgs/animal.jpeg"

    slice_arr = ft_load(path)
    squeeze_arr = slice_arr.squeeze()
    print(" or:", squeeze_arr.shape)
    print(slice_arr)

    transpose_arr = transpose(slice_arr.squeeze())
    print("New shape after transpose:", squeeze_arr.shape)
    print(transpose_arr)

    img = Image.fromarray(transpose_arr)
    img.show()


if __name__ == "__main__":
    main()
