# 🧮 Oddiy Kalkulyator
# Muallif: Og'abek
# Tavsif: Foydalanuvchidan ikkita son olib, arifmetik amallarni bajaradi.

def qo‘shish(a, b):
    return a + b

def ayirish(a, b):
    return a - b

def ko‘paytirish(a, b):
    return a * b

def bo‘lish(a, b):
    if b == 0:
        return "❌ Nolga bo‘lish mumkin emas!"
    return a / b


def menyu():
    print("\n🧮 Oddiy Kalkulyator")
    print("1. Qo‘shish")
    print("2. Ayirish")
    print("3. Ko‘paytirish")
    print("4. Bo‘lish")
    print("5. Chiqish")


while True:
    menyu()
    tanlov = input("\nAmalni tanlang (1-5): ")

    if tanlov == "5":
        print("👋 Dastur tugatildi.")
        break

    try:
        a = float(input("Birinchi sonni kiriting: "))
        b = float(input("Ikkinchi sonni kiriting: "))
    except ValueError:
        print("⚠️ Iltimos, faqat son kiriting!")
        continue

    if tanlov == "1":
        print(f"Natija: {qo‘shish(a, b)}")
    elif tanlov == "2":
        print(f"Natija: {ayirish(a, b)}")
    elif tanlov == "3":
        print(f"Natija: {ko‘paytirish(a, b)}")
    elif tanlov == "4":
        print(f"Natija: {bo‘lish(a, b)}")
    else:
        print("❗ Noto‘g‘ri tanlov!")
