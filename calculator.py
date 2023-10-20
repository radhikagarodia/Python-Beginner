print("Lets Start Calculation")
x = True
while(x):
    print("Type add, mul, sub, div, pow as required")
    operation = input()
    flag = False
    if(operation not in ('add','sub','mul','div','pow')):
        print("invalid operation")
        continue
    for i in range(3,0,-1):
        num1 = input("enter first number")
        if(not(num1.lstrip('-').isdigit())):
            print(f"Please enter number. {i} tries left")
            if(i==3):
                flag = True
            continue
        break
    if(flag == True):
        print("Retries ended, Shutting down application!")
        break
    for i in range(3,0,-1):
        num2 = input("enter second number")
        if(not(num2.lstrip('-').isdigit())):
            print(f"Please enter number. {i} tries left")
            if(i==3):
                flag = True
            continue
        break
        flag = True
    if(flag == True):
        print("restart tries ended")
        break
    num1 = int(num1)
    num2 = int(num2)
    if(operation=='add'):
        print(num1+num2)
    elif(operation=='sub'):
        print(num1-num2)
    elif(operation=='mul'):
        print(num1*num2)
    elif(operation=='div'):
        if(num2==0):
            print('Cant divide by 0. Please enter valid number')
            continue
        print(num1/num2)
    elif(operation=='pow'):
        print(num1**num2)
    
    count = input("Do you want to continue. Type Y or N")
    if(count=='N' or count=='n'):
        x = False
    elif(count=='Y' or count=='y'):
        x = True
    else: 
        print("Please restart and enter valid argument")
        break
