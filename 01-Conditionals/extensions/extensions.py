# In a file called extensions.py, implement a program that prompts
# the user for the name of a file and then outputs that file’s media
# type if the file’s name ends, case-insensitively, in any of these suffixes:
            # .gif
            # .jpg
            # .jpeg
            # .png
            # .pdf
            # .txt
            # .zip

# If the file’s name ends with some other suffix or has no suffix at all,
# output application/octet-stream instead, which is a common default.

prompt = input("File name: ").strip()

possibilities = [".gif",".jpg",".jpeg",".png",".pdf",".txt",".zip"]

images = [".gif",".jpg",".jpeg",".png"]
application = [".pdf", ".zip"]
text = [".txt"]

for elem in possibilities:
    extension = prompt.lower().split(".")[-1]
    if elem == "." + extension and extension != "jpg": # not jpg
        if elem in images:
            print(f"image/{extension}")
            break
        elif elem in application:
            print(f"application/{extension}")
            break
        elif elem in text:
            print(f"text/{prompt.lower().split(".")[0]}")
            break
    elif elem == "." + extension and extension == "jpg": # yes jpg
        print(f"image/jpeg")
        break
else:
    print(f"application/octet-stream")
