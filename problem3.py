#Check whether a character is vowel or consonant

vowel="AaEeIiOoUu"
spl="`~!@#$%^&*()_-+=}{[]'|:;?/><,."
char=input()

if char in vowel:
    print("Vowel")

elif char in spl:
    print("invalid")

else:
    print("Consonant")
