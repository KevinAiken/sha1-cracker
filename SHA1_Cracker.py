import hashlib

with open('./10-million-password-list-top-1000000.txt') as f:
    lines = f.read().splitlines()

for x in lines:
    if(hashlib.sha1(x).hexdigest() == "b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3"):
        print("found")
        print(x)
        break


print("Done")