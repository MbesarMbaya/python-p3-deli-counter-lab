def line(katz_deli):
    """Shows everyone their current place in the line.

    Args:
        katz_deli: A list of strings containing the names of the people in line.

    Returns:
        None.
    """

    if not katz_deli:
        print("The line is currently empty.")
    else:
        line_str = "The line is currently:"
        for index, name in enumerate(katz_deli, start=1):
            line_str += f" {index}. {name}"
        print(line_str)


def take_a_number(katz_deli, name):
    if name not in katz_deli:
        katz_deli.append(name)
    position = len(katz_deli)
    print(f"Welcome, {name}! You are number {position} in line.")


def now_serving(katz_deli):
    """Removes the first person in line and prints their name.

    Args:
        katz_deli: A list of strings containing the names of the people in line.

    Returns:
        The name of the person who was just served.
    """

    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        next_person = katz_deli.pop(0)
        print(f"Now serving {next_person}.")
        return next_person


# Example usage:

katz_deli = []

line(katz_deli)
# Output: The line is currently empty.

take_a_number(katz_deli, "Alice")
# Output: Welcome, Alice! You are number 1 in line.

line(katz_deli)
# Output:
# The line is currently: 1. Alice

take_a_number(katz_deli, "Bob")
# Output: Welcome, Bob! You are number 2 in line.

line(katz_deli)
# Output:
# The line is currently: 1. Alice 2. Bob

next_person = now_serving(katz_deli)
# Output: Now serving Alice.
# Output: Alice

line(katz_deli)
# Output:
# The line is currently: 1. Bob

