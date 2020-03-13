import random
my_number = random.randint(0,20)
guess = -1
print(my_number)
while guess!=my_number:
    guess = int(input())
    if guess == my_number:
       print("Gratulacje moja liczba to %d!\n"%my_number)
    elif guess > my_number:
        print("Moja liczba jest mniejsza!\n")
    else: print("Moja liczba jest wieksza!\n")
