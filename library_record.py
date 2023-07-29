import numpy.random as ran

TotalBooks = 100
borrowedBooks = 20
no_of_renewals = ran.randint(0, 5, borrowedBooks)
print(no_of_renewals)

print(f"{borrowedBooks} Books are borrowed out of {TotalBooks} \n")
for i in range(borrowedBooks):
    print(f"Book {i+1} has '{no_of_renewals[i]}' no of renewals")

print(f"Total No of borrows are: {sum(no_of_renewals)}")

#preceision