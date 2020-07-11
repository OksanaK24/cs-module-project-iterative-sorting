# Add up and print the sum of the all of the minimum elements of each inner array:
# [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
# The expected output is given by:
# 4 + -1 + 9 + -56 + 201 + 18 = 175
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

arr = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]

final_sum = 0

for i in arr: 
    final_sum += min(i) 

print(final_sum)

# STRETCH:
# Add up and print the sum of the all of the minimum elements of each inner array. Each array may contain additional arrays nested arbitrarily deep, in which case the minimum value for the nested array should be added to the total.
# [
#   [8, [4]], 
#   [[90, 91], -1, 3], 
#   [9, 62], 
#   [[-7, -1, [-56, [-6]]]], 
#   [201], 
#   [[76, 0], 18],
# ]
# The expected output for the above input is:
# 8 + 4 + 90 + -1 + 9 + -7 + -56 + -6 + 201 + 0 + 18 = 260
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

# new_arr = [
#   [8, [4]], 
#   [[90, 91], -1, 3], 
#   [9, 62], 
#   [[-7, -1, [-56, [-6]]]], 
#   [201], 
#   [[76, 0], 18],
# ]

# new_final_sum = 0

# def counting(arr):
#     for i in arr:
#         for j in range(len(i)):
#             if type(j) == list:
#                 return counting(i)
#         global new_final_sum
#         new_final_sum += min(i)

# print(counting(new_arr))