def score(x, y):
    a=((x*x)+(y*y))
    if (a<(1*1)):
        return 10
    elif (a<(5*5)):
        return 5
    elif (a<(10*10)):
        return 1
    else:
        return 0
    
    
