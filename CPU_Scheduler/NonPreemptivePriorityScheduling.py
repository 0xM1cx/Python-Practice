from random import randint
from rich.console import Console
from rich.table import Table
from time import sleep
from os import system

console = Console()

# This is a Non-Preemtive Priotity Scheduling Program
# Round Robin nak nabutang kay ambot, wa ko na ayusa kay bayn maruba 
class _NonPreemptivePriorityScheduling:

    processList = []
    process_Timing = {}
    # Function to get the user input for processes
    def User_Input(self, Num_Process):
        for IDprocess in range(1, Num_Process + 1):
            tempList = []
            
            # Prompt for arrival time, burst time, and priority level
            arrivalTime = int(input(f"\nP{IDprocess} Arrival Time: "))
            burstTime = int(input(f"P{IDprocess} Burst Time: "))
            Priority = int(input(f"P{IDprocess} Priotiy lvl: "))
            
            tempList = [f"P{IDprocess}", arrivalTime, burstTime, Priority]
            
            self.processList.append(tempList)
    # Function that generates random input for processes
    def Random_Input(self, Num_Process, Max_Burst):
        half = Num_Process // 2
        randomizer_limit = Num_Process + half
        
        for IDprocess in range(1, Num_Process + 1):
            tempList = []

            while True:
                arrivalTime = randint(0, randomizer_limit)
                if [_process for _process in self.processList if _process[1] == arrivalTime]:
                    pass
                else:   
                    break

            burstTime = randint(1, Max_Burst)
            Priority = randint(1, Num_Process)
            
            tempList = [f"P{IDprocess}", arrivalTime, burstTime, Priority]

            self.processList.append(tempList)
        
        return self.processList

    # Execution of the Algorithm
    def Execute(self, processList):
        # Gin comment out ko anay kay dire gamit
        # table = Table(title="Non-Preemptive Priority Scheduling", style="bold white")
        # table.add_column("Process ID", style="bold cyan", justify="center")
        # table.add_column("Arrival Time", style="bold cyan", justify="center")
        # table.add_column("Burst Time", style="bold cyan", justify="center")
        # table.add_column("Priority Level", style="bold cyan", justify="center")

        # for process in self.processList:
        #     table.add_row(process[0], str(process[1]), str(process[2]), str(process[3]))
        
        
        currentTime = 0
        ProcessComplete = []
        MemoryQueue = []
        process_timings = {}
        # print("\n\n--------Gantt Chart Simulation--------") # Simulation or displaying of process of the algorithm
        while len(ProcessComplete) < len(self.processList):
            for process in self.processList:
                if process[1] <= currentTime and process not in ProcessComplete and process not in MemoryQueue:
                    MemoryQueue.append(process)

            # console.print(f"\nTimeframe {currentTime}")

            # Executed if there is no Process in the moment
            if not MemoryQueue:
                # console.print(f"Running: None\n")
                # console.rule(style="green", characters="-")
                # sleep(1)
                currentTime += 1
                continue

            MemoryQueue.sort(key=lambda x: (x[3], x[1]))  # Sort by priority and arrival time
            
            current_process = MemoryQueue.pop(0) # pops the first elemnt stored in the memory queue
            ProcessComplete.append(current_process)
            self.process_Timing[current_process[0]] = (currentTime, currentTime+current_process[2])
            print(f"{current_process[0]} : {currentTime} - {currentTime+current_process[2]}")
            currentTime += current_process[2]


            # console.print(f"Running: {current_process[0]}")
            # console.print(f"Burst Time: {current_process[2]}")
            # console.print(f"Priority lvl: {current_process[3]}\n")
            # console.rule(style="green", characters="-")
            # sleep(1)


        # totalWT = 0
        # totalTT = 0

        # for process in self.processList:
        #     turnarroundTime = currentTime - process[1]
        #     waitingTime = turnarroundTime - process[2]

        #     totalWT += waitingTime
        #     totalTT += turnarroundTime

        # WT = totalWT / len(self.processList) # Waiting time
        # TT = totalTT / len(self.processList) # Turnaround TIme

        G_fig, G_ax = plt.subplots()
        for i, (process, timings) in enumerate(process_Timing.items()):
            start, end = timings
            ax.barh(i, end - start, left=start, align='center', label=process)

        ax.set_xlabel('Time')
        ax.set_yticks(range(len(process_Timing)))
        ax.set_yticklabels(process_Timing.keys())
        ax.set_title('Gantt Chart')
        plt.legend(loc='upper right')
        plt.grid(axis='x')
        plt.savefig("./GANTT_OUTPUT/GTChart.png", bbox_inches='tight', dpi=150)
        


        # return self.process_Timing
        # table2 = Table(title="Results", style="bold white")
        # table2.add_column("Process ID", style="bold cyan", justify="center")
        # table2.add_column("Waiting Time", style="bold cyan", justify="center")
        # table2.add_column("Turnaround Time", style="bold cyan", justify="center")

        # for process in self.processList:
        #     waitingTime = currentTime - process[1] - process[2]
        #     turnarroundTime = waitingTime + process[2]
        #     table2.add_row(process[0], str(waitingTime), str(turnarroundTime))

        # console.print(table2)

        # console.print(f"WT average: {WT}")
        # console.print(f"TT average: {TT}\n\n")


# # Main Function of the program
# def mainFunction():
#     The_User = _NonPreemptivePriorityScheduling()

#     Number_of_process = int(input("Number of process: "))
#     print("\n\t[ 1 ] User Input ->")
#     print("\t[ 2 ] random INput->")
#     UR = int(input("\nUser or Random Input? >>  "))

#     if UR == 1:
#         The_User.User_Input(Number_of_process)
#     elif UR == 2:
#         The_User.Random_Input(Number_of_process, 10)
        
#     The_User.Execute(The_User.processList)



# mainFunction()
