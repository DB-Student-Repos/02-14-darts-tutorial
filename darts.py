def score(x, y):
    a=((x*x)+(y*y))
    if (a<(1*1)):
        return "player earns 10 points"
    elif (a<(5*5)):
        return "player earns 5 points"
    elif (a<(10*10)):
        return "player earns 1 points"
    else:
        return "player earns 0 points"
    
    
