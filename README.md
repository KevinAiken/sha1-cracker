# sha1-cracker
Python SHA1 cracker for GSU's CSC 4980 Blockchain & Applications Course. 

Code is written by Kevin Aiken, the repo author.

This repo includes a dictionary, a basic cracking application, and the assignment handout.

## How to Run

Assuming you have a Python 2.7 environment configured, run `python Sha1_Cracker_Basic.py yourhashhere non-combination unsalted`from the 
terminal for a basic unsalted hash that is not a combination of dictionary terms. 

Program arguments following the following format: `hash non-combination/combination unsalted/salted salt`

Example to brute force a hash that is a combination of two words from the dictionary: `python Sha1_Cracker_Basic.py 34302959e138917ce9339c0b30ec50e650ce6b40 combination unsalted`

Example for a salted password consisting of one word from the dictionary: `python Sha1_Cracker_Basic.py ece4bb07f2580ed8b39aa52b7f7f918e43033ea1 non-combination salted f0744d60dd500c92c0d37c16174cc58d3c4bdd8e`

## Assignment Solutions with Basic Version

These are the hashes assigned to be cracked and their cleartext.

- A) Easy hash
  - Hash: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
  - Clear text: letmein
  - Time to crack: .000054 seconds

- B) Medium difficulty hashw
  - Hash: 801cdea58224c921c21fd2b183ff28ffa910ce31
  - Clear text: vjhtrhsvdctcegth
  - Time to crack: 0.655790

- C) Hash with salt
  - Hash: ece4bb07f2580ed8b39aa52b7f7f918e43033ea1
  - Salt: f0744d60dd500c92c0d37c16174cc58d3c4bdd8e
  - Clear text: harib
  - Time to crack: 0.376532
  - Salt's clear text: slayer

- D) Combination hash consisting of two dictionary words with a space between
  - Note: Cracked using hashcat on a GPU in 4 minutes, as my calculated estimated time was too 
  long for me to run on my system. However the program does work, as it can solve passwords closer to the top of the list.
  - Hash: 34302959e138917ce9339c0b30ec50e650ce6b40
  - Clear text: Alligator1 YpeKawOqO
  - Estimated time to crack: 8.3 days
  
