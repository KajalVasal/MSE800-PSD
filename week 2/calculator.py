# Mathematical Operations
a = complex(input("enter a complex number:"))
b = complex(input("enter another complex number:"))

def calculator_basic(a, b, op):
    
    if op == '+':
        return a + b
    elif op =='-':
        return a - b
    elif op == '*':
        return a * b
    
    else:
        return "Not support operator"
    
def main():
    print(f"{a} + {b} = {calculator_basic(a, b, '+')}")
    print(f"{a} - {b} = {calculator_basic(a, b, '-')}")
    print(f"{a} * {b} = {calculator_basic(a, b, '*')}")
    
if __name__ == "__main__":
    main()
     