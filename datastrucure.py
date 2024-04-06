# list datastructure
# list are mutable/changeable

my_list = ["Banana", "Mangoes", "Oranges", "Apples", "Watermelon"]

my_list.sort()
print(my_list)

my_list[1] = 'Pineapple'
print(f"I love eating {my_list[1]}")
my_numlist2 = [56, 7, -3, -30, -1, 0]
print(f"{my_numlist2}")
my_numlist2.sort()

# tuple datastructures/unchangeable/ordered
# tuple are immutable
my_tuple = ("Toyota", "Mercedes", "Nissan", "Subaru", "BMW", "Ranger Rover")
print(f"{my_tuple[3]} is manufactured in Japan")

# set datastructures
# unordered
my_set = {"Kenya", "Uganda", "Nigeria", "Mozambique", "South Africa"}
print(my_set)
my_set.add("Senegal")

# dictionaries datastructures

my_dic = {"Name": "Olive", "Age": 50, "Gender": "Female", "Profession": "Software engineer"}
print(my_dic)
print(f"My name is {my_dic['Name']}")
print(f"I am {my_dic['Age']} years old")
print(f"I am a {my_dic['Gender']}")
print(f"And I am a {my_dic['Profession']}")
