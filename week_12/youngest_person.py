people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]


younger_name = ''
younger_age = 5000 # We use an arbitrary number that is high enough so that no one in the list would be at that age.

for person in people:
    name, age = person.split(" ")
    age = int(age)

    if age < younger_age:
        younger_name = name
        younger_age = age

print(f"The youngest person is {younger_name}, {younger_age} years old.")
