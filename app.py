import os
import subprocess

###  Good Functions (Best Practices) ###

def add(a, b):
    """Adds two numbers and returns the result."""
    return a + b  #  Correct and safe

def subtract(a, b):
    """Subtracts two numbers and returns the result."""
    return a - b  #  Correct and safe

def multiply(a, b):
    """Multiplies two numbers."""
    return a * b  #  Correct and safe

def safe_divide(a, b):
    """Safely divides two numbers, handling zero division."""
    if b == 0:
        raise ValueError("Cannot divide by zero")  #  Exception handling
    return a / b

def read_file_safe(filename):
    """Safely reads a file and prevents path traversal."""
    if ".." in filename or filename.startswith("/"):
        raise ValueError("Invalid file path!")  #  Prevents directory traversal
    with open(filename, "r") as file:
        return file.read()

###  Vulnerable / Bad Practice Functions ###
# Insecure function: Uses eval() leading to command injection
def insecure_eval(user_input):
    return eval(user_input)  #  HIGH-RISK: Arbitrary code execution

# Hardcoded credentials (Security issue)
def get_db_password():
    return "password123"  # Hardcoded credentials

# OS Command Injection
def run_system_command(command):
    return subprocess.Popen(command, shell=True)  # Security Risk: Shell Injection

# Function with poor error handling
def error_prone_function():
    try:
        return 10 / 0  # Will cause ZeroDivisionError
    except:
        pass  # Silent exception handling (Bad Practice)
