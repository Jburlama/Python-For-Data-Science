from ft_filter import ft_filter
import sys


def main():
    """a program that accepts two arguments: a string (S) and an integer (N).
The program should output a list of words from S that have a length greater
than N."""
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        S = sys.argv[1]
        N = sys.argv[2]
        if (N.isdecimal() is False):
            raise AssertionError("the arguments are bad")

        words = S.split()
        lenght = int(N)
        notwords = [w for w in words if not w.isalnum() or not w.isprintable()]
        if (notwords != []):
            raise AssertionError("the arguments are bad")

        filter_word = ft_filter(lambda word: len(word) > lenght, words)
        filter_words_list = [w for w in filter_word]
        print(filter_words_list)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
