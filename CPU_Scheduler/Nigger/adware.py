import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("CPU Scheduler Algorithm")
        self.geometry("1000x300")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.greet = customtkinter.CTkLabel(self, text="PUTANG INA", fg_color="transparent", font=("Arial", 100))
        self.greet.grid(row=0, column=0, sticky="ew")
        

while True:
    app = App()
    app.mainloop()