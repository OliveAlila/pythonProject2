# arithmetic operators,assignment operator,logical operators,comparison operators


num = 43  # first operand
num2 = 12  # second operand

print(f"The sum of {num} and {num2} is {num + num2}")
print(f"The difference of {num} and {num2} is {num - num2}")
print(f"The division of {num} and {num2} is {num / num2}")
print(f"The multiplication of {num} and {num2} is {num * num2}")
print(f"The remainder of {num} and {num2} is {num % num2}")
print(f"The exponent of {num} and {num2} is {num ** num2}")
print(f"The floor of {num} and {num2} is {num // num2}")

num3 = 56
num4 = 23

# comparison operators

print(f"{num3} and {num4} are equal {num3 == num4}")
print(f"{num3} and {num4} are not equal {num3 != num4}")
print(f"{num3} is greater than or equals to {num4} {num3 >= num4}")
print(f"{num3} is less than than or equals to {num4} {num3 <= num4}")

# assignment operators
num5 = 27
num6 = 8
print(f"num5=num6:{num5 == num6}")
print(f"num5-=num6:{num5 - num6}")
print(f"num5*=num6:{num5 * num6}")
print(f"nm5+=num6 {num5 + num6}")

# logical operators

num7 = 10
print(f"One statement is true {num7 >= 15 or num7 < 12}")
print(f"One statement is true {15 <= num7 < 12}")
