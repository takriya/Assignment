#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Lower Triangular Pattern
def lower_triangular(n):
    for i in range(1, n + 1):
        print('* ' * i)

# Upper Triangular Pattern
def upper_triangular(n):
    for i in range(n, 0, -1):
        print('* ' * i)

# Pyramid Pattern
def pyramid(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '* ' * i)

# Size of the patterns
n = 5

print("Lower Triangular Pattern")
lower_triangular(n)
print("\nUpper Triangular Pattern")
upper_triangular(n)
print("\nPyramid Pattern")
pyramid(n)


# In[ ]:




