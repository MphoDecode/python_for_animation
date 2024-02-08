name = "Mpho"
print(name)

def ask_age():
    age = input("How old is Mpho? ")
    return age

def ask_location():
    location = input("Where does Mpho stay? ")
    return location

age = ask_age()
location = ask_location()

print(name + " is " + age + " years old.")
print(name + " stays in " + location + ".")
print(name + " is beautiful.")
