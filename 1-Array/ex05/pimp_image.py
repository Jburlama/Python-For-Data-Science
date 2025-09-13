from PIL import Image


def ft_invert(array):
    """Inverts the color of the image received."""
    result = array.copy()

    result = 255 - result

    img = Image.fromarray(result)
    img.show()
    return result


def ft_red(array):
    """Red filter for the image received"""
    result = array.copy()

    result[:, :, 1] = 0
    result[:, :, 2] = 0

    img = Image.fromarray(result)
    img.show()

    return result


def ft_green(array):
    """Green filter for the image received"""
    result = array.copy()

    result[:, :, 0] = 0
    result[:, :, 2] = 0

    img = Image.fromarray(result)
    img.show()

    return result


def ft_blue(array):
    """Blue filter for the image received"""
    result = array.copy()

    result[:, :, 0] = 0
    result[:, :, 1] = 0

    img = Image.fromarray(result)
    img.show()

    return result


def ft_grey(array):
    """Grey filter for the image received"""
    result = array.copy()

    result = result[:, :, 1]

    img = Image.fromarray(result)
    img.show()

    return result
