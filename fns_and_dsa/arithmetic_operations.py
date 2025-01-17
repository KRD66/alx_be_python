
def perform_operation(num1, num2, operation):
    
    #Perform basic arithmetic operations based on the operation parameter.#
    
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0: #Dividing by zero is not allowed!
          return "Error: Cannot divide by Zero"
        return num1/num2
    else:
        return "Error:Invalid operation"   
              
    