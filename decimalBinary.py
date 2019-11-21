s ='''karnataka bangalore lalbagh
tamilnadu Kanyakumari vivekananda_rock
kerala thiruvanthapuram padmanabha_temple
karnataka Mysore brindavan_gardens
karnataka hassan shravanabelagola
tamilnadu chennai egmore_museum
tamilnadu kanyakumari kaamaakshmi_temple
karnataka bangalore cubbon_park
karnataka hampi maharnavami_dibba
karnataka bangalore bangalore_palace
karnataka hassan halebeedu
tamilnadu chennai ashtalakshmi_temple
karnataka hampi purandara_mantapa
karnataka Mysore ambavilas_palace
kerala thiruvanthapuram zoo
karnataka hassan belur
tamilnadu chennai valluvar_kootam
karnataka hampi vijaya_vittal_temple'''
#1. Number of unique states
uniqueStates=set()
lines=s.split('\n')
for line in lines:
    word=line.split()
    state=word[0]
    uniqueStates.add(state)
print(uniqueStates)     

#2. list the number of cities per state
d={}





