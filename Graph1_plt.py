import numpy as np
import matplotlib.pyplot as plt

x = ["French", "English", "Maths", "Science", "Music"]
y = [93, 72, 90, 85, 86]

plt.bar(x, y)
plt.title("Sid's Exam Results")
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.legend()
plt.show()