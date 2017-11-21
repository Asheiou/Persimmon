def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
def restart():
    time.sleep(1)
    print("""
    =======+++=======
          ERROR:
     ENTER A CORRECT
          VALUE!
      RESTARTING...
    =======+++=======
        """)
    time.sleep(3)
    restart = 1

while True:
    import time, random
    print("""
    =======+++=======
        WELCOME TO
        PERSIMMON
    =======+++=======
    """)
    time.sleep(2)
    difficulty = input("SELECT YOUR DIFFICULTY: TYPE 'EASY' OR 'HARD', or 'HELP' for more options ")
    time.sleep(2)
    if difficulty == "EASY":
        maxn = 5
    elif difficulty == "HARD":
        maxn = 10
    elif difficulty == "HELP":
        what = input("""Welcome to the help menu.
1. Rules
2. Highscore""")
        if what == "1":
            print("""RULES:
A number will be randomly selected each round.
Guess the number correctly to get 10 points.
If you don't guess correctly, not to worry, but you will lose 1 point.
Good luck!""")
            time.sleep(6)
            continue
        elif what == "2":
            hisc = open("highscore.txt")
            print("HIGHSCORE =",hisc.read())
            time.sleep(5)
            
        else:
            restart()
            continue


    rounds = input("How many rounds would you like to play? ")
    
    if isInt(rounds) == True:
        rounds = int(rounds)
        if rounds <= 0:
            restart()
            continue
    else:
        restart()
        continue
    
    score = 0
                 
    for x in range(rounds):
        time.sleep(0.5)
        randint = random.randint(1,maxn)
        guess = int(input("TIME TO GUESS! GUESS A NUMBER BETWEEN 1 AND " + str(maxn) + "! "))
        if guess == randint:
            score += 10
            print("CORRECT! YOUR SCORE IS NOW",str(score) + "!")
        else:
            score += -1
            print("INCORRECT! YOUR SCORE IS NOW",str(score) + ".")

    time.sleep(2)
    print("GAME OVER! You scored",str(score) + "!")

    highscore = 0

with open("highscore.txt", "r+") as hisc:
    hi = hisc.read()
    if not hi:  
        hi = '0'
    if score > int(hi):
        print("NEW HIGHSCORE!")
        hisc.seek(0)  
        hisc.write(str(score))
    else:
        print("HIGHSCORE =%s" % hi)

    time.sleep(3)
        

