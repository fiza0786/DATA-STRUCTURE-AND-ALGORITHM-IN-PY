# Push Zeros to end

# You have been given a random integer array/list(ARR) of size N. You have been required to push all the zeros that are present in the array/list to the end of it. Also, make sure to maintain the relative order of the non-zero elements.
# Note:
# Change in the input array/list itself. You don't need to return or print the elements.

# You need to do this in one scan of array only. Don't use extra space.


# Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

# First line of each test case or query contains an integer 'N' representing the size of the array/list.

# Second line contains 'N' single space separated integers representing the elements in the array/list.
# Output Format :
# For each test case, print the elements of the array/list in the desired order separated by a single space.

# Output for every test case will be printed in a separate line.
# Constraints :
# 1 <= t <= 10^2
# 0 <= N <= 10^5
# Time Limit: 1 sec
# Sample Input 1:
# 1
# 7
# 2 0 0 1 3 0 0
# Sample Output 1:
# 2 1 3 0 0 0 0
#  Explanation for the Sample Input 1 :
# All the zeros have been pushed towards the end of the array/list. Another important fact is that the order of the non-zero elements have been maintained as they appear in the input array/list.
# Sample Input 2:
# 2
# 5
# 0 3 0 2 0
# 4
# 9 0 0 8 2
# Sample Output 2:
# 3 2 0 0 0
# 9 8 2 0 0


 ....................................................................................................................................................................
 CODE
 
 
 
 def PushZerostoend(arr):
    nonzero = 0
    for i in range(len(arr)):
      if(arr[i]!=0):
        swap(arr[i],arr[nonzero])
        nonzero+=1  
    return arr
  
  
 
 
 
 
