import time

def heading(text):       #Heading mechanism
    print(f"{'='*len(text)}")
    print(text)
    print(f"{'='*len(text)}")
heading("TIMER")
while True:        # Odd loop mechanism
    again = None

    def timer(duration):      #Function for timer 
        print(f"Timer set for {duration} seconds")
        for i in range(duration, 0, -1):
            print(i)
            time.sleep(1)
        print("Time's up")
    duration = int(input("Enter the duration of timer in seconds: "))
    timer(duration)
    again = input(
        "Wanna try again? (Press (\"N\" or \"n\") for \"No\", and any other key for \"Yes\"): ")
    if (again == "N" or again == "n"):  #This will decide whether the odd loop should execute or not 
        break
#PROJECT MADE BY : FAIZAN ASHRAF
# ROLL NUMBER :18 