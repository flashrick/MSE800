"""
Author: Wade Wang
Date: 30/11/2025
"""

from functools import lru_cache

# calculate factorial and fibonacci series.
class MathClass:
    def __init__(self):
        # get the calculation type and the number
        print("Choose an option:")
        print("1. Factorial")
        print("2. Fibonacci Serires")

        choice = input("Enter choice (1/2): ")
        # need a parameter
        text = "Please enter an integer greater than or equal to 0: "
        # get the number
        n = input(text)
        # set the invalid text
        text = "Invalid. " + text
        # verify the invalid number
        while n.isdigit() is False or int(n) < 0:
            n = input(text)
        # convert str to int
        n = int(n)
        # users choose the type
        if choice == "1":
            ans = self.factorial(n)
        elif choice == "2":
            ans = self.fibonacci(n)
        else:
            ans = "Invalid choice"

        # print the answer
        print("\nFinal result:", ans)

    # calculate the factorial
    def factorial(self, n):
        # the base case
        if n == 0:
            return 1
        # calculate using recursion
        return n * self.factorial(n - 1)



    # cache results to avoid repeated calculations
    def fibonacci(self, n):
        # cache the function results for identical parameters
        @lru_cache(maxsize=None)
        def fib(m):
            # stopping conditions
            if m <= 1:
                return m

            # Fibonacci series shows as F(n) = F(n-1) + F(n-2), use recursive function.
            return fib(m - 1) + fib(m - 2)

        return [fib(i) for i in range(n)]


obj = MathClass()
