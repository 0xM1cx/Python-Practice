era = int(input("Enter Age: "))

print("Choices for Gender...\n [F] if Female\n [M] if Male")

gen = input("Enter Gender: ").casefold()

if era >= 18:
    if gen == "F":
        print("This user is an Adult Female")
    elif gen == "M":
        print("This use is an Adult Male")
    elif gen != "F" or gen != "M":
        print("This user is an adult LGBTQ")
   
elif era < 18:
    print("This user is a minor")

else: 
    print("Error")
