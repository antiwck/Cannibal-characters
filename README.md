# Cannibal-characters
Reducing the character from input

You are given an integer n and a string s of size n composed of lower case english letters.

You can perform the following operation on it:
1. In one operation, you have to choose any character in the string s, then delete the first character to the left of the chosen character that is equal to the chosen character (if there exists) and delete the first character to the right of the chosen character that is equal to the chosen character (if there exists). 
2. Note that in one operation, the length of the string s is reduced by a maximum of two characters.

Task:
1. You want to minimize the length of the string s.
2. Find the minimum number of operations that need to be performed to minimize the length of the string s.

Note:
Assume 1 based indexing.

Example
Assumptions :
n = 4
s = "abaa" (without quotes)

Approach:
1. Choose 3rd character in the string for 1st operation, this will delete the 1st character and 4th character in string s, the string becomes "ba".
2. The length of the string s can not be reduced further.
3. Hence, minimum number of operations needed to reduce the length of the string s to a minimum is 1.

Input format:
Note: This is the input format that you must use to provide custom input (available above the Compile and Test button).
1. The first line contains a single integer T, which denotes the number of test cases. T also specifies the number of times you have to run the Minimum_Operations function on a different set of inputs.
2. For each test case:
  i. First line contains an integer n.
  ii. Second line contains a string s.

Output format:
For each test case in a new line, print the minimum number of operations required to minimize the length of string s.
