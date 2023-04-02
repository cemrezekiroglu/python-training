#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from getpass import getpass as input
print("Rock, Paper, Scissors Game")


# In[ ]:


player_1_counter = 0
player_2_counter = 0


# In[ ]:


while True:
  player_1 = input("R for Rock, P for Paper and S for Scissors>")
  print()
  player_2 = input("R for Rock, P for Paper and S for Scissors>")
  print()
  if player_1 == "R" or player_1== "r":
    if player_2 == "R" or player_2 == "r":
      print("Tied!")
      if player_1_counter == 3 or player_2_counter==3:
        print("Thanks for playing!")
        print("Player 1 has", player_1_counter, "points and player 2 has", player_2_counter, "points.")
        if player_1_counter > player_2_counter:
          print("Player 1 wins!")
        else:
          print("Player_2 wins!")
        exit()
      else:
        continue
    elif player_2 == "S" or player_2 == "s":
      print("You won!")
      player_1_counter += 1
      if player_1_counter == 3 or player_2_counter==3:
        print("Thanks for playing!")
        print("Player 1 has", player_1_counter, "points and player 2 has", player_2_counter, "points.")
        if player_1_counter > player_2_counter:
          print("Player 1 wins!")
        else:
          print("Player 2 wins!")
        exit()
      else:
        continue
    else:
      print("You lost :(")
      player_2_counter += 1
      if player_1_counter == 3 or player_2_counter==3:
        print("Thanks for playing!")
        print("Player 1 has", player_1_counter, "points and player 2 has", player_2_counter, "points.")
        if player_1_counter > player_2_counter:
          print("Player 1 wins!")
        else:
          print("Player 2 wins!")
        exit()
      else:
        continue
  elif player_1 == "S" or player_1== "s":
    if player_2 == "p" or player_2=="P":
      print("You won!")
      player_1_counter += 1
      if player_1_counter == 3 or player_2_counter==3:
        print("Thanks for playing!")
        print("Player 1 has", player_1_counter, "points and player 2 has", player_2_counter, "points.")
        if player_1_counter > player_2_counter:
          print("Player 1 wins!")
        else:
          print("Player 2 wins!")
        exit()
      else:
        continue
    elif player_2 == "s" or player_2== "S":
      print("Tied!")
      if player_1_counter == 3 or player_2_counter==3:
        print("Thanks for playing!")
        print("Player 1 has", player_1_counter, "points and player 2 has", player_2_counter, "points.")
        if player_1_counter > player_2_counter:
          print("Player 1 wins!")
        else:
          print("Player 2 wins!")
        exit()
      else:
        continue
    else:
      print("You lost :(")
      player_2_counter += 1
      if player_1_counter == 3 or player_2_counter==3:
        print("Thanks for playing!")
        print("Player 1 has", player_1_counter, "points and player 2 has", player_2_counter, "points.")
        if player_1_counter > player_2_counter:
          print("Player 1 wins!")
        else:
          print("Player 2 wins!")
        exit()
      else:
        continue
  elif player_1 == "p" or player_1 == "P":
      if player_2 == "s" or player_2 == "S":
        print("You lost :(")
        player_2_counter += 1
        if player_1_counter == 3 or player_2_counter==3:
          print("Thanks for playing!")
          print("Player 1 has", player_1_counter, "points and player 2 has", player_2_counter, "points.")
          if player_1_counter > player_2_counter:
            print("Player 1 wins!")
          else:
            print("Player_2 wins!")
          exit()
        else:
          continue
      if player_2 == "p" or player_2=="P":
        print("Tied!")
        if player_1_counter == 3 or player_2_counter==3:
          print("Thanks for playing!")
          print("Player 1 has", player_1_counter, "points and player 2 has", player_2_counter, "points.")
          if player_1_counter > player_2_counter:
            print("Player 1 wins!")
          else:
            print("Player_2 wins!")
            exit()
        else:
          continue
      else:
        print("You won!")
        player_1_counter += 1
        if player_1_counter == 3 or player_2_counter==3:
          print("Thanks for playing!")
          print("Player 1 has", player_1_counter, "points and player 2 has", player_2_counter, "points.")
          if player_1_counter > player_2_counter:
            print("Player 1 wins!")
          else:
            print("Player_2 wins!")
            exit()
        else:
          continue
  else:
    print("Invalid move. Please try again!")
    continue

