def safe_divide(numerator, denominator):
    
    try :
        numerator = float(numerator)
        denominator = float(denominator)
        result = denominator / denominator
        return f"The result of division is {result}"

    except ValueError:
        return "Error: Please enter numeric values only."

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
       