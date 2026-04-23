# Mathematical operations
class Calculator:
    
    # Methods
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a-b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b==0:
            return "cannot divided by zero"
        return a / b
    
# Functions
def display_menu():
    print("\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Exit")
   
def main():
    cal= Calculator()
    
    while True:
        display_menu()
        choice= input("enter your choice:")
        
        if choice=='5':
            print("existing calculator")
            
        try:
            num1= float(input("enter first number:"))
            num2= float(input("enter second number:"))
            
            if choice == '1':
                print("Result:",cal.add(num1,num2))
            elif choice == '2':
                print("Result:",cal.subtract(num1,num2))
            elif choice == '3':
                print("Result:",cal.multiply(num1,num2))
            elif choice == '4':
                print("Result:",cal.divide(num1,num2))
            else: 
                print("Invalid choice")
                
        except ValueError:
            print("please enter valid numbers")
            
main()            

