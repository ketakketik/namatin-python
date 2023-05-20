# float mengkonversi bilangan bulat ke float
berat = float(input("Masukan berat kamu dalam kg: "))
tinggi = float(input("Masukan tinggi kamu dalam cm: "))

def rumus_bmi(berat, tinggi):
    bmi = berat / (tinggi / 100) ** 2
    return bmi

bmi = rumus_bmi(berat, tinggi)

def arti_bmi(bmi):
    if bmi < 18.5:
        return "Kerempeng lu"
    elif 18.8 <= bmi < 25:
        return "Normal lu dude"
    elif 25 <= bmi < 30:
        return "Kegendutan"
    else:
        return "OBESITAS"

arti_bmi = arti_bmi(bmi)

print("BMI kamu:", round(bmi, 2)) # round untuk membulatkan angka, argumen kedua untuk mempertahan jumlah digit dibelakang titik
print("Yang artinya:", arti_bmi)