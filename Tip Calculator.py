#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Tip Calculator")
total_bill = float(input("Total Bill:"))
of_tip = int(input("% of tip:"))
people = int(input("How many people:"))
answer = (((total_bill * of_tip)/100) + total_bill) / people
rounded = round(answer, 2)
print("Each will pay:", rounded)

