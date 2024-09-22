# Project Euler Solutions in Python

Welcome to my collection of solutions for [Project Euler](https://projecteuler.net/) problems, implemented in Python. This repository aims to provide efficient solutions and insights into the mathematical concepts behind each problem.


## Table of Contents

- [About](#about)
- [Structure](#structure)
- [Project Euler](#project-euler)
- [HackerRank](#hackerrank)
  - [Environment Overview](#hackerrank-environment-overview)
  - [Input Format](#input-format)
  - [Reading the Input](#reading-the-input)
- [Acknowledgments](#acknowledgments)


## About

This repository contains Python solutions to various Project Euler problems. Each solution is designed for efficiency and passes all test cases provided by [HackerRank](https://www.hackerrank.com/).


## Structure

Each solution is saved as a separate Python file, named according to the problem number (e.g., `Problem1.py` for Problem 1). The code is well-commented, explaining the mathematical theory, thought process, and example inputs.


## Project Euler

Project Euler is a series of challenging mathematical and computational problems that require creative, optimized solutions. The problems range from simple arithmetic to complex mathematical theories.

![Project Euler](https://github.com/user-attachments/assets/14ae4943-445e-4e90-b650-99253c35fa70)


## HackerRank

HackerRank provides multiple test cases for each problem, allowing you to identify flaws in your code and optimize performance.

![HackerRank](https://github.com/user-attachments/assets/88f68ad8-1589-427f-8589-b8af6f4e9af4)


### HackerRank Environment Overview

![image](https://github.com/user-attachments/assets/263c3130-b6ae-496b-a9a6-13cf62fa8347)

- **Left Panel**: Displays the problem statement, input format, constraints, and output format.

- **Right Panel**: The coding editor, where you can write and submit your solution.


### Input Format

![Input Format](https://github.com/user-attachments/assets/14015c22-d93b-4a39-9acd-24a9c45fbd99)

The input format is as follows:

1. The first line contains the number of test cases, denoted as `N`.
2. Each of the next `N` lines contains input for a test case.

For example, in the image above:
- The first line (`2`) indicates that there are two test cases.
- The second line contains `10`, which is the input for the first test case.
- The third line contains `100`, which is the input for the second test case.


### Reading the Input

![Reading the Input](https://github.com/user-attachments/assets/eb0dcf13-e12d-44be-adc9-bbba45555504)

The input reading process is as follows:

- The first line is often irrelevant when not importing one Python file into another and can be ignored.

- The second line removes leading and trailing whitespaces and stores the number of test cases in the variable `t`.

- The code then runs a loop `t` times to process each test case.

Within the loop:
- Each test case value is read, stripped, and stored in `n`.
- The function is called with `n`, returning the solution, which is printed.

(Note: You can customize how input is handled. For example, Problem 10 offers a different input format.)


## Acknowledgments

I hope this repository helps you in solving Project Euler problems. If you find it helpful, please ⭐ star this repository!
