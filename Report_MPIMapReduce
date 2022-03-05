# R Noah Padilla Map Reduce Report
## ABOUT
This programs main purpose is to perform the map reduce algorithm done in parallel using MPI (mpi4py) in python.

## Problems Encountered and how I overcame them
The main issue that I was having with this program was performing the regex operations. I don't think I was performing the regex part right BUT I was doing that parallel part correctly. Since this lab was not about regex, I believe I did perform and complete the intended purpose of this program. I did not correct this problem but I don't think it was worth fixing since the point of this lab was not to perform regex functionality correctly.
    
## Total Time Taken
Total time it took was ~10 hours because regex issue. Although I didn't fix it, I did try which took about a 3rd of that time.

## Performance Measurements
The performance of the program was measured by taking the performance time 'time.time()'. The results are shown below in seconds. 


 * 1 thread: 0.8080966472625732


 * 2 threads: 0.9912528991699219


 * 4 threads: 1.1351990699768066


 * 8 threads: 2.198441743850708


## Program Behavior
It seems that the performance peaked at about 1 threads and then declined. An output run for 1 thread looks like the below -

```
Total amount of words  961257
Finished Filtering the Data...
Thread 0 distributing
Mapping the data...
Thread  0   0 120157
Thread  1   120157 240314
Thread  2   240314 360471
Thread  3   360471 480628
Thread  4   480628 600785
Thread  5   600785 720942
Thread  6   720942 841099
Thread  7   841099 961257
{'hate': 121, 'love': 1335, 'death': 364, 'night': 286, 'sleep': 113, 'time': 711, 'henry': 0, 'hamlet': 0, 'you': 9592, 'my': 11425, 'blood': 368, 'poison': 50, 'macbeth': 0, 'king': 175, 'heart': 565, 'honest': 217}
Elapsed time in seconds for calculating all the word frequencies:  5.109552383422852
```

## Observations/Comments
I think that this assignment was good and way BETTER than the pymp assignment. I understood how it was working a lot more and also because it was less buggy than pymp. What I noticed was that the performance declined as the number of ranks/process increased. Another observation worth mentioning is how MPI executes the file - each thread executes the ENTIRE code over again whereas in pymp, the parallel section was the only part that repeated. Lastly, I noticed pymp worked a lot better than mpi4py - I believe that its because of assigning the ranks that costs that extra time.


## CPU Info Dump
* model name: Intel(R) Core(TM) i7-1065G7 CPU @ 1.30GHz

## HOW TO RUN
1. Clone the repo

2. Navigate to this folder and write the following command
```
mpirun -n <1,2,4,8> python3 MapReduceMPI.py
```
