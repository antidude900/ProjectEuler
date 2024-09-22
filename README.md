# Project Euler Solutions in Python

Welcome to my collection of solutions for [Project Euler](https://projecteuler.net/) problems, implemented in Python.


## About

This repository contains Python solutions to various problems from Project Euler. Each solution is crafted to be efficient and pass all the test cases in HackerRank.


## Structure

Each solution is saved as a separate Python file, named according to the problem number (e.g., `Problem1.py` for problem 1). The code is well explained with comments providing mathematical theory, thought process and examples.


## Project Euler

Project Euler is a series of challenging mathematical and computational problems that require creative and optimized solutions. The problems can range from simple arithmetic to complex mathematical theory. 

![image](https://github.com/user-attachments/assets/14ae4943-445e-4e90-b650-99253c35fa70)


## HackerRank

HackerRank offers multiple test cases for each problem, allowing you to identify flaws in your code and optimize it for better performance.

![image](https://github.com/user-attachments/assets/88f68ad8-1589-427f-8589-b8af6f4e9af4)

### About Its Environment

![image](https://github.com/user-attachments/assets/2c832c77-7410-49b1-b6a9-29dba6834632)

The Left Side of the Environment provides the details related to the problem. For eg: Problem Statement, Input Format, Constraints, Output Format.
The Right Side of the Environment provides the coding editor to code and submit the code.

### Input Format

![image](https://github.com/user-attachments/assets/14015c22-d93b-4a39-9acd-24a9c45fbd99)

The First Line contains the no of test cases say "N".
After that, there are "N" Lines each containing the input for each test case.
For eg: In the figure above, the first line contains 2 meaning there are 2 test cases. After that, the second line has "10" which means the input of the first test case is 10 and the second line has "100" which means the input of the second test case is 100.

### Reading the Input
![image](https://github.com/user-attachments/assets/eb0dcf13-e12d-44be-adc9-bbba45555504)

The first line is irrelevant(relevant when importing one python file in another python file) in the present context and the code still works if it is removed. 
The second line first removes leading and trailing whitespace from the input to maintain the format of the input and then stores it in in variable "t".
Thus "t" contains the no of test cases.
The third line runs a loop of range "t" to read all the test cases.
The fourth line which is inside the loop reads the value of the test case, strips it and stores in "n".
We can then pass n as argument to the function which then returns the required answer and then we print it.
(Note: This is only the default way how the input is read in the code. You can write your own custom way to read the input which you will be experience the first time in Problem 10)





