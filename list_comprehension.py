#  Using a for loop
addition = []

for index in range(10):
    addition.append(index + index)

addition = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


# Now using list comprehension
addition = [index + index for index in range(10)]

addition [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
