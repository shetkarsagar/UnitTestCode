import pytest
from app import (
    add, subtract, multiply, safe_divide, read_file_safe, 
    insecure_eval, get_db_password, run_system_command, error_prone_function
)

###   Test Cases for Good Functions ###
def test_add():
    assert add(3, 2) == 5  #   Correct

def test_subtract():
    assert subtract(10, 3) == 7  #   Correct

def test_multiply():
    assert multiply(4, 5) == 20  #   Correct

def test_safe_divide():
    assert safe_divide(10, 2) == 5  #   Correct
    with pytest.raises(ValueError):  
        safe_divide(10, 0)  #   Expected failure

def test_read_file_safe():
    with pytest.raises(ValueError):
        read_file_safe("../etc/passwd")  # Prevents directory traversal

###  Test Cases for Bad Functions ###
def test_insecure_eval():
    assert insecure_eval("2 + 2") == 4  #  Dangerous function

def test_hardcoded_password():
    assert get_db_password() == "password123"  #   Hardcoded password should be avoided

def test_command_injection():
    result = run_system_command("echo Hello")
    assert result is not None  #   Test allows unsafe command execution

def test_error_handling():
    assert error_prone_function() is None  #   Poor error handling should be flagged
