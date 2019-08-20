'''Given a string S of length N, print the vowels first and then consonants in the same order as they have occurred in the string.
Input Size : N <= 10000
Sample Testcase :
INPUT
asdaqrew
OUTPUT
aaesdqrw'''

string=input()
v=[]
c=[]
ostring=""
vowel="aeiou"

for i in range(0,len(string)):
    if string[i] in vowel:
        v.append(string[i])
    else:
    	c.append(string[i])

v=sorted(v)
c=sorted(c)
v.extend(c)

for j in v:
	ostring+=j

print(ostring)
