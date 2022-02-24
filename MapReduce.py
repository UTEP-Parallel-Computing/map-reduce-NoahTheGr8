# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 19:41:35 2022

@author: R Noah Padilla

Algorithm Map Reduce:
    1. Input 
    2. Map
    3. Sort and Shuffle
    4. Reduce
    5. Output

"""

import re
import pymp

'''
count instances of a group of words and map them into a dictionary


'''

def map_(kw_dict, words):

    for word in words: 
        if word in kw_dict:
            kw_dict[word] += 1        

    return kw_dict
    

'''
combine the similar words
'''
def shuffle_():
    return -1


'''
combine the counts
'''
def reduce_():
    
    return -1


if __name__ == "__main__":
    print("-------------- MAP REDUCE --------------\n")
    
    readings = []    
    
    f = open('shakespeare1.txt', 'r', encoding='utf8')
    s1 = f.read()
    readings.append(s1)
    
    f = open('shakespeare2.txt', 'r', encoding='utf8')
    s2 = f.read()
    readings.append(s2)
    
    f = open('shakespeare3.txt', 'r', encoding='utf8')
    s3 = f.read()
    readings.append(s3)
    
    f = open('shakespeare4.txt', 'r', encoding='utf8')
    s4 = f.read()
    readings.append(s4)
    
    f = open('shakespeare5.txt', 'r', encoding='utf8')
    s5 = f.read()
    readings.append(s5)
    
    f = open('shakespeare6.txt', 'r', encoding='utf8')
    s6 = f.read()
    readings.append(s6)
    
    f = open('shakespeare7.txt', 'r', encoding='utf8')
    s7 = f.read()
    readings.append(s7)
    
    f = open('shakespeare8.txt', 'r', encoding='utf8')
    s8 = f.read()
    readings.append(s8)
    
    
    '''
    Will only do 2 for sake of time
    '''   
    #--------------------------------------------- FILTER --------------------------------------- ------
    
    #get all words from all documents
    words = []
    for doc in readings[:1]:
        words.append(re.split('\n| ',doc))    


    #below populates list with ALL words from ALL documents without any spaces ||| words_new is a 1D list of strings
    words_new = [] 
    for i in range(len(words)):
        for word in words[i]:
            if len(word) != 0:
                words_new.append(word)
  
    #--------------------------------------------- MAP ---------------------------------------   
    #print(len(words_new)) #198,323 words
    # start a parallel section
    with pymp.Parallel(4) as p:
        
        #the shared list of all keywords we need to find
        keywords = pymp.shared.list(["hate", "love", "death", "night", "sleep", "time", "henry", "hamlet", "you", "my", "blood", "poison", "macbeth", "king", "heart", "honest"])        
        
        # create a shared dict since bug in OpenMP with outside initialization
        kw_dict = dict.fromkeys(keywords, 0)         
        kw_dictShared = pymp.shared.dict(kw_dict)
        
        #print(len(words_new) * p.thread_num)
        
        countLock = p.lock
        for i in p.iterate(words_new):
        #splits up words evenly amongst threads using the iterate keyword 
            
            countLock.acquire()
            #-----------TODO call the map function
            kw_dictShared = map_(kw_dictShared, words_new)
            countLock.release()
      
        print( "Thread", p.thread_num, "\n", kw_dictShared)
    
    #------------------------Step 3 ------------------------------
  
    
    

    
