import numpy as np
import matplotlib.pyplot as plt

subjects = ["French", "English", "Maths", "Science", "History"]
yr7scores = [76, 60, 80, 90, 65]
yr8scores = [92, 72, 85, 85, 80]

plt.plot(subjects, yr7scores, label = "Year 7 scores", marker = 'o', markerfacecolor = 'green')
plt.plot(subjects, yr8scores, label = "Year 8 scores", marker = 'o', markerfacecolor = 'green')
plt.title("Sid's Exam Results")
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.show()
