def calculate_factorial(n):
    # This function has some issues for demonstration
    result = 1
    for i in range(n):  # Bug: should be range(1, n+1)
        result = result * i
    return result

# Inefficient fibonacci implementation
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)  # Very inefficient for large n

# Missing error handling
def divide_numbers(a, b):
    return a / b  # No check for division by zero

print(calculate_factorial(5))
print(fibonacci(10))
print(divide_numbers(10, 0))  # This will crash