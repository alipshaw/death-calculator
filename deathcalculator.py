# Import datetime module
import datetime
import random

# Ask for user's name and birthday
while True:
    name = input('What is your name?: ').strip().title()
    while True:
        try:
            birth_year = int(input('What year were you born? (Please enter four digits.): '))
        except ValueError:
            print("Sorry, that's not a valid year.")
            continue
        if birth_year < (datetime.date.today().year - 100) or birth_year > datetime.date.today().year:
            print("Sorry, that's not a valid year.")
            continue
        else:
            break
    while True:    
        try:
            birth_month = int(input('What month were you born? (Please enter two digits.): '))
        except ValueError:
            print("Sorry, that's not a valid month.")
            continue
        if birth_month < 1 or birth_month > 12:
            print("Sorry, that's not a valid month.")
            continue
        else:
            break
    while True:
        try:
            birth_day = int(input('What day were you born? (Please enter two digits.): '))
        except ValueError:
            print("Sorry, that's not a valid day.")
            continue
        if birth_day < 1 or birth_day > 31:
            print("Sorry, that's not a valid day.")
            continue
        else:
            break

# Figure out user's full birthdate and today's date    
    birthdate = datetime.date(birth_year, birth_month, birth_day)
    today = datetime.date.today()
    currentYear = datetime.datetime.now().year

# Calculate user's age    
    def calculate_age(born):
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    age = calculate_age(birthdate)
    if age < 13:
        print("You're too young for this! Try again later.")
        exit()
    elif age >= 123:
        print("""The oldest recorded human being lived to 122. I think you're lying. Try again later.""")
        exit()

# Calculate year user will die
    if age <= 42:
        death_year = int(currentYear + random.randint(5,80))
    else:
        death_year = int(currentYear + (random.randint(5,(80 - (age - 42)))))

# Calculate age of death
    death_age = int(death_year - birth_year)

# Calculate cause of death
    ailment = [
    "burned at the stake",
    "a rare parasite",
    "a tragic bus accident",
    "lost on Mount Everest",
    "a cave diving incident",
    "mauled by a bear",
    "murdered by a clown",
    "human sacrifice",
    "lost at sea",
    "lost in Yonkers",
    "surfeit of eels",
    "trampled by badgers",
    "eaten by wild dogs",
    "bubonic plague",
    "heavy metal poisoning",
    "cannibalism"
    ]
    if death_age <= 40:
        cause = "nothing because you are too young to die!"
    else:
        cause = random.choice(ailment)

# Display message to user
    print(f'Congrats, {name}, you are {age} years old!')
    print (f'You will die in the year {death_year} at age {death_age}. Your cause of death will be: {cause}.')
       
   
