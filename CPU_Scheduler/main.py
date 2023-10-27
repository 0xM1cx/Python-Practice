import customtkinter
counter = 1

def click():
    global counter
    print(f"Count: {counter}")
    counter += 1

def main():
    app = customtkinter.CTk()
    app.geometry("1000x500")
    counter = 1
    button = customtkinter.CTkButton(app, text="Pisliti Ko", command=click)
    button.pack(padx=20, pady=20)


    app.mainloop()


if __name__ == "__main__":
    main()


