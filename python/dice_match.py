import random

def dice_throw():
    
    throws = 0
    
    
    while True:
        
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        
       
        throws += 1
        
       
        print("Throw "+(str(throws))+": Die 1 - "+(str(dice1))+", Die 2 - "+(str(dice2)))
        
        
        if dice1 == dice2:
            break
    
    
    print("It took "+(str(throws))+" throws to get a matching pair.")

dice_throw()
