# print("cheack the vm")


# mystr = "aeitoasndlakjio"

# print("z" not in mystr)

# marks = 95
# passing_marks = 40

# if marks >= passing_marks:
#     print("Congratulations! You passed")
# else:
#     shortage = passing_marks - marks
#     print(f"You failed. Need {shortage} more marks")


# marks = 95

# if marks >= 90:
#     print("Grade: A")
# elif marks >= 80:
#     print("Grade: B")
# elif marks >= 70:
#     print("Grade: C")
# elif marks >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")


# age = 25
# has_ticket = True
# has_id = True

# if age >= 18:
#     if has_ticket:
#         if has_id:
#             print("Entry granted - Enjoy the event")
#         else:
#             print("ID verification required")
#     else:
#         print("Please purchase a ticket")
# else:
#     print("Sorry, event is 18+ only")


# day = "unkonwday"

# match day:
#     case "Monday":
#         print("Start of the work week")
#     case "Friday":
#         print("Last working day")
#     case "Saturday" | "Sunday":
#         print("Weekend!")
#     case _:
#         print("Midweek day")


# month = "May"

# match month:
#     case "December" | "January" | "February":
#         print("Winter")
#     case "March" | "April" | "May":
#         print("Spring")
#     case "June" | "July" | "August":
#         print("Summer")
#     case "September" | "October" | "November":
#         print("Autumn")
#     case _:
#         print("Invalid month")


# user = {"name": "Alice", "role": "admin"}

# match user:
#     case {"role": "admin"}:
#         print("Administrator access granted")
#     case {"role": "user"}:
#         print("Standard user access")
#     case {"role": "guest"}:
#         print("Limited guest access")
#     case _:
#         print("Unknown role")

# age = 20
# status = "Adult" if age >= 18 else "Minor"
# print(status)  # Adult


# student = {"name": "Alice", "age": 20, "grade": "A"}

# # Iterate over keys
# for key in student:
#     print(key)
# # Output: name age grade

# # Iterate over values
# for value in student.values():
#     print(value)
# # Output: Alice 20 A

# # Iterate over key-value pairs
# for key, value in student.items():
#     print(f"{key}: {value}")
# # Output: name: Alice, age: 20, grade: A



# for i in range(1,101,2):
#     print(i)


fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Output:
# 0: apple
# 1: banana
# 2: cherry

# restart learning python using gfg