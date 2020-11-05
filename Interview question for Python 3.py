#!/usr/bin/env python
# coding: utf-8

# In[1]:


input_value = {
  'hired': {
    'be': {
      'to': {
        'deserve': 'I'
      }
    }
  }
}


# In[2]:


def dictreverse(input_value):
    AllList = []
    global inside
    while isinstance(input_value,dict):
        AllList.append(list(input_value.keys())[0])
        input_value = input_value[list(input_value.keys())[0]]

    AllList.append(input_value)

    for i in range(len(AllList)-1):
        if i == 0: 
            inside = {AllList[1]:AllList[0]}
        else:
            inside = {AllList[i+1]:inside}

    return(inside)

dictreverse(input_value)

