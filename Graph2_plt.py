import numpy as np
import matplotlib.pyplot as plt

subjects = ["French", "English", "Maths", "Science", "History"]
yr7scores = [76, 60, 80, 90, 65]
yr8scores = [92, 72, 85, 85, 80]
yr9scores = [95, 74, 88, 82, 85]

plt.plot(subjects, yr7scores, yr8scores, yr9scores)
plt.title("Sid's Exam Results")
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.show()
