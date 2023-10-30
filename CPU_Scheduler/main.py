import customtkinter
import math

class PlotWindow(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.labs = customtkinter.CTkLabel(self, width=400, height=400)
        self.labs.grid(row=2, column=2)



class OptionWindow(customtkinter.CTkFrame):
    def __init__(self, master, ATwindow):
        super().__init__(master)



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
        self.AlgoChoice.grid(row=0, column=0)

        # Start Button
        self.start_Btn = customtkinter.CTkButton(self, text="Pagsugod", command=self.startExecution)
        self.start_Btn.grid(row=1, column=4, padx=10, pady=10)
        

    def setBT(self, value):
        self.BTSlider_CurValue.configure(text=math.trunc(value))
    
    
    def startExecution(self):
        pass
    

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("CPU Scheduler Algorithm")
        self.geometry("1000x500");
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        ## Check if mayda na TopLevelWindow
        self.ATwindow = None

        ### OPTION MENU
        self.optionMenu = OptionWindow(self, self.ATwindow)
        self.optionMenu.grid(row=1, column=0, sticky="ew", columnspan=2, padx=50, pady=10)
        
        ### PLOT Window
        self.plotWindow = PlotWindow(self)
        self.plotWindow.grid(row=0, column=0, columnspan=2, sticky="nesw", padx=10, pady=(0,10))
        

        





app = App()
app.mainloop()
