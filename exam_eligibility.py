no_of_classes = [2, 3, 5, 2, 6, 5, 3, 4]
no_attended = [2, 2, 3, 1, 5, 4, 3, 2]

for i in range(len(no_of_classes)):
    print(f"Attendance for the day: {no_attended[i]}/{no_of_classes[i]}")

percent_attendance = (sum(no_attended)/sum(no_of_classes))*100

print("\nFinal Attendance:")
if (percent_attendance >= 75):
    print(
        f"Student is eligible for exam with {percent_attendance}% attendance")
else:
    print(
        f"Student is not eligible for exam with {percent_attendance}% attendance")