import random

rnn = random.randint(10, 99)
hehe = int(input("please guess a number between 10 and 99!"))
for i in range(5):
    if hehe > rnn :
        hehe = int(input("Wrong! Less!\n"))
    elif hehe < rnn :
        hehe = int(input("Wrong! More!\n"))
    elif hehe == rnn : 
        hehe = int(input("Correct! You win!\n"))
        break
    else:
        hehe = int(input("Please write a number between 10-99!"))

print(f"{rnn} was the answer")