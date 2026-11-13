for cont in range (1, 30, 1):
    resto_3 = cont % 3 
    resto_7 = cont % 7
    if resto_3 == 0 and resto_7 == 0:
        print (cont)