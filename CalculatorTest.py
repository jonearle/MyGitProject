def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def test_calculator():
    assert add(2, 3) == 5, "Addition failed"
    assert add(0, 0) == 0, "Addition with zeros failed"

    assert subtract(5, 3) == 2, "Subtraction failed"
    assert subtract(0, 3) == -3, "Subtraction with negative result failed"

    assert multiply(4, 3) == 12, "Multiplication failed"
    assert multiply(0, 5) == 0, "Multiplication with zero failed"

    assert divide(10, 2) == 5, "Division failed"
    assert divide(9, 3) == 3, "Division failed"

    try:
        assert divide(10, 2) == 5, "Division failed"
        divide(5, 0)
    except ZeroDivisionError:
        print("Division by zero raised an exception")
    else:
        assert False, "Division by zero did not raise an exception"

    print("All tests passed successfully")

