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
    n = int(input("Enter a positive integer or 0: "))
    while n < 0:
        n = int(input("Invalid. Enter a positive integer: "))

    if choice == "1":
        ans = factorial(n)
    elif choice == "2":
        ans = fibonacci(n)
    else:
        ans = "Invalid choice"

    print("\nFinal result:", ans)
