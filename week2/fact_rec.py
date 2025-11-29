def factorial(n):

    if n == 0:
        return 1
    return n * factorial(n - 1)  


from functools import lru_cache

# cache results to avoid repeated calculations
@lru_cache(maxsize=None)
def fibonacci(n):
    # base case
    if n <= 1:
        return n
    # This will repeat calculations if just like this.
    return fibonacci(n - 1) + fibonacci(n - 2)
    # As calls reach base cases, results pop back up and combine.


if __name__ == "__main__":
    print("Choose an option:")
    print("1. Factorial")
    print("2. Fibonacci")

    choice = input("Enter choice (1/2): ")
    # need a parameter
    text = "Please enter an integer greater than or equal to 0: "
    n = input(text)
    text = "Invalid. " + text
    while type(n) is not int or n < 0:
        n = input(text)

    if choice == "1":
        ans = factorial(n)
    elif choice == "2":
        ans = fibonacci(n)
    else:
        ans = "Invalid choice"

    print("\nFinal result:", ans)
