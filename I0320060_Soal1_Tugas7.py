#fungsi center
kata = "Selamat Pagi Dunia Tipu Tipu"
cntr = kata.center(50, '-')
print(cntr)

print("="*60)

#fungsi upper
nama = input("Kami kepo dengan nama Anda nich kawan: ")
print("Kawan ingin menjadi: ")
print("1. Besar")
print("2. Kecil")
choice = int(input("> "))
if choice == 1:
    print("Selamat",nama.upper(),",Anda menjadi besar.")
elif choice == 2:
    print("Selamat",nama.lower(),", Anda menjadi kecil.")
else:
    pass

print("="*60)
print("Ayo main quizzzz!")
soal = "Presiden ke-2 adalah Pak Jokowi"
print(soal)
print("-"*10)
print("Coba benarkan pernyataan tersebut")
print("-"*10)
print("Apa jawaban kawan?")
kaaata = input("> ")
print("-"*10)
#fungsi replace
print("Jawaban kawan adalah: ",soal.replace("Jokowi", kaaata))


