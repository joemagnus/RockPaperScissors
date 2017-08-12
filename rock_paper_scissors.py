# here we import all the modules we need
from microbit import *
import random

# it sets the rand variable equal to the randint
rand = random.randint

rock = Image("00900:09090:90009:09090:00900")
paper = Image("99999:90009:90009:90009:99999")
scissors = Image("00900:09000:90000:09000:00900")
rps_arr = [rock, paper, scissors]
    
def randomselect():
    for i in range(5):
        display.scroll('3, 2, 1')
        # generates random integer, fetches element for that index from list
        answer = rps_arr[rand(0,2)]
        # prints rock, paper, or scissors
        display.show(answer)
        time.sleep(3)
    
while True:
    randomselect()
