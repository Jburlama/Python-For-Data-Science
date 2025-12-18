import sys


def building(text: str, cr: bool) -> None:
    """
        takes a single string argument
        and displays the sums of its
        upper-case characters,
        lower-case characters,
        punctuation characters,
        digits,
        and spaces

        If cr is true, Carrage Return will count has space,
        otherwise not
        """

    upper = 0
    lower = 0
    punctuation = 0
    digits = 0
    spaces = 0
    if (cr):
        spaces = 1

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            digits += 1
        elif char.isspace():
            spaces += 1
        elif is_punctuation(char):
            punctuation += 1

    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")

    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def is_punctuation(c: str) -> bool:
    """Takes a char, string of lenght 1,
    and returns True if c is punctuation and False otherwise"""

    punctuations = ".,!?><;:/'\"[]{}()-"
    if c in punctuations:
        return True
    return False


def main():
    """
        takes a single string argument and displays the sums of its

        upper-case characters,
        lower-case characters,
        punctuation characters,
        digits,
        spaces and
        If cr is true, Carrage Return will count has space,
        otherwise not

        - If none or nothing is provided,
        the user is prompted to provide a string

        - If more than one argument is provided to the program,
        print an AssertionError
        """

    try:
        if (len(sys.argv) > 2):
            raise AssertionError("To Many Arguments")
        elif (len(sys.argv) < 2):
            text = input("What is the text to count?\n")
            building(text, cr=True)
        else:
            building(sys.argv[1], cr=False)

    except AssertionError as e:
        print(f"AssertionError: {e}")
    except EOFError:
        building("", cr=False)


if __name__ == "__main__":
    main()
