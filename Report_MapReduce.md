# R Noah Padilla Map Reduce Report
## ABOUT
This programs main purpose is to perform the map reduce algorithm done in parallel in python.

## Problems Encountered and how I overcame them
The main issue that I was having was that OpenMP was having the shared dictionary sync with all the threads but could not get it going. I think this is because the OpenMP library is buggy thus leaving issues to the programmer like freezing or locking if the shared dictionary is instantiated outside of the parallel section. 
    
## Total Time Taken
Total time it took was ~10 hours because of the shared memory issue..

## Performance Measurements
The performance of the program was measured by taking the performance time 'time.time()'. The results are shown below in seconds. 


 * 1 thread: 0.1938166618347168


 * 2 threads: 0.24344372749328613


 * 4 threads: 0.2616910934448242


 * 8 threads: 2.1395139694213867


## Program Behavior
It seems that the performance peaked at about 2 threads and then declined. An output run for 1 thread looks like the below -

```
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
Elapsed time in seconds for calculating all the word frequencies:  0.19500064849853516
```

## Observations/Comments
I think that this assignment was good since I leared how to use a shared list and dictionary within the OpenMP libray for the most part. I think that the OpenMP bug really needs to be fixed asap! Other than that, it was a nice lab.


## CPU Info Dump
* model name	: 11th Gen Intel(R) Core(TM) i5-11400F @ 2.60GHz

## HOW TO RUN
1. Clone the repo
2. Install the dependencies 
```
sudo apt update
sudo apt upgrade
sudo apt install python3-pip
pip install numpy
pip install pymp-pypi
sudo apt install libgomp1
```
3. Navigate to this folder and write the following command
```
OMP_NUM_THREADS= <1,2,4,8> python3 MapReduce.py
```
