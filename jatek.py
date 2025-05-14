import random

jatekos1 = []
jatekos2 = []


while len(jatekos1) != 2:
    jatekos1.append(random.randint(2, 11))

while len(jatekos2) != 2:
    jatekos2.append(random.randint(2, 11))


while jatekos1 >= 21 and jatekos2 >= 21:
    


print(jatekos1)
print(jatekos2)