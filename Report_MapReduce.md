# R Noah Padilla Map Reduce Report
## ABOUT
This programs main purpose is to perform the map reduce algorithm done in parallel in python.

## Problems Encountered and how I overcame them

    
## Total Time it Took to Complete
Total time it took was ~ hours because of the shared memory issues mentioned aboves.

## Performance Measurements
The performance of the program was measured by taking the performance time 'time.perf_time()'. The results are shown below in seconds. 


* 1 thread: 



* 2 threads: 



* 4 threads: 


* 8 threads:



## Program Behavior

## Observations/Comments
.

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
