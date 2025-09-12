def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Body Mass Index =  weight (kg) / height (m²)
    take 2 lists of integers or floats in input and returns a list
of BMI values."""

    try:
        if len(height) != len(weight):
            raise AssertionError("Lists must be the same size")

        return [w / (h*h) for w, h in zip(weight, height)]

    except TypeError:
        print("TypeError: Only accpet int or float")
        return []

    except AssertionError as e:
        print(f"AssertionError: {e}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Takes a list of bmi values and return true if the value is above
        the limit and false otherwise"""

    try:
        return [i > limit for i in bmi]

    except TypeError:
        print("TypeError: Only accpet int or float")
        return []
