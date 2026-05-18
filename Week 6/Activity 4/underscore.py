# 1. Last Expression in Python
# In the interactive interpreter/REPL, _ stores the last evaluated result.
# In a script it just acts as a normal variable.
_ = 12 * 5
print("1. Last Expression:", _)

# 2. Ignoring Values
# Use _ when unpacking but you don't need some values
first_name, _, age = ("Alex", "Student", 42)
print("2. Ignoring Values:", first_name, age)

# 3. As a Loop Variable
# Use _ when you only care about looping, not the index value
total = 0
for _ in range(4):
    total += 15
print("3. Loop Variable:", total)

# 4. Formatting Large Numbers
# _ can be used as a separator in numbers for readability
population = 5_120_000
price = 1_999_99  # 1999.99 cents
print("4. Formatting Large Numbers:", population, price)

#5. Placeholder for temporary or unimportant variables
# Use _ as a placeholder for variables that are not important
first,_,last = [10,"20,30,40,50",80]
print("5. Placeholder:", first, last)
