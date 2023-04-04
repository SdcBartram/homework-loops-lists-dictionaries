# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)

# 2. Print the difference between the largest and smallest value:
ordered_numbers = sorted(numbers)
# print(ordered_numbers)
difference_of_max_and_min_number = ordered_numbers[-1] - ordered_numbers[0]
print(difference_of_max_and_min_number)


# 3. Print True if the list contains a 2 next to a 2 somewhere.


# 4. Print the sum of the numbers, 
# # sum_numbers = sum(numbers)
# # print(sum_numbers)
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 







