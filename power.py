
def calculate_power(base,exponent):
    return base ** exponent

def main():
    print("power calculate program")
    
    base = float(input("enter the base: "))
    exponent = float(input("enter the exponent: "))
    
    result = calculate_power(base,exponent)
    print(f"{base} raised to the power of {exponent} is: {result}")
    if __name__ =="__main__":
        main()



