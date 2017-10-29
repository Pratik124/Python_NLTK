
# coding: utf-8

# In[5]:

import pandas as pd
import numpy as np
import nltk, re, pprint
import string
from collections import Counter
from nltk.tokenize import sent_tokenize,word_tokenize
from urllib import request
text=open('MobyDick.txt',encoding="latin1").read() #extracting the book
c=0
example_text =word_tokenize(text)  #word tokenizing it with nltk
c=Counter(example_text)            #running the counter to see the frequecy of each word in the text file
#print(c)
with open('tags.txt','r') as f:    #reading the tag file
    words = f.read().split()       #splitting according to the word to save it in a list
    #print(words)
    
with open('MobyDick.txt',encoding='utf8') as g:    #reading the mobydick file
    text = g.read().split()                        #splitting according to the word to save it in a list
    #print(text)
    
   #below is a logical approach to find out the how many time each tag appear in each book

    
    # for each word in words()                 #we have to extract each word in the words list(tag file)
     # count=0                                  #set the count to zero
      #parse through the text and if found      #check the word is present in the text list(mobydick file) and if found increase the counter
       # count= count+1
       #print(word, count)                      #at the end of parsing loop finally print the word and the count
    


# In[ ]:




# In[ ]:



