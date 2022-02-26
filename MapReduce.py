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
import time

'''
counts how many times kw is in all_words

'''
def count(kw, all_words):
    count = all_words.count(kw.lower())
    print("Found ", count, "for ", kw)
    return count


if __name__ == "__main__":
    print("-------------- MAP REDUCE --------------\n")
    
    
    files = ['shakespeare1.txt','shakespeare2.txt','shakespeare3.txt','shakespeare4.txt','shakespeare5.txt',
        'shakespeare6.txt','shakespeare7.txt','shakespeare8.txt']
    readings = []    
    
    for file_ in files:
        f = open(file_, 'r', encoding='utf8')
        s1 = f.read()
        readings.append(s1)
    
    #--------------------------------------------- FILTER --------------------------------------- ------
    
    print("Filtering the Data...")
    #get all words from all documents
    words = []
    for doc in readings[:]:
        words.append(re.split('\n| |,',doc))    


    #below populates 'words_new' list with ALL words from ALL documents without any spaces ||| words_new is a 1D list of strings
    words_new = [] 
    for i in range(len(words)):
        for word in words[i]:
            if len(word) != 0:
                words_new.append(word)
    print("Total amount of words ",len(words_new))
    print("Finished Filtering the Data...")
    #--------------------------------------------- MAP->SHUFFLE->REDUCE ---------------------------------------   
    #print(len(words_new)) #198,323 words
    # start a parallel section
    print("Mapping the data...")
    start = time.time()
    
    global keywords
    global kw_dict
    global kw_dictShared
    with pymp.Parallel() as p:        
        # create a shared dict since bug in OpenMP with outside initialization
        #the shared list of all keywords we need to find
        keywords = pymp.shared.list(["hate", "love", "death", "night", "sleep", "time", "henry", "hamlet", "you", "my", "blood", "poison", "macbeth", "king", "heart", "honest"])        
        kw_dict = dict.fromkeys(keywords, 0)         
        kw_dictShared = pymp.shared.dict(kw_dict)
        
        for key_word in p.iterate(keywords):
            #Below is mapping words and their frequency
            kw_dictShared[key_word] = count(key_word, words_new)
      
        print(kw_dictShared)
    elapsed_time = time.time() - start
    print("Elapsed time in seconds for calculating all the word frequencies: ",elapsed_time)

'''
----------------------------------------- EXAMPLE OUTPUT 1 THREAD -----------------------------------------

Filtering the Data...
Total amount of words  961909
Finished Filtering the Data...
Mapping the data...
Found  150 for  hate
Found  1746 for  love
Found  563 for  death
Found  493 for  night
Found  175 for  sleep
Found  899 for  time
Found  0 for  henry
Found  0 for  hamlet
Found  11172 for  you
Found  11425 for  my
Found  530 for  blood
Found  65 for  poison
Found  0 for  macbeth
Found  296 for  king
Found  775 for  heart
Found  246 for  honest
{'hate': 150, 'love': 1746, 'death': 563, 'night': 493, 'sleep': 175, 'time': 899, 'henry': 0, 'hamlet': 0, 'you': 11172, 'my': 11425, 'blood': 530, 'poison': 65, 'macbeth': 0, 'king': 296, 'heart': 775, 'honest': 246}
Elapsed time in seconds for calculating all the word frequencies:  0.1938166618347168





'''   
    
    
    
