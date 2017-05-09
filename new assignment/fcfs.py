#!/usr/bin/env python
process_queue = []
total_wtime = 0
no_of_processes = int(raw_input('Enter the total no of processes: '))
def input():
    for process_no in xrange(no_of_processes):
        process_queue.append([])
        process_queue[process_no].append(raw_input('Enter p_name: '))
        process_queue[process_no].append(int(raw_input('Enter p_arrival: ')))
        process_queue[process_no].append(int(raw_input('Enter p_bust: ')))
        print '\n'
        
def sort_arrival_time():
  process_queue.sort(key = lambda process_queue:process_queue[1])
  
def show_output(total_wtime):
    print 'ProcessName\tArrivalTime\tBurstTime'
    for process_no in xrange(no_of_processes):
        print process_queue[process_no][0],'\t\t',process_queue[process_no][1],'\t\t',process_queue[process_no][2]
        total_wtime+=process_queue[process_no][1]
    print 'Total waiting time: ',total_wtime
    print 'Average waiting time: ',(total_wtime/no_of_processes)

input()
sort_arrival_time()
show_output(total_wtime)