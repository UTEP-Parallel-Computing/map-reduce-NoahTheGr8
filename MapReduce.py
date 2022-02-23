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


def map_phase():
    return -1
    
def sort_n_shuffle_phase():
    return -1

def reduce_phase():
    
    return -1


if __name__ == "__main__":
    print("-------------- MAP REDUCE --------------\n")
    
    readings = []    
    
    f = open('map-reduce-NoahTheGr8/shakespeare1.txt', 'r', encoding='utf8')
    s1 = f.read()
    readings.append(s1)
    
    f = open('map-reduce-NoahTheGr8/shakespeare2.txt', 'r', encoding='utf8')
    s2 = f.read()
    readings.append(s2)
    
    f = open('map-reduce-NoahTheGr8/shakespeare3.txt', 'r', encoding='utf8')
    s3 = f.read()
    readings.append(s3)
    
    f = open('map-reduce-NoahTheGr8/shakespeare4.txt', 'r', encoding='utf8')
    s4 = f.read()
    readings.append(s4)
    
    f = open('map-reduce-NoahTheGr8/shakespeare5.txt', 'r', encoding='utf8')
    s5 = f.read()
    readings.append(s5)
    
    f = open('map-reduce-NoahTheGr8/shakespeare6.txt', 'r', encoding='utf8')
    s6 = f.read()
    readings.append(s6)
    
    f = open('map-reduce-NoahTheGr8/shakespeare7.txt', 'r', encoding='utf8')
    s7 = f.read()
    readings.append(s7)
    
    f = open('map-reduce-NoahTheGr8/shakespeare8.txt', 'r', encoding='utf8')
    s8 = f.read()
    readings.append(s8)
    
    
    '''
    Will only do 2 for sake of time
    '''   
    #------------------------Step 1------------------------------
    
    #split - calculate total amount of words and split them into 4 groups since the are 4 processors >>right here p.range would do it
    
    lines = []
    for doc in readings[:2]:
        lines.append(re.split('\n| ',doc))    

    words = [] #list of ALL words from all documents
    for i in range(len(lines)):
        for line in lines[i]:
            if len(line) != 0:
                words.append(line)
    
    #------------------------Step 2------------------------------
    #shuffle - from all the mappings 
    
    
    
    #------------------------Step 3 ------------------------------
    #reduce
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
