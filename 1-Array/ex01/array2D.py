import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    try:
        if type(family).__name__ != "list":
            raise AssertionError("family parameter must be a list")
        if type(start).__name__ != "int":
            raise AssertionError("start parameter must be a int")
        if type(end).__name__ != "int":
            raise AssertionError("end parameter must be a int")

        arr = np.array(family)
        print("My shape is :", arr.shape)
        new_arr = arr[start:end]
        print("My new shape is :", new_arr.shape)

        return family[start:end]

    except AssertionError as e:
        print(f"AssertionError: {e}")
        if type(family).__name__ != "list":
            return []
        return family
