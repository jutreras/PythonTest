def validaRut(rut):
    rut=rut.replace('.','').replace('-','')
    dv = rut[len(rut)-1:]
    acum = 0
    factor = 2
    dvr = 0
    """for i in rut[:len(rut)-1][::-1]:
         for x in range(2,8):"""
    for i in reversed(range(0,len(rut)-1)):
        if (factor > 7):
            factor = 2
        acum = acum + (factor*int(rut[i]))
        factor += 1
    dvr = 11 - (acum % 11)

    if (dvr==10):
        return (dv.upper()=='K')
    elif (dvr==11):
        return (dv=='0')
    else:
        return (dvr==int(dv))

    return False
