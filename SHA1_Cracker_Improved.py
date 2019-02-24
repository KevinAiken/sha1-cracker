import hashlib
import datetime

# part a hash: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
# part b hash: 801cdea58224c921c21fd2b183ff28ffa910ce31
# part c hash: ece4bb07f2580ed8b39aa52b7f7f918e43033ea1
# part c salt: f0744d60dd500c92c0d37c16174cc58d3c4bdd8e
# part d hash: 34302959e138917ce9339c0b30ec50e650ce6b40
with open('./10-million-password-list-top-1000000.txt') as f:
    lines = f.read().splitlines()

goalHash = "ece4bb07f2580ed8b39aa52b7f7f918e43033ea1".lower()
hashOfSalt = "f0744d60dd500c92c0d37c16174cc58d3c4bdd8e"
unhashedSalt = ""
salted = True
multiWord = False
attemptCount = 0
attemptCountSalt = 0
startTime = datetime.datetime.now()

if not salted and not multiWord:
    print("Unsalted single word")
    for x in lines:
        attemptCount += 1
        if hashlib.sha1(x).hexdigest() == goalHash:
            print("Password is: " + x)
            break
elif not multiWord and salted:
    print("Salted single word")
    for x in lines:
        attemptCountSalt += 1
        if hashlib.sha1(x).hexdigest() == hashOfSalt:
            unhashedSalt = x
            print x
            break
    if unhashedSalt != "":
        for x in lines:
            attemptCount += 1
            if hashlib.sha1(unhashedSalt + x).hexdigest() == goalHash:
                print("Password is: " + x)
                break
    else:
        print("Could not solve salt")
elif multiWord and not salted:
    print(str(datetime.datetime.now() - startTime))
    for x in lines:
        for y in lines:
            if hashlib.sha1(x + " " + y).hexdigest() == goalHash:
                print("found")
                print(x + " " + y)
                break
        else:
            print(str(datetime.datetime.now() - startTime))
            continue
        break
else:
    print("Cannot handle input.")

print("Time taken: " + str(datetime.datetime.now() - startTime))
print("Took " + str(attemptCount) + " attempts.")