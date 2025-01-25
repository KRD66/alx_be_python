def safe_divide(numerator, denominator):

    try:
        numerator = float(numerator)
        denominator = float(denominator)
        if denominator == 0:
            return ZeroDivisionError("Error: Cannot divide by zero.")
        else:
            return f"The result of the division is {numerator / denominator}"

    except ValueError:
<<<<<<< HEAD
        return "Error: Please enter numeric values only."
=======
        return "Error: Please enter numeric values only."
>>>>>>> 0fc109382dfa912d4c9cf327941a8e06bca923be
