#Rock Paper Scissors

import random
import time

game = "Begin"
while game == "Begin":
    numberOfMoveCPU = random.randint(1, 3)
    if numberOfMoveCPU == 1:
        CpuMove = "Rock"
    elif numberOfMoveCPU == 2:
        CpuMove = "Scissors"
    elif numberOfMoveCPU == 3:
        CpuMove = "Paper"
    move = input("Please select Rock, Paper or Scissors (spell same way). ")
    print("Player: ", move, "CPU: ", CpuMove)
    time.sleep(1)
    if CpuMove == "Rock" and move == "Rock":
        print("TIE!")
        numberOfMoveCPU = random.randint(1, 3)
    elif CpuMove == "Scissors" and move == "Rock":
        print("PLAYER WINS")
        numberOfMoveCPU = random.randint(1, 3)
    elif CpuMove == "Paper" and move == "Rock":
        print("CPU WINS")
    elif CpuMove == "Scissors" and move == "Scissors":
        print("TIE!")
        numberOfMoveCPU = random.randint(1, 3)
    elif CpuMove == "Scissors" and move == "Paper":
        print("CPU WINS")
        numberOfMoveCPU = random.randint(1, 3)
    elif CpuMove == "Scissors" and move == "Rock":
        print("PLAYER WINS")
        numberOfMoveCPU = random.randint(1, 3)
    elif CpuMove == "Paper" and move == "Paper":
        print("TIE!")
        numberOfMoveCPU = random.randint(1, 3)
    elif CpuMove == "Paper" and move == "Scissors":
        print("PLAYER WINS")
        numberOfMoveCPU = random.randint(1, 3)
    elif CpuMove == "Paper" and move ==  "Rock":
        print("CPU WINS")
        numberOfMoveCPU = random.randint(1, 3)
    elif CpuMove == "Rock" and move == "Paper":
        print('CPU WINS')
        numberOfMoveCPU = random.randint(1, 3)
    
    else:
        print('Please try again, the game did not compute')
        numberOfMoveCPU = random.randint(1, 3)
        
    numberOfMoveCPU = random.randint(1, 3)    