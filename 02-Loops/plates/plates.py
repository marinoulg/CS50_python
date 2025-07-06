# In Massachusetts, home to Harvard University, it’s possible to request a
# vanity license plate for your car, with your choice of letters and numbers
# instead of random ones. Among the requirements, though, are:
    # - “All vanity plates must start with at least two letters.”
    # - “… vanity plates may contain a maximum of 6 characters (letters or
        # numbers) and a minimum of 2 characters.”
    # - “Numbers cannot be used in the middle of a plate; they must come at the
        # end. For example, AAA222 would be an acceptable … vanity plate; AAA22A
        # would not be acceptable. The first number used cannot be a ‘0’.”
    # - “No periods, spaces, or punctuation marks are allowed.”

# In plates.py, implement a program that prompts the user for a vanity plate
# and then output Valid if meets all of the requirements or Invalid if it does
# not. Assume that any letters in the user’s input will be uppercase. Structure
# your program per the below, wherein is_valid returns True if s meets all
# requirements and False if it does not. Assume that s will be a str. You’re
# welcome to implement additional functions for is_valid to call (e.g., one
# function per requirement).

from string import ascii_lowercase, punctuation

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s = s.lower()
    first_two = s[:2]
    for letter in first_two:
        if letter not in ascii_lowercase:
            # print("error 0")
            return False

    if len(s) > 6:
        # print("error 1")
        return False

    count_ascii = 0
    for char in s:
        if char in ascii_lowercase:
            count_ascii += 1
    if count_ascii < 2:
        # print("error 2")
        return False

    for idx in range(len(s) - 1):
        if s[idx] in ascii_lowercase:
            if s[idx + 1] in numbers:
                if s[idx + 1] == "0":
                    # print("error 3")
                    return False
        if s[idx] in numbers and s[idx + 1] in ascii_lowercase:
            # print("error 4") # will never happen, error n°2 always before
            return False

    for char in s:
        if char in punctuation:
            # print("error 5")
            return False

    return True

# print(ascii_lowercase)
# so = "a" in ascii_lowercase
# print(so)
main()
