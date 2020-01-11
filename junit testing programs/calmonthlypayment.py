def payment(p,y,R):
    n = 12 * y
    r = R /(12*100)
    return int(p*r/(1-(1+r)**(-n)))