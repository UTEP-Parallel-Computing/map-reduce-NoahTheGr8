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
import time
from mpi4py import MPI

'''
counts how many times kw is in all_words

'''
def count(kw, all_words):
    counter = all_words.count(kw.lower())
    #print("Found ", count, "for ", kw)
    return counter

def updateDict(mainDict, newDict):
    
    for key in mainDict:
        mainDict[key] += newDict[key]
    
    return mainDict


if __name__ == "__main__":
    
    files = ['shakespeare1.txt','shakespeare2.txt','shakespeare3.txt','shakespeare4.txt','shakespeare5.txt','shakespeare6.txt','shakespeare7.txt','shakespeare8.txt']
    readings = [] 
    
    for file_ in files:
        f = open(file_, 'r')
        s1 = f.read().split()
        readings.append(s1)
            
    #----------------------- FILTER -----------------------
    
    #get all words from all documents
    all_words = []
    for wordset in readings:
        all_words.extend(wordset)
    
    #----------------------- MAP->SHUFFLE->REDUCE -----------------------   
    #print(len(words_new)) #198,323 words
    # start a parallel section    
    # get the world communicator
    comm = MPI.COMM_WORLD

    # get our rank (process #)
    rank = comm.Get_rank()

    # get the size of the communicator in # processes
    size = comm.Get_size()
   
    
    #----------------------------------
    #list of all words we want to find
    keywords = ["hate", "love", "death", "night", "sleep", "time", "henry", "hamlet", "you", "my", "blood", "poison", "macbeth", "king", "heart", "honest"]
    kw_dict = dict.fromkeys(keywords, 0)         
      
    
    # thread 0 distributes the work
    if rank is 0:
        print("Total amount of words ",len(all_words))
        print("Finished Filtering the Data...")
        print('Thread 0 distributing')
        print("Mapping the data...")
        

        wordsPerThread = len(all_words) / size

        # first setup thread 0s slice of the list
        localList = all_words[:int(wordsPerThread)]
        print("Thread ", rank, " ", 0 , int(wordsPerThread))
        
        start = time.time()
        #distributes the sub lists
        for process in range(1, size):
            #start and end of slice we're sending
            startOfSlice = int( wordsPerThread * process )
            endOfSlice = int( wordsPerThread * (process + 1) )
            sliceToSend = all_words[startOfSlice:endOfSlice]
            print("Thread ", process, " ", startOfSlice , endOfSlice)
            comm.send(sliceToSend, dest=process, tag=0)
        
        
        #counts the keywords within the list of all words in the first sublist
        for key_word in keywords:
            #Below is mapping words and their frequency
            kw_dict[key_word] = count(key_word, localList)
        
        #thread 0 tells the rest of the threads to count instances of each word
        for process in range(1,size):
            dic = comm.recv(source = process, tag = 1)
            kw_dict = updateDict(kw_dict, dic)
            
        elapsed_time = time.time() - start
        print(kw_dict)
        print("Elapsed time in seconds for calculating all the word frequencies: ",elapsed_time)

            
    #everyone else receives that message
    else:
        # receive a message from thread 0 with tag of 0
        localList = comm.recv(source=0, tag=0)
        
        #get the count of each word in the list it was given from thread 0
        for key_word in keywords:
            #Below is mapping words and their frequency
            kw_dict[key_word] = count(key_word, localList)
            
        #send the info to thread 0, to update the main dictionary
        comm.send(kw_dict,dest = 0, tag = 1)       

'''
-------------------- EXAMPLE OUTPUT THREADS (RANKS) --------------------

'''   
    
    
    
