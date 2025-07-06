# In a file called bank.py, implement a program
# that prompts the user for a greeting.

# If the greeting starts with “hello”, output $0.
# If the greeting starts with an “h” (but not “hello”), output $20.
# Otherwise, output $100.

# Ignore any leading whitespace in the user’s greeting, and
# treat the user’s greeting case-insensitively.

prompt = input("Greeting: ")
prompt = prompt.strip()

if "hello" in prompt.split()[0].lower(): # first word
    output = "$0"
elif prompt.split()[0][0].lower() == "h": # first letter
    output = "$20"
else:
    output = "$100"

print(output)
