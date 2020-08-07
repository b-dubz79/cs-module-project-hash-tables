# Add up and print the sum of the all of the minimum elements of each inner array:
# [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
# The expected output is given by:
# 4 + -1 + 9 + -56 + 201 + 18 = 175
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

# set list to variable name
nums = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
# use a for loop for outter list
new_arr = []
for i in nums:
    minimum = 10000
    for j in i:
        if j < minimum:
            minimum = j
    new_arr.append(minimum)
        
            
    



        

# use inner loop to compare values at outer loops i index
# create new array based on minimum values
# sum minimum values

