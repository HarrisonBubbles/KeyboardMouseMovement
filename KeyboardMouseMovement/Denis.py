import random as rd
import time

character = "0123456789abcdefghijklmnopqrstuvwxyxzABCDEFGHIJKLMNOPQRSTUVWXYZ"

password = input("Enter your password:")
start = time.time()
guess = ""
i = 0
num_guesses = 0
letters = []

while i < len(password):
    while (guess != password[i]):
        guess = rd.choice(character)
        num_guesses += 1
        
    letters.append(guess)  

    i += 1

print("Your password is: " + "".join(letters))
print("Number of guesses:" + str(num_guesses))
print(len(password))
print("--- %s seconds ---" % (time.time() - start))