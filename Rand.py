while True:
    import time, random
    print("""

    =======+++=======
        WELCOME TO
        PERSIMMON
    =======+++=======


    """)
    time.sleep(2)
    difficulty = input("SELECT YOUR DIFFICULTY: TYPE 'EASY' OR 'HARD' ")
    time.sleep(2)
    if difficulty == "EASY":
        maxn = 5
    elif difficulty == "HARD":
        maxn = 10
    else:
        print("""

    =======+++=======
          ERROR:
     ENTER A CORRECT
          VALUE!
      RESTARTING...
    =======+++=======

        """)
        time.sleep(3)
        continue
    rules = input("Would you like to read the rules? Y/N ")
    if rules == "Y":
        print("""RULES:
A number will be randomly selected each round.
Guess the number correctly to get 10 points.
If you don't guess correctly, not to worry, but you will lose 1 point.
You are guessing between 1 and""",str(maxn) + """.
Good luck!""")
        
    elif rules == "N":
        pass
    
    else:
        print("""

    =======+++=======
          ERROR:
     ENTER A CORRECT
          VALUE!
      RESTARTING...
    =======+++=======

        """)
        time.sleep(3)
        continue
        
    score = 0
    playing = "Y"
    while playing == "Y":
        time.sleep(0.5)
        randint = random.randint(1,maxn)
        guess = int(input("TIME TO GUESS! GUESS A NUMBER BETWEEN 1 AND " + str(maxn) + "! "))
        if guess == randint:
            score += 10
            print("CORRECT! YOUR SCORE IS NOW",str(score) + "!")
        else:
            score += -1
            print("INCORRECT! YOUR SCORE IS NOW",str(score) + ".")
        playing = input("PLAY ANOTHER? Y/N ")

    time.sleep(2)
    print("GAME OVER! You scored",str(score) + "!")
