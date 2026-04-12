def calculate_power(x,y):
  return x**y

if_name_ =="main":
  x=int(input("enter the base: "))
  y=int(input("enter the exponent: "))
  
  result= calculate_power(x,y)
  print(f"{x} raised to the power of {y} is:{result}")
  

