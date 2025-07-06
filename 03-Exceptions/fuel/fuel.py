# Fuel gauges indicate, often with fractions, just how much fuel is in a tank.
# For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank
# is 50% full, and 3/4 indicates that a tank is 75% full.

# In a file called fuel.py, implement a program that prompts the user for a
# fraction, formatted as X/Y, wherein each of X and Y is a positive integer,
# and then outputs, as a percentage rounded to the nearest integer, how much
# fuel is in the tank. If, though, 1% or less remains, output E instead to
# indicate that the tank is essentially empty. And if 99% or more remains,
# output F instead to indicate that the tank is essentially full.

# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead
# prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch
# any exceptions like ValueError or ZeroDivisionError.

fraction = input("Fraction: ").strip()

def fuel(fraction):
    if "/" in fraction:
        x, y = fraction.split("/")
        # print("x:", x)
        # print("y:", y)
        try:
            if int(x) <= int(y) and y != "0":
                percent = round((int(x)/int(y))*100)
                if percent >= 0:
                    if percent <= 1:
                        return "E"
                    elif percent >= 99:
                        return "F"
                    return percent
                else:
                    return ""
            else:
                return ""
        except ValueError:
            return ""
    else:
        return ""

res = (fuel(fraction))

while True:
    if isinstance(res, str) and res != "E" and res != "F":
        fraction = input("Fraction: ").strip()
        res = fuel(fraction)
    else:
        break

if res != "E" and res != "F":
    print(f"{res}%")
else: print(res)
