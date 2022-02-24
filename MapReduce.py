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
    count = all_words.count(kw)
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
    for doc in readings[:1]:
        words.append(re.split('\n| ',doc))    


    #below populates list with ALL words from ALL documents without any spaces ||| words_new is a 1D list of strings
    words_new = [] 
    for i in range(len(words)):
        for word in words[i]:
            if len(word) != 0:
                words_new.append(word)
    print("Total amount of words ",len(words_new))
    print("Finished Filtering the Data...")
    #--------------------------------------------- MAP ---------------------------------------   
    #print(len(words_new)) #198,323 words
    # start a parallel section
    print("Mapping the data...")
    start = time.time()
     
        
    with pymp.Parallel(4) as p:
        

        # create a shared dict since bug in OpenMP with outside initialization
        #the shared list of all keywords we need to find
        keywords = pymp.shared.list(["hate", "love", "death", "night", "sleep", "time", "henry", "hamlet", "you",
                                     "my", "blood", "poison", "macbeth", "king", "heart", "honest"])        
        kw_dict = dict.fromkeys(keywords, 0)         
        kw_dictShared = pymp.shared.dict(kw_dict)
        
        #print("In thread:", p.thread_num)      
        countLock = p.lock
        #print("TN>>>>>>>>>>>>>>>>>>>>>",p.thread_num)
        for key_word in p.iterate(keywords):
            print("Thread ", p.thread_num , " : ", key_word)    
            countLock.acquire()
            #Below is mapping words and their frequency
            kw_dictShared[key_word] += count(key_word, words_new)
            countLock.release()
      
        #print( "Thread", p.thread_num, "\n", kw_dictShared)
    print(kw_dictShared)
    elapsed_time = time.time() - start
    print("Elapsed time in seconds for multithreading: ",elapsed_time)
    #------------------------Shuffle and Reduce Method ------------------------------
    
    
    
    
