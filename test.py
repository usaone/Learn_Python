name1 = "Hello"
name2 = 10
name3 = 10.5
mylist1 = [1, "Hi there", 10.5, name1]
user_age = int(input("Enter your age: "))
current_yr = int(input("Enter current year: "))

print(name1.upper())
print(name1.capitalize())

for item in mylist1:
    if type(item) == int:
        product = item * 10
        print(product)
    elif type(item) == float:
        product = item * 100
        print(product)
    else:
        print("Item is probably a string")

def birth_year(age, current_year):
    birth_yr = current_year - age
    return birth_yr
print(birth_year(user_age, current_yr))

#file = open("example.txt", "r")
#content = file.read()
#file2 = open("example2.txt", "w")
#file2.write("Hey there, what's up??")
#print(content)