# lahko sestaviš več seznamov v en seznam terk z zip (pred 3.0)
teze = [74, 83, 58, 66, 61, 84]
imena = ["Anže", "Benjamin", "Cilka", "Dani", "Eva", "Franc"]
studentka = [False, False, True, False, True, False]
student_zip = zip(teze, imena, studentka)
# skozi to lahko greš z for zanko

for teza, ime, _ in student_zip:
    print(ime, " : ", teza)
# če hočeš dobit dejanski seznam:
student = list(student_zip)
