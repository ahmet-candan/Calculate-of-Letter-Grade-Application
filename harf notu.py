import time

def not_hesapla(satır):
    
    satır = satır[:-1]
    satır= satır.split(",")

    isim = satır[0]
    not1 = int(satır[1])
    not2 = int(satır[2])
    not3 = int(satır[3])

    son_not = not1 * (3/10) + not2 * (3/10) + not3 * (4/10)

    if (son_not>=90):
        harf ="AA"

    elif (son_not>=85):
        harf = "BA"

    elif (son_not>=80):
        harf = "BB"

    elif (son_not>=75):
        harf = "CB"

    elif (son_not>=65):
        harf = "CC"

    elif (son_not>=60):
        harf = "DC"

    elif (son_not>=55):
        harf = "DD"

    else:
        harf = "FF"

    return isim + " ---------------> " + harf + " " + str(son_not) + "\n"

    

print("""                         ************* Harf Notu Uygulamasına Hoşgeldiniz *************
 ******************** Öğrencilerin Yıl Sonu ve Harf Notunu Hesaplamak İçin 1'i Tuşlayınız  ******************** """)

secim = input()

if (secim =="1"):
    print("Notlar Hesaplanıyor Lütfen Bekleyiniz..")
    time.sleep(2)
    with open("ogrenciler.txt","r",encoding="utf-8") as file:
        yeni_liste = []
        for i in file:
        
            yeni_liste.append(not_hesapla(i))

            with open("sonuclar.txt","w",encoding="utf-8") as file2:

                for i in yeni_liste:
                    file2.write(i)
        print("\nÖğrencilerin Notları sonuclar.txt adlı dosyaya kaydedildi")

else:
    print("Çıkış Yapılıyor...")
    time.sleep(0.5)