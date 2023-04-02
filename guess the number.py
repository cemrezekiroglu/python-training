#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Guess the number game")
guess_counter = 0


# In[ ]:


while True:
  guess_number = int(input("Type a number between 1 and 1000000"))
  if guess_number < 0:
    print("Negative number.")
    exit()
  elif guess_number > 500000 and guess_number <= 1000000:
    print("Too high.")
    guess_counter += 1
    continue
  elif guess_number < 500000:
    print("Too low.")
    guess_counter += 1
    continue
  elif guess_number == 500000:
    print("You got it right!")
    guess_counter += 1
    print("You got it right in your", guess_counter, "try.")
    exit()
  elif guess_number > 1000000:
    print("Higher than 1000000. Try again.")
    guess_counter +=1
    continue
  else:
    print("Invalid, try again")

