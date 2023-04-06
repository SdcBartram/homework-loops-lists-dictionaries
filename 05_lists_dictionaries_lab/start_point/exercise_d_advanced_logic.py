# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)

# Alternative found --> 
# even_numbers = [num for num in numbers if num%2==0]
# print(even_numbers)

# 2. Print the difference between the largest and smallest value:
ordered_numbers = sorted(numbers)
# print(ordered_numbers)
difference_of_max_and_min_number = ordered_numbers[-1] - ordered_numbers[0]
print(difference_of_max_and_min_number)
# solution -->
largest = max(numbers)
smallest = min(numbers)

print(largest - smallest)


# 3. Print True if the list contains a 2 next to a 2 somewhere.
# # Not finished!
# Not correct yet ... type error
# result = True
# first_index = 0

# for num in numbers:
#     if num[0] == num[(first_index)-1]:
#         first_index =+1
#         print(result)

# solution -->
result = False
index = 0
for number in numbers:
    if (number == 2 and numbers[index-1] == 2):
        result = True
    index +=1
print(result)


# 4. Print the sum of the numbers, 
# # sum_numbers = sum(numbers)
# # print(sum_numbers)
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

#  solution --->
total = 0
found_6 = False
for number in numbers:
    if number == 6:
        found_6 = True
    elif found_6:
        if number == 7:
            found_6 = False
    else:
        total += number

print(total)

# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 
# solution -->
index = 0
total = 0
for number in numbers:
    if number == 13 or numbers[index-1] == 13:
        pass
    else:
     total += number
    index += 1
print(total)







