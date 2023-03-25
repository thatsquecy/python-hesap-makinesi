def topla(x, y):
    return x + y

def cikar(x, y):
    return x - y

def carp(x, y):
    return x * y

def bol(x, y):
    return x / y

def mod(x, y):
    return x % y

print("Yapılacak İşlemler:")
print("1.Toplama")
print("2.Çıkarma")
print("3.Çarpma")
print("4.Bölme")
print("5.Mod alma")

while True:
    secim = input("Hangi işlemi yapmak istiyorsunuz? (1/2/3/4/5): ")
    
    if secim in ('1', '2', '3', '4', '5'):
        sayi1 = float(input("Birinci sayıyı girin: "))
        sayi2 = float(input("İkinci sayıyı girin: "))
        
        if secim == '1':
            print(sayi1, "+", sayi2, "=", topla(sayi1, sayi2))
        
        elif secim == '2':
            print(sayi1, "-", sayi2, "=", cikar(sayi1, sayi2))
        
        elif secim == '3':
            print(sayi1, "*", sayi2, "=", carp(sayi1, sayi2))
        
        elif secim == '4':
            print(sayi1, "/", sayi2, "=", bol(sayi1, sayi2))
        
        elif secim == '5':
            print(sayi1, "%", sayi2, "=", mod(sayi1, sayi2))
        break
    else:
        print("Geçersiz giriş")
