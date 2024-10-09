import tkinter as tk
import math
import random

def is_prime_trial_division(num):
    """Checks primality using trial division (O(sqrt(n)))

    Time Complexity: O(sqrt(n)) in the worst case, where n has small prime factors. In the average case, it's closer to O(log log n).
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def is_prime_fermat(num):
    """Checks primality using Fermat's Little Theorem (O(log n))

    Time Complexity: O(log n) due to the repeated modular exponentiation.
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    a = 2
    while a < num:
        if pow(a, num - 1, num) != 1:
            return False
        a += 1
    return True

def is_prime_miller_rabin(num):
    """Checks primality using the Miller-Rabin test (O(k * log n))

    Time Complexity: O(k * log n), where k is the number of iterations (typically 10-12 for good accuracy).
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0:
        return False
    r, d = 0, num - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    for _ in range(10):  # Adjust the number of iterations for desired accuracy
        a = random.randint(2, num - 2)
        x = pow(a, d, num)
        if x == 1 or x == num - 1:
            continue
        for _ in range(r - 1):
            x = (x * x) % num
            if x == num - 1:
                break
        else:
            return False
    return True

def strassen(n):
    """Checks primality using the AKS primality test (O(((log n)^6))

    Time Complexity: O(((log n)^6)) in the worst case, but generally considered impractical for large numbers.
    """
    # Implementation omitted due to complexity (refer to external resources)
    """Checks primality using the Solovay-Strassen test.

    Args:
        n: The number to check for primality.

    Returns:
        True if n is probably prime, False otherwise.
    """

    if n <= 1:
        return False
    if n <= 3:
        return True

    # Ensure n is odd
    if n % 2 == 0:
        return False

    # Perform multiple iterations for increased accuracy
    for _ in range(10):
        a = random.randint(2, n - 2)
        if not is_quadratic_residue(a, n):
            return False

    return True

def is_quadratic_residue(a, n):
    """Checks if a is a quadratic residue modulo n.

    Args:
        a: The number to check.
        n: The modulus.

    Returns:
        True if a is a quadratic residue modulo n, False otherwise.
    """

    if n == 2:
        return a % 2 == 0
    elif n % 8 == 3 or n % 8 == 7:
        return pow(a, (n - 1) // 2, n) == 1
    else:
        return pow(a, (n - 1) // 2, n) in (1, n - 1)


def check_primality(num, method):
    """Checks primality using the specified method."""
    if method == "Trial Division":
        return is_prime_trial_division(num)
    elif method == "Fermat's Little Theorem":
        return is_prime_fermat(num)
    elif method == "Miller-Rabin Test":
        return is_prime_miller_rabin(num)
    elif method == "Solovay Strassen":
        return strassen(num)  # Note: Implementation not provided
    else:
        return False

def check_button_click():
    """Handles button click event and displays primality result with time complexity."""
    try:
        num = int(num_entry.get())
        method = method_var.get()
        result = check_primality(num, method)
        time_complexity = {
            "Trial Division": "O(sqrt(n))",
            "Fermat's Little Theorem": "O(log n)",
            "Miller-Rabin Test": "O(k * log n)",
            "Solovay Strassen": "O(n^(1/2 + e))"
        }.get(method, "N/A")  # Handle missing time complexity information
        result_label.config(text=f"Result: {'Prime' if result else 'Composite'}")
        time_complexity_label.config(text=f"Time Complexity: {time_complexity}")
    except ValueError:
        result_label.config(text="Invalid input: Please enter an integer.")

# Create the main window
window = tk.Tk()
window.title("Primality Testing")
window.geometry("400x350")  # Set window size for better visibility

# Configure grid layout for centered alignment
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=1)

# Create input labels and entry fields
num_label = tk.Label(window, text="Number:")
num_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
num_entry = tk.Entry(window)
num_entry.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

# Create method selection
method_var = tk.StringVar(value="Trial Division")
method_label = tk.Label(window, text="Method:")
method_label.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
method_menu = tk.OptionMenu(window, method_var, "Trial Division", "Fermat's Little Theorem", "Miller-Rabin Test", "Solovay Strassen")
method_menu.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

# Create the check button
check_button = tk.Button(window, text="Check", command=check_button_click)
check_button.grid(row=2, columnspan=2, padx=10, pady=10, sticky="nsew")

# Create the result label
result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.grid(row=3, columnspan=2, padx=10, pady=10, sticky="nsew")

# Create the time complexity label
time_complexity_label = tk.Label(window, text="", font=("Arial", 12))
time_complexity_label.grid(row=4, columnspan=2, padx=10, pady=10, sticky="nsew")

# Start the main loop
window.mainloop()
