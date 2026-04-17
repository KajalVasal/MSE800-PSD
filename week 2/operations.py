def calculate_basic(a, b, c):
    
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '*':
        return a * b
    
    else:
        return "Not support operator"


def main():
    c1 = complex(6, 3) # 6 + 3j
    c2 = complex(2, 1) # 2 + 1j
    print(f"{c1} + {c2} = {calculate_basic(c1, c2, '+')}")
    print(f"{c1} - {c2} = {calculate_basic(c1, c2, '-')}")
    print(f"{c1} * {c2} = {calculate_basic(c1, c2, '*')}")
 

if __name__ == "__main__":
    main()
