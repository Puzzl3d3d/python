# Conversion rates:

import re

pounds_to_kg = 0.45359237
cm_to_inch = 0.3937
feet_to_inches = 12
yard_to_metre = 0.9144
km_to_miles = 0.6214
sqrinch_to_sqrcm = 6.4516
ounce_to_gram = 28.35

# Conversion functions

def ounce_gram(ounce):
    return ounce * ounce_to_gram
def gram_ounce(gram):
    return gram / ounce_to_gram

def lbs_kg(lbs):
    return lbs * pounds_to_kg
def kg_lbs(kg):
    return kg / pounds_to_kg

def cm_inch(cm):
    return cm * cm_to_inch
def inch_cm(inch):
    return inch / cm_to_inch

def feet_inch(feet):
    return feet * feet_to_inches
def inch_feet(inch):
    return inch / feet_to_inches

def yard_metre(yard):
    return yard * yard_to_metre
def metre_yard(metre):
    return metre / yard_to_metre

def km_mile(km):
    return km * km_to_miles
def mile_km(mile):
    return mile / km_to_miles

def inch2_cm2(inch2):
    return inch2 * sqrinch_to_sqrcm
def cm2_inch2(cm2):
    return cm2 / sqrinch_to_sqrcm


# Main functions

def run(string, val):
    result = eval(f"{string}({val})")

    print(result)

def split_on_letter(s):
    match = re.compile("[^\W\d]").search(s)
    return [s[:match.start()], s[match.start():]]

while True:
    val,unit = split_on_letter(input("Units: "))
    val = float(val)
    convert_unit = input("Convert to: ")

    run(f"{unit}_{convert_unit}", val)

    print("\n")

    
