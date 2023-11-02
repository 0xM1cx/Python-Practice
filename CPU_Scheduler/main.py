import customtkinter, math, os
from NonPreemptivePriorityScheduling import _NonPreemptivePriorityScheduling
from CTkTable import *
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk



class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("1000x500")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        # self.fig, self.ax = plt.subplots()
        # self.table = self.ax.table(cellText=self.values, loc='center', cellLoc='center')
        # self.ax.axis("off")
        # self.table.auto_set_font_size(False)
        # self.table.set_fontsize(12)
        # self.table.scale(1, 1.5)
        # plt.savefig("output\Processtable.png")

        
        self.myimg = customtkinter.CTkImage(Image.open("table.png"), size=(400, 400))
        self.imgLabel = customtkinter.CTkLabel(self, image=self.myimg, text="")
        self.imgLabel.grid(row=0, column=0, sticky="nsew")

        self._myimg = customtkinter.CTkImage(Image.open("output/Processtable.png"), size=(400, 400))
        self._imgLabel = customtkinter.CTkLabel(self, image=self._myimg, text="")
        self._imgLabel.grid(row=0, column=1, sticky="nsew")


# class PlotWindow(customtkinter.CTkFrame):
#     def __init__(self, master):
#         super().__init__(master)

#         # self.add("GC")
#         # self.add("PT")
#         # self.set("PT")
        
#         # self.values = [
#         #     [1, 2, 3, 4],
#         #     [1, 2, 3, 4],
#         #     [1, 2, 3, 4],
#         #     [1, 2, 3, 4]
#         # ]
#     def DrawTable(self):
#         self._myimg = customtkinter.CTkImage(Image.open("output/Processtable.png"), size=(400, 400))
#         self._imgLabel = customtkinter.CTkLabel(self, image=self._myimg, text="")
#         self._imgLabel.grid(row=0, column=0, columnspan=1, sticky="nesw", padx=5, pady=5)
# #         # self.fig, self.ax = plt.subplots()
# #         # self.table = self.ax.table(cellText=self.values, loc='center', cellLoc='center')
# #         # self.ax.axis("off")
# #         # self.table.auto_set_font_size(False)
# #         # self.table.set_fontsize(12)
# #         # self.table.scale(1, 1.5)
# #         # plt.savefig("output\Processtable.png")

# #         self.myimg = customtkinter.CTkImage(light_image=Image.open("table.png"))
# #         self.imgLabel = customtkinter.CTkLabel(self, image=self.myimg, text="")
# #         self.imgLabel.grid(row=0, column=0)


        
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
        command=self.setAlgo, width=250)
        self.AlgoMenu.grid(row=1, column=3)

        # Start Button
        self.start_Btn = customtkinter.CTkButton(self, text="Pagsugod", command=self.startExecution)
        self.start_Btn.grid(row=1, column=4, padx=10, pady=10)
        

    def setBT(self, value):
        self.BTSlider_CurValue.configure(text=math.trunc(value))
    
    def setAlgo(self, choice):
        return choice
    
    def startExecution(self):
        
        if self.AlgoMenu.get() == "Preemptive Priority Scheduling":
            print("This is Preemptive Priority Scheduling")
        elif self.AlgoMenu.get() == "Non-Preemtive Priotity Scheduling":
             
            self.toplev = ToplevelWindow(self)
            # self.processList = self.NonPPS_Instance.Random_Input(int(self.Process_Input.get()), math.trunc(self.Burst_Time.get()))
            # self.Plot_Window.DrawTable(int(self.Process_Input.get()))
            # self.TopWin = ToplevelWindow(self)
            # self.myimg = customtkinter.CTkImage(light_image=Image.open("table.png"), size=(100,100))
            # self.imgLabel = customtkinter.CTkLabel(self, image=self.myimg, text="")
            # self.imgLabel.grid(row=0, column=0)
            
    

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
      
        self.title("CPU Scheduler Algorithm")
        self.geometry("1000x500");
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        ### OPTION MENU
        self.optionMenu = OptionWindow(self)
        self.optionMenu.grid(row=1, column=0, sticky="ew", columnspan=2, padx=50, pady=10)
        
        ### PLOT Window
        # self.plotWindow = PlotWindow(self)
        # self.plotWindow.grid(row=0, column=0, columnspan=2, sticky="nesw", padx=20, pady=20)

      

        
        

app = App()
app.mainloop()
