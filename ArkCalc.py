
from concurrent.futures.process import _ResultItem


def choices():
    userInput = input("Select a menu")
    switch = {
            "1": AttackSpeedCalc(),
            "2": "result2",
            "3": "result3",
        } 
    return switch.get(userInput, "default")

def AttackSpeedCalc():
     while True:
        apsdBuff = input("Input the aspdBuff of a operator: ")
        try:
            apsdBuff = float(apsdBuff)  
            
            print("Attack speed buff:", apsdBuff)
            break 
        except ValueError:
            print("Error: Please enter a valid number.") 
            AttackSpeedCalc()


def AttackSpeedFormula(aspdbuff, opsAtkInv, atkIntervalIncrease):
    result = ((100 + aspdbuff )/(opsAtkInv + atkIntervalIncrease)) / 100
    return 1 / result

def FinalAttackFormula(opsDefaultAtk,baseAtkBuff,flatAtkBuff,attackMultiplier):
    result = ((opsDefaultAtk * (1+ baseAtkBuff) + flatAtkBuff)* attackMultiplier)
    return result

def PhysicalDamageFormula(opFinalAtk, scaleDefDown,flatDefDown,physicalDMGAtkBuff,enemyDef):
    result = (opFinalAtk - (enemyDef + flatDefDown) * (scaleDefDown)) * physicalDMGAtkBuff
    return result


choices()
