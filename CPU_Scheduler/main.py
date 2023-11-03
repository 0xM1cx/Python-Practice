import customtkinter, math, os
from NonPreemptivePriorityScheduling import _NonPreemptivePriorityScheduling
from CTkTable import *
from matplotlib import pyplot as plt
from matplotlib.table import Table
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

NP = 0


class ProcessTableBox(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)
        self.height = 4000
        global NP
        if NP > 30 and NP <= 50:
            self.height = 1500
        elif NP <= 30 and NP >= 20:
            self.height = 1000
        elif NP < 20:
            self.height = 500

        # Label For Process Table
        self.title = customtkinter.CTkLabel(self, text="Process Table", fg_color="transparent", font=("Arial", 20))
        self.title.grid(row=0, column=0, sticky="ew", pady=20, padx=20)

        self.myimg = customtkinter.CTkImage(Image.open("table.png"), size=(400, self.height))
        self.imgLabel = customtkinter.CTkLabel(self, image=self.myimg, text="")
        self.imgLabel.grid(row=1, column=0, sticky="nsew")


class GanttChartBox(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)
        self.height = 4000
        global NP
        if NP > 30 and NP <= 50:
            self.height = 1500
        elif NP <= 30 and NP >= 20:
            self.height = 1000
        elif NP < 20:
            self.height = 500       

        # Label for GANTT Chart
        self.title = customtkinter.CTkLabel(self, text="GANTT Chart", fg_color="transparent", font=("Arial", 20))
        self.title.grid(row=0, column=0, sticky="ew", pady=20, padx=20)

        ## WT Avg
        self.title = customtkinter.CTkLabel(self, text="Waiting Time Average", fg_color="transparent", font=("Arial", 10))
        self.title.grid(row=1, column=0, sticky="ew", pady=20, padx=20)
        self.WT_Result = customtkinter.CTkLabel(self, text=" Result", fg_color="transparent", width=20)
        ## TT Avg
        self.title = customtkinter.CTkLabel(self, text="Turnaround Time Average", fg_color="transparent", font=("Arial", 10))
        self.title.grid(row=2, column=0, sticky="ew", pady=20, padx=20)
        self.TT_Result = customtkinter.CTkLabel(self, text="Result", fg_color="transparent", width=20)

        self.myimg = customtkinter.CTkImage(Image.open("table.png"), size=(400, self.height))
        self.imgLabel = customtkinter.CTkLabel(self, image=self.myimg, text="")
        self.imgLabel.grid(row=3, column=0, sticky="nsew")



class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("880x500")
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        # self.fig, self.ax = plt.subplots()
        # self.table = self.ax.table(cellText=self.values, loc='center', cellLoc='center')
        # self.ax.axis("off")
        # self.table.auto_set_font_size(False)
        # self.table.set_fontsize(12)
        # self.table.scale(1, 1.5)
        # plt.savefig("table.png")

        
        # self.myimg = customtkinter.CTkImage(Image.open("table.png"), size=(400, 400))
        # self.imgLabel = customtkinter.CTkLabel(self, image=self.myimg, text="")
        # self.imgLabel.grid(row=0, column=0, sticky="nsew")

        # Instantiating Process Table Frame
        self.Process_Table_Box = ProcessTableBox(self)
        self.Process_Table_Box.grid(row=0, column=0, sticky="nsew", pady=20, padx=20)

        # Instantiating Process 
        self.Gantt_Chart_Box = GanttChartBox(self)
        self.Gantt_Chart_Box.grid(row=0, column=1, sticky="nsew", pady=20, padx=20)





        
class OptionWindow(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.NonPPS_Instance = _NonPreemptivePriorityScheduling()
        # self.Plot_Window = PlotWindow(self)
        
        #Burst Time Slider
        self.BTLabel = customtkinter.CTkLabel(self, text="Unsay Max Burst Time imo gusto", fg_color="transparent")
        self.BTLabel.grid(row=0, column=0)
        self.Burst_Time = customtkinter.CTkSlider(self, from_=1, to=15, command=self.setBT, number_of_steps=15)
        self.Burst_Time.grid(row=1, column=0, padx=10, pady=10)
        self.BTSlider_CurValue = customtkinter.CTkLabel(self, text=math.trunc(self.Burst_Time.get()), fg_color="transparent", width=20)
        self.BTSlider_CurValue.grid(row=1, column=1)
        
        #Input Box for Number of Processes
        self.Process_InputLabel = customtkinter.CTkLabel(self, text="Pila kabuok imo Processes")
        self.Process_InputLabel.grid(row=0, column=2)
        self.Process_Input = customtkinter.CTkEntry(self, placeholder_text="Number of Processes", width=190)
        self.Process_Input.grid(row=1, column=2, padx=10, pady=10)

        # What Algorithm to Use
        self.AlgoChoice = customtkinter.CTkLabel(self, text="What Algorithm to Use?", fg_color="transparent")
        self.AlgoChoice.grid(row=0, column=3)
        self.AlgoMenu = customtkinter.CTkOptionMenu(self, values=["Preemptive Priority Scheduling", "Non-Preemtive Priotity Scheduling"], 
        width=250)
        self.AlgoMenu.grid(row=1, column=3)

        # Start Button
        self.start_Btn = customtkinter.CTkButton(self, text="Pagsugod", command=self.startExecution)
        self.start_Btn.grid(row=1, column=4, padx=10, pady=10)
        

    def setBT(self, value):
        self.BTSlider_CurValue.configure(text=math.trunc(value))
    
    def GenerateTable(self):
        global NP
        NP = int(self.Process_Input.get())
        self.columnTitles = ["Process ID", "Arrival Time", "Burt Time", "Priority Number"]
        self.processList = self.NonPPS_Instance.Random_Input(int(self.Process_Input.get()), math.trunc(self.Burst_Time.get()))
        self.data = [self.columnTitles]
        for i in self.processList:
            self.data.append(i)

        self.fig, self.ax = plt.subplots()
        self.table = self.ax.table(cellText=self.data, loc='center', cellLoc='center')
        self.ax.axis("off")
        self.table.auto_set_font_size(False)
        self.table.set_fontsize(10)
        self.table.scale(1, 1.5)
        self.fig.tight_layout()
        plt.savefig("table.png", bbox_inches='tight', dpi=150)
        # plt.show()



    
    def startExecution(self):
        if self.AlgoMenu.get() == "Preemptive Priority Scheduling":
            ## Draw Table for processes
            pass
            ## Draw GANTT Chart
        elif self.AlgoMenu.get() == "Non-Preemtive Priotity Scheduling":
            self.GenerateTable()
            self.toplev = ToplevelWindow(self)

            # self.Plot_Window.DrawTable(int(self.Process_Input.get()))
            # self.TopWin = ToplevelWindow(self)
            # self.myimg = customtkinter.CTkImage(light_image=Image.open("table.png"), size=(100,100))
            # self.imgLabel = customtkinter.CTkLabel(self, image=self.myimg, text="")
            # self.imgLabel.grid(row=0, column=0)

            ## Draw Table for processes
            
            ## Draw GANTT Chart

            
    

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
      
        self.title("CPU Scheduler Algorithm")
        self.geometry("1000x300")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        ## Welcome Label
        self.greet = customtkinter.CTkLabel(self, text="CPU Algorithm Simulator", fg_color="transparent", font=("Arial", 40))
        self.greet.grid(row=0, column=0, sticky="ew")

        # ## Member Names
        # ## Ivan
        # self.greet = customtkinter.CTkLabel(self, text="Galang, John Ivan", fg_color="transparent", font=("Arial", 20))
        # self.greet.grid(row=1, column=0, sticky="ew")
        # ## Michael
        # self.greet = customtkinter.CTkLabel(self, text="Ochengco, Michael Angelo", fg_color="transparent", font=("Arial", 20))
        # self.greet.grid(row=2, column=0, sticky="ew")
        # # Shawn
        # self.greet = customtkinter.CTkLabel(self, text="Sudaria, Shawn Michael", fg_color="transparent", font=("Arial", 20))
        # self.greet.grid(row=3, column=0, sticky="ew")

        ### OPTION MENU
        self.optionMenu = OptionWindow(self)
        self.optionMenu.grid(row=4, column=0, sticky="ew", columnspan=2, padx=50, pady=10)
        
        ### PLOT Window
        # self.plotWindow = PlotWindow(self)
        # self.plotWindow.grid(row=0, column=0, columnspan=2, sticky="nesw", padx=20, pady=20)

      

        
        

app = App()
app.mainloop()
