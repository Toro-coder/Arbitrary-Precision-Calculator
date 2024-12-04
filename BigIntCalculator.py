# this is a calculator with add, subtract, multiply, divide, logarithm, Square root and we can do base_conversion.
# this calculator does not use native support and is for very large numbers
# creating a class for easy management of the fuctionalities
class Calculator:
    # Addition
    def add(self, num1, num2):
        # here you add large integer numbers which are represented as strings
        result = [] # this is a list storing result digits
        carry = 0 # holds an overflow value from addition of the two digits
        num1, num2 = num1[::-1], num2[::-1] #makes the string to start addition from the least significant digit

        # loop through the longer number
        for i in range(max(len(num1), len(num2))):
            # get digit or  0 if out of range
            digit1 = int(num1[i]) if i < len(num1) else 0
            digit2 = int(num2[i]) if i < len(num2) else 0
            # addition the digits with the carry
            addition = digit1 + digit2 + carry
            #update carry and the current digit
            carry, digit =divmod(addition, 10)
            # appending the current digit to the result
            result.append(str(digit))

        # append a carry if it remains
        if carry:
            result.append(str(carry))

        # reverse the result to get the correct order
        return "".join(result[::-1])

    #Subtraction
    def subtract(self, num1, num2):
        # here we subtract the second number from the first number with the assumption of first number is greater than second
        result = []
        borrow = 0 # here we borrow instead of carrying on
        num1, num2 = num1[::-1], num2[::-1] # reversing the digits

        # we loop through
        for i in range(len(num1)):
            digit1 = int(num1[i])
            digit2 = int(num2[i]) if i < len(num2) else 0
            difference = digit1-digit2-borrow
            if difference < 0:
                difference += 10
                borrow = 1
            else:
                borrow = 0
            result.append(str(difference))

        while len(result) > 1 and result[-1] == '0': #removal of trailing zeros
            result.pop()
        return "".join(result[::-1])

    #Multiplication
    def multiply(self, num1, num2):
        num1, num2 = num1[::-1], num2[::-1]
        result = [0]*(len(num1)+ len(num2))
        # here we have a nested loop for multiplication
        for i in range(len(num1)):
            for j in range(len(num2)):
                result[i+j] += int(num1[i]) * int(num2[j])
                result[i+j+1] += result[i+j] // 10 #this is when we have a carry
                result[i+j] %= 10

        while len(result) > 1 and result[-1] == 0:
            result.pop() # removing the trailing zeros
        return "".join(map(str, result[::-1]))

    #Division
    def division(self, num1, num2):
        quotient = []
        remainder = 0
        num2 = int(num2)
        # check if the divisor is zero hence raising an error
        if num2 == 0:
            raise ZeroDivisionError("cannot divide by zero")
        for digit in num1:
            remainder = remainder * 10 + int(digit)
            quotient.append(str(remainder//num2))
            remainder %= num2
        while len(quotient) > 1 and quotient[0] == '0':
            quotient.pop(0)
        return "".join(quotient)

    # Modulo
    def modulus(self,num1, num2):
        remainder = 0
        num2 = int(num2)
        if num2 == 0:
            raise ZeroDivisionError("Cannot take modulus by zero")
        for digit in num1:
            remainder = (remainder * 10 + int(digit)) % num2
        return str(remainder)

    # Exponential
    def power(self, base, exponent):
        result = "1"
        for _ in range(int(exponent)):
            result = self.multiply(result, base)
        return result

    # Factorial
    def factorial(self, num):
        result = "1"
        for j in range(2, int(num) + 1):
            result = self. multiply(result, str(j))
        return result

    # manually base conversion
    def base_converter(self, num, from_base, to_base):
        # here we coverting num from_base to decimal
        decimal_value = 0
        for digit in num:
            decimal_value = decimal_value * from_base + int(digit, base=from_base)
        # here we are coverting from decimal to_base
        result = []
        while decimal_value > 0:
            result.append(str(decimal_value % to_base))
            decimal_value //= to_base
        return "".join(result[::-1]) if result else "0"

    # Logarithm
    def log(self, num, base):
        num = int(num)
        base = int(base)
        if num <= 0 or base <= 1:
            raise ValueError("Logarithm input must be positive and base > 1")
        result = 0
        value = 1
        while value < num:
            value *= base
            result += 1
        return str(result - 1 if value > num else result)

    # Square root
    def root(self, num, n=2):
        num = int(num)
        n = int(n)
        if num < 0 and n % 2 == 0:
            raise ValueError("Cannot compute even root of a negative number")
        low, high = 0, num
        while low <= high:
            mid = (low + high) // 2
            if self.power(str(mid), str(n)) == str(num):
                return str(mid)
            elif int(self.power(str(mid), str(n))) < num:
                low = mid + 1
            else:
                high = mid - 1
        return str(high)

# REPL
def repl():
    calc = Calculator()
    print("Welcome to the Arbitrary-Precision Integer Calculator (No Native Support)")
    print("Supported commands: add, subtract, multiply, divide, modulus, power, factorial, base_convert, logarithm, root")
    print("Type 'exit' to quit.")
    while True:
        command = input("Enter command: ").strip().lower()
        if command == 'exit':
            break
        try:
            if command == 'add':
                a = input("Enter first number: ")
                b = input("Enter second number: ")
                print("Result:", calc.add(a, b))
            elif command == 'subtract':
                a = input("Enter first number: ")
                b = input("Enter second number: ")
                print("Result:", calc.subtract(a, b))
            elif command == 'multiply':
                a = input("Enter first number: ")
                b = input("Enter second number: ")
                print("Result:", calc.multiply(a, b))
            elif command == 'division':
                a = input("Enter first number: ")
                b = input("Enter second number: ")
                print("Result:", calc.division(a, b))
            elif command == 'modulus':
                a = input("Enter first number: ")
                b = input("Enter second number: ")
                print("Result:", calc.modulus(a, b))
            elif command == 'power':
                a = input("Enter base: ")
                b = input("Enter exponent: ")
                print("Result:", calc.power(a, b))
            elif command == 'factorial':
                a = input("Enter number: ")
                print("Result:", calc.factorial(a))
            elif command == 'base_converter':
                num = input("Enter number: ")
                from_base = int(input("Enter source base: "))
                to_base = int(input("Enter target base: "))
                print("Result:", calc.base_converter(num, from_base, to_base))
            elif command == 'log':
                a = input("Enter number: ")
                b = input("Enter base: ")
                print("Result:", calc.log(a, b))
            elif command == 'root':
                a = input("Enter number: ")
                n = input("Enter root degree (default is 2): ") or "2"
                print("Result:", calc.root(a, n))
            else:
                print("Unknown command. Try again.")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    repl()
