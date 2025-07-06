prompt = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

mylist = ["42", "forty-two", "forty two"]

for elem in mylist:
    if elem in prompt.lower():
        print("Yes")
        break
else:
    print("No")
