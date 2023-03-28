#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Exam Grade Calculator")
point= int(input("Your grade:"))
if point < 50:
  print("Your grade is", point, "and you've got U")
elif point >=50 and point <= 59:
  print("Your grade is", point, "and you've got D")
elif point >=60 and point <=69:
  print("Your grade is", point, "and you've got C")
elif point >=70 and point <=79:
  print("Your grade is", point, "and you've got B")
elif point >=80 and point <=89:
  print("Your grade is", point, "and you've got A")
elif point >=90 and point <=100:
  print("Your grade is", point, "and you've got A+")
else:
  print(point, "is either greater than 100 or negative, please try again.")

