import pandas as pd
import matplotlib.pyplot as plt

students = ["Shawn", "Abby", "Patricia"]
data = [
    ["Shun", 19, "Filipino"],
    ["Jason", 20, "American"],
    ["Zyra", 20, "Filipino"]
]

ser = pd.Series(students)
df = pd.DataFrame(data, columns=["Name", "Age", "Nationality"])

x_data = ["Shawn", "Abby", "James", "Patricia"]
y_data = [90, 100, 89, 94]


plt.plot(x_data, y_data)
plt.show()
