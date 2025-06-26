from datetime import datetime
birth_year=int(input("enter your birth year: "))
current_year=datetime.now().year
age=current_year-birth_year
print(f"you are {age} years old.")
if (age>=18):
    print("you can vote")
else:
    print("you are minor so you can not vote")
    pass
    print("Thanks for trying")