from random import randint
from copy import deepcopy



class _PreemptivePriorityScheduling: # Class for simulating Preemptive Priority CPU Scheduling
    process_list = [] # List to Store the Processes [PID, AT, BT, RT, PL,CT]
    fourColumnProcessList = []
    waitingTime = 0
    turnaroundTime = 0
    start_times = []
    end_times = []
    
    def inputUser(self, no_of_processes): # USER INPUT
        for process_id in range(1, no_of_processes + 1): # Loop to enter user values for each process
            temporary = [] # Temporary list to store values
            
            while True:
                arrival_time = int(input(f"\nEnter Arrival Time for P{process_id}: ")) # Arrival Time input
                
                if [pr for pr in self.process_list if pr[1] == arrival_time]: # Arrival Time duplicate checker
                    print("Duplicate")
                else:
                    break

            burst_time = int(input(f"Enter Burst Time for P{process_id}: ")) # Burst Time input
            
            remaining_time = deepcopy(burst_time) # Remaining Time is used for the scheduling process to simulate the remaining burst time of the process

            priority_level = int(input(f"Enter Priority Level for P{process_id}: ")) # Priority Level input
            
            completion_time = 0 # Completion Time is the time that the process finished running

            temporary = [f"P{process_id}", arrival_time, burst_time, remaining_time, priority_level, completion_time] # Storing input values inside a list
            
            self.process_list.append(temporary) # Appending the list of values inside the list of processes
        
    def inputRandom(self, no_of_processes, max_BT): # RANDOM INPUT
        half = no_of_processes // 2 
        randomizer_limit = no_of_processes + half # Randomizer limit is 150% of the Number of Processes
        
        for process_id in range(1, no_of_processes + 1): # Loop to enter random values for each process
            temporary = [] 

            while True:
                arrival_time = randint(0, randomizer_limit)
                
                if [pr for pr in self.process_list if pr[1] == arrival_time]:
                    pass
                else:
                    break

            burst_time = randint(1, max_BT)
            
            remaining_time = deepcopy(burst_time)

            priority_level = randint(1, no_of_processes)
            
            completion_time = 0

            temporary = [f"P{process_id}", arrival_time, burst_time, remaining_time, priority_level, completion_time]

            
            self.process_list.append(temporary)
            self.fourColumnProcessList.append([f"P{process_id}", arrival_time, burst_time, priority_level])


        return self.fourColumnProcessList
        
    def schedulingProcess(self, process_list): # Scheduling Algorithm
        start_times = []
        end_times = []
        current_time = 0 # Current Time Frame
        completed_list = [] # List for completed processes
        ready_queue = [] # Memory Queue
        
        while len(completed_list) < len(process_list): # Loop for the Algorithm
            for process in process_list:
                if process[1] <= current_time and process not in completed_list and process not in ready_queue: # Inserting newly arrived processes to the Memory Queue
                    ready_queue.append(process)
            
            # print(f"\nTimeframe {current_time}")
            
            if not ready_queue: # Checking for idle time
                # print(f"R unning: None")
                current_time += 1
                continue # Skip rest of the algorithm if idle time
            
            ready_queue.sort(key=lambda x: x[3]) # Sorting the ready queue based on Priority Level
            
            current_process = ready_queue[0] # Set current process as process with highest level in memory queue
            current_process[3] -= 1 # Decerement current process bust time
            
            # Print Simulation
            # print(f"Running: {current_process[0]}")
            # print(f"Current Burst Time: {current_process[3]}")
            # print(f"Priority Level: {current_process[4]}")
            
            # if current_process[3] == 0:
            #     start_times.append(current_time)
            #     end_times.append(current_time + 1)

            # for i, process in enumerate(completed_list):
            #     start_time = start_times[i]
            #     end_time = end_times[i]
            #     process_name = process[0]
            #     ax.barh(process_name, end_time - start_time, left=start_time, label=process_name)

            
            current_time += 1 # Increment Current Time Frame
        


        # fig, ax = plt.subplots()


        # ax.set_xlabel('Time', fontsize=9)
        # ax.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
        # plt.grid(axis='x')
        # plt.savefig("./GANTT_OUTPUT/GTChart.png", bbox_inches='tight', dpi=100)
        # # Initialize Totals of TT and WT
        # total_wt = 0
        # total_tt = 0
        
        # for process in process_list: # Loop to calculate WT and TT of each rocess
        #     turnaround_time = process[5] - process[1] # Calculate TT of process (Completion Time - Arrival Time)
        #     waiting_time = turnaround_time - process[2] # Calculate WT of process (Turnaround Time - Burst Time)
            
        #     total_wt += waiting_time # Add TT of the process to the total
        #     total_tt += turnaround_time # Add WT of the process to the total
        
        # Compute Averages
        avg_wt = total_wt / len(self.process_list)
        avg_tt = total_tt / len(self.process_list)
        

        self.waitingTime = avg_wt
        self.turnaroundTime = avg_wt
        return completed_list
        # # Print table results
        # print("\nProcess\tWaiting Time\tTurnaround Time")
        # for process in self.process_list:
        #     print(f"{process[0]}\t{process[5] - process[1] - process[2]}\t\t{process[5] - process[1]}")

        # print(f"Average Waiting Time: {avg_wt}")
        # print(f"Average Turnaround Time: {avg_tt}")



# # Main Machinery
def runner():
    proseso = _PreemptivePriorityScheduling() # Create instance
    process_list = proseso.inputRandom(10, 8)
    proseso.schedulingProcess(process_list) # Run Scheduling Algotihm
    

runner()