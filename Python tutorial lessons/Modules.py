#Modules
#using converters module

#def lbs_to_kg(weight):
#    return weight * 0.45
#
#
#def kg_to_lbs(weight):
#    return weight / 0.45

import converters
from converters import kg_to_lbs

print(kg_to_lbs(100))

print(converters.kg_to_lbs(70))
