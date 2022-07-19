#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
def start_game():
    mat = []
    for i in range(4):
        mat.append([0]*4)
    return mat


# In[2]:


def add_new_2(mat):
    row = random.randint(0,3)
    col = random.randint(0,3)
    while mat[row][col]!=0:
        row = random.randint(0,3)
        col = random.randint(0,3)
    mat[row][col] = 2


# In[1]:





# In[14]:


def merge(mat):
    changed = False
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j+1] and mat[i][j]!=0:
                mat[i][j] = mat[i][j]*2
                mat[i][j+1] = 0
                changed = True
    return mat,changed
            
def compress(mat):
    
    changed = False
    new_mat = []
    for i in range(4):
        new_mat.append([0]*4)
    
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                if j!= pos:
                    changed = True
                pos+=1
    return new_mat,changed


# In[9]:


def reverse(mat):
    new_mat = []
    
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][4-j-1])
    return new_mat

def transpose(mat):
    
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat


# In[12]:


def move_up(grid):
    #Implement This Function
    grid = transpose(grid)
    grid,changed1 = compress(grid)
    grid,changed2 = merge(grid)
    changed = changed1 or changed2
 
    grid,temp = compress(grid)
    grid = transpose(grid)
    
    return grid,changed

    

def move_down(grid):
    #Implement This Function
    grid = transpose(grid)
    grid = reverse(grid)
    grid,changed1 = compress(grid)
    grid,changed2 = merge(grid)
    changed = changed1 or changed2
 
    grid,temp = compress(grid)
    grid = reverse(grid)
    grid = transpose(grid)
    
    return grid,changed


def move_right(grid):
    #Implement This Function
    grid = reverse(grid)
    grid,changed1 = compress(grid)
    grid,changed2 = merge(grid)
    changed = changed1 or changed2
 
    grid,temp = compress(grid)
    grid = reverse(grid)
    return grid,changed


def move_left(grid):
    #Implement This Function
    grid,changed1 = compress(grid)
    grid,changed2 = merge(grid)
    changed = changed1 or changed2
 
    grid,temp = compress(grid)
    
    return grid,changed

def get_current_state(mat):
    
    ## 2048 present
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return 'WON'
    # if 0 is present       
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return 'GAME NOT OVER'
    # Every Row col except last        
    for i in range(3):
        for j in range(3):
            if mat[i][j] == mat[i+1][j] or mat[i][j] == mat[i][j+1]:
                return 'GAME NOT OVER'
    # Last Row        
    for j in range(3):
        if mat[3][j] == mat[3][j+1]:
            return 'GAME NOT OVER'
    # Last Column    
    for i in range(3):
        if mat[i][3] == mat[i+1][3]:
            return 'GAME NOT OVER'
    return 'LOST'

# In[ ]:




