import sys


def main():
    """akes a string as an argument and encodes it into Morse Code."""
    morse = {
        " ": "/ ",
        "A": ".- ",
        "B": "-.. ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-- ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
    }

    try:
        if (len(sys.argv) != 2):
            raise AssertionError("the arguments are bad")
        text = sys.argv[1]
        not_text = [c for c in text if not c.isalnum()]
        not_text = [c for c in not_text if not c.isspace()]
        if not_text != []:
            raise AssertionError("the arguments are bad")

        for c in text:
            print(morse[c.upper()], end="")
        print()

    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit()


if __name__ == "__main__":
    main()
