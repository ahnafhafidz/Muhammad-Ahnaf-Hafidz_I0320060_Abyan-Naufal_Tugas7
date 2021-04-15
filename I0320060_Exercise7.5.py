def panggil(func):
    return func
def helloworld(func):
    return "HELLO WORLD"
def main():
    daftarnama = ["Adi, Cahyo, Budi, Dedi"]
    print("Keadaan Awal")
    print(daftarnama)

    print("\n Menggunakan sorted():")
    print(sorted(daftarnama))

    daftarnama.sort(key=lambda n: n.lower)

    print("\n Keadaan Akhir:")
    print(daftarnama)

if __name__ == '__main__':
    main()

