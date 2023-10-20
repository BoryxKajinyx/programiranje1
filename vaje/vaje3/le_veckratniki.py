xs = [42, 84, 126, 168]

samo_veckratniki = True
for x in xs:
    if x % 42 != 0:
        samo_veckratniki = False
        break
print(samo_veckratniki)
