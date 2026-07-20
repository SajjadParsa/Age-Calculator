def user_age(user_name,user_bt,user_cYear):
    if user_bt >user_cYear:
        print("Birth year can not be greater than current year")
        return

    age=user_cYear - user_bt
    months= age * 12
    days= age*365
    hours= days * 24
    minutes= hours * 60
    left = 100 - age
    print("""

        """)

    if age>=18 and age<=30:
        print("You are a young adult!")
    elif age>=31 and age<=60:
        print("You are a adult!")
    elif age>=61 and age<=120:
        print("You are a senior!")
    elif age>=1 and age<=17:
        print("You are under 18!")
    elif age <= 0 or age >=121:
        print("Invalid age!")
        return

    if left>0:
        print(f"You have {left} years left until your 100th birthday.")
    elif left==0:
        print("Congratulations! You are 100 years old!")
    print("""

        """)
    
    print(f"Hello {user_name} Now you are {age}.\t You have lived:   \n {months} months \n {days} days \n {hours} hours \n {minutes} minutes!")
    print("""

        """)
#پروژه محاسبه سن
while True:
    while True:
        user_name=input("Enter Your name:    ")
        if user_name.isalpha():
            break
        print("please Enter a valid name.")

    try:
        user_bt=int(input("Enter Your Birthday year:   "))
        user_cYear=int(input("Enter current year:  "))
        

        user_age(user_name,user_bt,user_cYear)

        user=input("Do you want to calculate again? (Yes/No)   ")

    except ValueError:
        print("Enter valid Year!")
        continue
    if user=="No":
        print("have a nice day dude")
        break
