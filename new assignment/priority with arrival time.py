process_queue = []
total_wtime = 0
p_arrival=0
bursttime=0
min_burst=1
no_of_processes = int(raw_input('Enter the total no of processes: '))
def input():
    for process_no in xrange(0,no_of_processes):
        process_queue.append([])
        process_queue[process_no].append(raw_input('Enter p_name: '))
        process_queue[process_no].append(int(raw_input('Enter p_arrival: ')))
        process_queue[process_no].append(int(raw_input('Enter p_bust: ')))
        process_queue[process_no].append(int(raw_input('Enter p_priority: ')))
        print '\n'
        
def sort_arrivaltime_bursttime_priority(bursttime,min_burst):
  for process_no in xrange(no_of_processes):
      for process_no_1 in xrange(no_of_processes-1):
         if process_queue[process_no][1] < process_queue[process_no_1+1][1]:
               temp=process_queue[process_no_1][3]
               process_queue[process_no_1][3]=process_queue[process_no][3]
               process_queue[process_no][3]=temp
               temp=process_queue[process_no_1][1]
               process_queue[process_no_1][1]=process_queue[process_no][1]
               process_queue[process_no][1]=temp
               temp1=process_queue[process_no_1][2]
               process_queue[process_no_1][2]=process_queue[process_no][2]
               process_queue[process_no][2]=temp1
               
  for process_no in xrange(no_of_processes):
      bursttime=bursttime+process_queue[process_no][2]
      minimum=process_queue[min_burst][2]
      new_process=min_burst
      for new_process in xrange(no_of_processes):
         minimum=process_queue[min_burst][3]
         if bursttime>=process_queue[new_process][1]:
            if process_queue[new_process][3]<minimum:
              temp=process_queue[min_burst][0]
              process_queue[min_burst][0]=process_queue[new_process][0]
              process_queue[new_process][0]=temp
              temp=process_queue[min_burst][1]
              process_queue[min_burst][1]=process_queue[new_process][1]
              process_queue[new_process][1]=temp
              temp1=process_queue[min_burst][2]
              process_queue[min_burst][2]=process_queue[new_process][2]
              process_queue[new_process][2]=temp1
              temp=process_queue[min_burst][3]
              process_queue[min_burst][3]=process_queue[new_process][3]
              process_queue[new_process][3]=temp
      min_burst=min_burst+1        
              
              
              
              
  
def show_output(total_wtime):
    print 'ProcessName\tArrivalTime\tBurstTime\tp_priority'
    for process_no in xrange(no_of_processes):
        print process_queue[process_no][0],'\t\t',process_queue[process_no][1],'\t\t',process_queue[process_no][2],'\t\t',process_queue[process_no][3]
        
input()
sort_arrivaltime_bursttime_priority(bursttime,min_burst)
show_output(total_wtime)