
ZodiacSign = ("Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat")

try:
    WhatYear = int(input("Enter a year!: "))
    if WhatYear >= 0:
        WhatYear %= 12
        print(ZodiacSign[WhatYear])
    elif WhatYear < 0:
        print("Negative number")
except ValueError:
    print("Invalid input")


