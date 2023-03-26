#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Project 1: Selection/Insertion Sort
#Q: [22,27,16,2,18,6]
#Yukarı verilen dizinin sort türüne göre aşamalarını yazınız.
#Big-O gösterimini yazınız.
#Time Complexity: Dizi sıralandıktan sonra 18 sayısı aşağıdaki case'lerden hangisinin kapsamına girer? Yazınız

#[7,3,5,8,2,9,4,15,6] dizisinin Selection Sort'a göre ilk 4 adımını yazınız.

Step 1: [2,27,16,22,18,6]
Step 2: [2,6,16,22,18,27]
Step 3: [2,6,16,18,22,27]
Step 4: [2,6,16,18,27,22]
    
Big-O = n * (n+1)/2
        n^2 + n / 2
dominant: n^2
        O(n^2)

Time Complexity 18: Average Case.


# In[ ]:


#Project 2: Merge Sort
#[16,21,11,8,12,22]
#Yukarıdaki dizinin sort türüne göre aşamalarını yazınız.
#Big-O gösterimini yazınız.

Step 1: [16,21,11] and [8,12,22]
Step 2: [16,21] and [11] and [8,12] and [22]
Step 3: [16] and [21] and [11] and [8] and [12] and [22]
Step 4: [16,21] and [11] and [8,12] and [22]
Step 5: [11,16,21] and [8,12,22]
Step 6: [8,11,12,16,21,22]
    
Big-O: log(n)


# In[ ]:


#Project 3: [7, 5, 1, 8, 3, 6, 0, 9, 4, 2] dizisinin Binary-Search-Tree aşamalarını yazınız.

x = 7
y = 8, 6, 9
z = 5, 4, 2, 1, 3, 0,  

