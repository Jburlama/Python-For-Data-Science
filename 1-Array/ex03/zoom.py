from load_image import ft_load
from PIL import Image


def main():
    try:
        path = "../imgs/animal.jpeg"

        img_arr = ft_load(path)
        print(img_arr)

        slice_arr = img_arr[:400, :400, :1]
        print("The shape after slicing is:", slice_arr.shape, end="")

        squeeze_arr = slice_arr.squeeze()
        print(" or", squeeze_arr.shape)

        print(slice_arr)

        img = Image.fromarray(squeeze_arr)
        img.show()

    except (FileNotFoundError and AttributeError) as e:
        print(f"{e}")


if __name__ == "__main__":
    main()
