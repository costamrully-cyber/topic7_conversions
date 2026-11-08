# Augustine
# conversions.py 

KM_PER_MILE = 1.609

def km_to_miles(km):
    return round(km / KM_PER_MILE, 2)

def celsius_to_fahrenheit(c):
    return round(c * 9 / 5 + 32, 1)

def shillings_to_dollars(ksh, rate=129):
    return round(ksh / rate, 2)