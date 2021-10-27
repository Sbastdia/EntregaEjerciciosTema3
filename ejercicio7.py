def añoBisiesto(año):
    añoBisiesto= True
    if(año%4==0):
        añoBisiesto=True
        if(año%100==0):
            añoBisiesto=False
            if(año%400==0):
                añoBisiesto=True
    else:
        añoBisiesto=False
    return añoBisiesto

