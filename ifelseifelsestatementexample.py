# Calculate BMI
bmi = weight / (height ** 2)

# Classify BMI
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
elif 25 <= bmi < 29.9:
    category = "Overweight"
else:
    category = "Obese"

    # Display the result
print(f"Your BMI is {bmi:2f}, and you are classified as {category}.")