def perform_operation(num1, num2, operation):
    match operation:
        case 'add':
            result = num1 + num2
        case 'subtract':
            result = num1 - num2
        case 'multiply':
            result = num1 * num2
        case 'divide':
            if num2 == 0:
                print("The divisor cann't be zero, ERROR!")
            else:
                result = num1 / num2
        case _:
            print("Not valid operation.")
    return result
