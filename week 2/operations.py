# Mathematical operations
a = complex(input("enter first complex number:"))
b = complex(input("enter second complex number:"))

def calculate_basic(a, b, op):
    
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    
    else:
        return "Not support operator"


def main():
    
    print(f"{a} + {b} = {calculate_basic(a, b, '+')}")
    print(f"{a} - {b} = {calculate_basic(a, b, '-')}")
    print(f"{a} * {b} = {calculate_basic(a, b, '*')}")
 
if __name__ == "__main__":
    main()
