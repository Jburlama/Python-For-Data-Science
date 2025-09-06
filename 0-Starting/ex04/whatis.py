import sys

def atoi(s: str) -> int:
    try:
        number = int(s);
        return number
    except ValueError as e:
        return None


try:
    if (len(sys.argv) > 2):
        raise AssertionError("more than one argument is provided");
    if (len(sys.argv) == 1):
        print();
    else:
        number = atoi(sys.argv[1]);
        if (number == None):
            raise AssertionError("argument is not an integer");
        if (number % 2):
            print("I'm Odd.")
        else:
            print("I'm Even.")

except AssertionError as e:
    print(f"AssertionError: {e}");
