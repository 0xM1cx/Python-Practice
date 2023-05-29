import tkinter as tk
from tkinter import messagebox, ttk

class StudentEnrollmentGUI:
    
    
    
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x500") # gin change from 400x400 to 600x500
        self.root.title("Student Enrollment System") # amo la ghp
        
        self.txt_label = tk.Label(root, text="STUDENT REGISTRATION SYSTEM") #bag-o
        self.txt_label.config(font=("Courier", 20)) #bag-o
        self.txt_label.grid(row=0, column=1, padx=10, pady=10) #bag-o
        self.txt = tk.Text(root, height=5, width=52) #bag-o

        self.firstname_label = tk.Label(root, text="FirstName:")
        self.firstname_label.grid(row=2, column=0, padx=10, pady=10)
        self.firstname_entry = tk.Entry(root,width=30, font=("Arial",12),bg="gray")
        self.firstname_entry.grid(row=2, column=1, padx=10, pady=10,)
        
        
        self.lastname_label = tk.Label(root, text="LastName:")
        self.lastname_label.grid(row=3, column=0, padx=10, pady=10)
        self.lastname_entry = tk.Entry(root,width=30, font=("Arial",12),bg="gray")
        self.lastname_entry.grid(row=3, column=1, padx=10, pady=10)


        self.age_label = tk.Label(root, text="Age:")
        self.age_label.grid(row=4, column=0, padx=10, pady=10)
        self.age_entry = tk.Entry(root,width=30, font=("Arial",12),bg="gray")
        self.age_entry.grid(row=4, column=1, padx=10, pady=10)

        self.gender_label = tk.Label(root, text="School ID:")
        self.gender_label.grid(row=5, column=0, padx=10, pady=10)   
        self.gender_entry = tk.Entry(root,width=30, font=("Arial",12),bg="gray")
        self.gender_entry.grid(row=5, column=1, padx=10, pady=10)

        self.enroll_button = tk.Button(root, text="Add", command=self.add_student,bg="lightgreen",width=5,height=2)
        self.enroll_button.grid(row=6, columnspan=10, padx=5, pady=8,column=1)
    
        self.student_listbox = tk.Listbox(root,width=60,height=8)
        self.student_listbox.grid(row=10, columnspan=2, padx=10, pady=3)
        self.student_listbox.insert(1, "FirstName   LastName   Age   School ID")
        

        self.delete_button = tk.Button(root, text="Delete", command=self.delete_student,bg="pink",width=5,height=2)
        self.delete_button.grid(row=6, columnspan=9, padx=20, pady=20,column=0)
        
        
        self.student_listbox.bind("<Double-Button>", self.load_student)
    
        
        
    def add_student(self):
        firstname = self.firstname_entry.get()
        lastname = self.lastname_entry.get()
        age = self.age_entry.get()
        gender = self.gender_entry.get()

        if firstname and lastname and age and gender:
            student_info =  firstname,lastname,age,gender
            self.student_listbox.insert(tk.END, student_info)
            self.clear_entries()
        else:
            messagebox.showwarning("Incomplete Information", "Please enter all the fields.")

    def delete_student(self):
        selected_index = self.student_listbox.curselection()

        if selected_index:
                self.student_listbox.delete(selected_index)
        else:
            messagebox.showwarning("No Student Selected", "Please select a student to delete.")

    def load_student(self, event):
        selected_index = self.student_listbox.curselection()

        if selected_index:
            selected_student = self.student_listbox.get(selected_index)
            messagebox.showinfo("Selected Student", selected_student)

    def clear_entries(self):
        self.firstname_entry.delete(0, tk.END)
        self.lastname_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.gender_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentEnrollmentGUI(root)
    root.mainloop()

 