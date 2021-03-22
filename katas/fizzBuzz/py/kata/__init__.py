# Example function
def template(arg):
    result = f"Doing something with {arg}"
    return result


def print_fizz_buzz(arg):
    result = ""
    if not arg % 3:
        result += "Fizz"
    if not arg % 5:
        result += "Buzz"

    if not result:
        result = str(arg)

    return result


for num in range(1, 101):
    print(print_fizz_buzz(num))


# Implement functions here
