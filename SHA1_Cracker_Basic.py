import hashlib
import datetime
import sys

with open('./10-million-password-list-top-1000000.txt') as f:
    lines = f.read().splitlines()

goalHash = ""
hashOfSalt = ""
unhashedSalt = ""
salted = False
multiWord = False
attemptCount = 0
attemptCountSalt = 0
solved = False

if len(sys.argv) > 1:
    goalHash = sys.argv[1].lower()
    saltedQuestion = raw_input("Is this hash salted? (y/n) ")
    if saltedQuestion == 'y':
        salted = True
        saltQuestion = raw_input("What is your salt? ")
        hashOfSalt = saltQuestion.lower()
    multiWordQuestion = raw_input("Does this hash consist of two dictionary words divided by a space? (y/n) ")
    if multiWordQuestion == 'y':
        multiWord = True
    if salted and multiWord:
        print "This hash can not be brute forced by this program because it is a salted combination of dictionary terms."
    else:
        startTime = datetime.datetime.now()
        if not salted and not multiWord:
            print("Solving unnsalted single word")
            for x in lines:
                attemptCount += 1
                if hashlib.sha1(x).hexdigest() == goalHash:
                    print("Password is: " + x)
                    solved = True
                    break
        elif not multiWord and salted:
            print("Solving salted single word")
            for x in lines:
                attemptCountSalt += 1
                if hashlib.sha1(x).hexdigest() == hashOfSalt:
                    unhashedSalt = x
                    print "Salt is: " + x
                    print "Took " + str(attemptCountSalt) + " attempts to crack salt."
                    break
            if unhashedSalt != "":
                for x in lines:
                    attemptCount += 1
                    if hashlib.sha1(unhashedSalt + x).hexdigest() == goalHash:
                        print("Password is: " + x)
                        solved = True
                        break
            else:
                print("Could not solve salt")
        elif multiWord and not salted:
            for x in lines:
                for y in lines:
                    attemptCount += 1
                    if hashlib.sha1(x + " " + y).hexdigest() == goalHash:
                        print("Password is " + x + " " + y)
                        solved = True
                        break
                else:
                    hashPerSecond = (float(attemptCount) / (datetime.datetime.now() - startTime).total_seconds())
                    myString = ("Time: " + str(datetime.datetime.now() - startTime) + " | Attempts: " + str(
                        attemptCount) +
                                " | Hashrate: " + str(hashPerSecond) + " hash/s | Possible passwords remaining: " +
                                str((len(lines) ** 2) - attemptCount) + " | Estimated time remaining: " +
                                str(((len(lines) ** 2) - attemptCount) / hashPerSecond) + " seconds")
                    sys.stdout.write('\r'+str(myString))
                    sys.stdout.flush()
                    continue
                break
        if solved:
            print("Time taken: " + str(datetime.datetime.now() - startTime))
            print("Took " + str(attemptCount) + " attempts to crack input hash.")
        else:
            print "Hash not resolvable with current dictionary and parameters."
else:
    print "Please input the desired hash value to crack as a argument when you run the  application."
