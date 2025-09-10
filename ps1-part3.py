
def heart_rate(age, goal):
    max_HR = 220 - age
    print(f"Your maximum heart rate is :{max_HR}")
    if goal == "S":
        print(f"Your target heart rate is between {0.8 * max_HR} and {max_HR}")
    if goal == "E":
        print(f"Your target heart rate is between {0.6 * max_HR} and {0.8 * max_HR}")

user_age = int(input("What is your age:"))
user_goal = input("Is your goal speed (S) or endurance(E)?")

heart_rate(user_age, user_goal)
