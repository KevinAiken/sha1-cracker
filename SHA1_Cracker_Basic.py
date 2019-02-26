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

if len(sys.argv) > 3:
    if(sys.argv[2] == "combination"):
        multiWord = True
    if(sys.argv[3] == "salted"):
        salted = True
        if(len(sys.argv) > 4):
            hashOfSalt = sys.argv[4].lower()
    goalHash = sys.argv[1].lower()
    if salted and multiWord:
        print "This hash can not be brute forced by this program because it is a salted combination of dictionary terms."
    else:
        startTime = datetime.datetime.now()
        if not salted and not multiWord:
            #print("Solving unnsalted single word")
            for x in lines:
                attemptCount += 1
                if hashlib.sha1(x).hexdigest() == goalHash:
                    print("Password is: " + x)
                    solved = True
                    break
        elif not multiWord and salted:
            #print("Solving salted single word")
            for x in lines:
                attemptCountSalt += 1
                if hashlib.sha1(x).hexdigest() == hashOfSalt:
                    unhashedSalt = x
                    # print "Salt is: " + x
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
            print("Took " + str(attemptCount) + " attempts to crack input hash. Time Taken: " + str(datetime.datetime.now() - startTime))
        else:
            print "Hash not resolvable with current dictionary and parameters."
else:
    print "Please run the application with all necessary arguments. Example: python SHA1_Cracker_Basic.py ece4bb07f2580ed8b39aa52b7f7f918e43033ea1 non-combination salted f0744d60dd500c92c0d37c16174cc58d3c4bdd8e"
    print "For more examples read the readme."
