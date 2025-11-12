
password1 = int(input("Not defterine girmek için kullanılacak şifrenizi belirleyiniz: "))

def not_ekle(yazkizim):
    with open("sifrelinot.txt", "a", encoding='utf-8') as file:
        file.write(yazkizim+ "\n")

def notlariGor():
    with open("sifrelinot.txt", "r", encoding='utf-8') as file2:
        print(file2.readlines())


sifre = int(input("Not defterine girmek için şifre giriniz: "))
while True:
    try:
        if sifre == password1:
            print("Not defterinde ne yapmak istiyorsunuz?\n1-Not ekleme\n2-Notları okuma\n3-Çıkış")
            gir = int(input(": "))
            if gir == 1:
                yaz = input("Buyrun yazın: ")
                not_ekle(yaz)
            elif gir == 2:
                notlariGor()    
            elif gir == 3:
                break
        else:
            print("Şifreyi yanlış girdiniz bay bay:(")
            break
    except Exception as e:
        print("Hata mesajı: ", e)
      
