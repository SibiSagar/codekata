#Check whether a character is an  alphabet or not

alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"



char=input()

if char in alphabet:
    print("Alphabet")

elif char in alphabet.lower():
    print("Alphabet")

else:
    print("No")


