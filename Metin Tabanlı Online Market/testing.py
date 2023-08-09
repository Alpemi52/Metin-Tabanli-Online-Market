import datetime

envanter = {"kuşkonmaz": [6, 3],
            "brokoli": [20, 7],
            "havuç": [15, 5],
            "elmalar": [25, 15],
            "muz": [19, 18],
            "meyve": [23, 5],
            "yumurta": [44, 4],
            "karışık meyve suyu": [1, 19],
            "balık çubukları": [27, 10],
            "dondurma": [0, 4],
            "elma suyu": [33, 8],
            "portakal suyu": [32, 4],
            "üzüm suyu": [21, 16],
            }
kullanicilar = {
    "ahmet": "İstinye123",
    "Meryem": "4444",
    "": ""
}
sepet = {}


def SatinAl(username):
    toplam = 0
    sayac = 0
    print("Makbuzunuz işleniyor...\n\n******* İstinye Online Market ********\n*************************************")
    print("\t0850 283 6000\n\tistinye.edu.tr")
    print("—" * 37)
    for name, data in sepet.items():
        toplam = toplam + (data[1] * data[0])
        envanter[name] = [envanter[name][0] - data[0], data[1]]
        print("\t" + str(sayac + 1) + ". " + name + " =" + str(data[1]) + "$ miktar=" + str(data[0]) + " toplam=" + str(
            data[1] * data[0]) + "$")
    print("—" * 37)
    print("Toplam " + str(toplam) + "$")
    print("—" * 37)
    now = datetime.datetime.now()
    print(now.strftime("%d/%m/%Y %H:%M:%S"))
    print("Online Market’imizi kullandığınız için teşekkür ederiz!\n")
    sepet.clear()
    Anasayfa(username)


def SepeteGit(username):
    tempSepet = []
    print("Sepetiniz şunları içerir:\n")
    if (len(sepet) > 0):
        sayac = 1
        toplam = 0
        for name, data in sepet.items():
            tempSepet.append(name)
            toplam = toplam + (data[1] * data[0])
            print("\t" + str(sayac) + ". " + name + " =" + str(data[1]) + "$ miktar=" + str(data[0]) + " toplam=" + str(
                data[1] * data[0]) + "$")
            sayac = sayac + 1
        sayac = 0
        print("Toplam " + str(toplam) + " $\n")
        durum = True
        while (durum):
            secim = int(input(
                "Bir seçeneği seçiniz:\n1. Tutarı güncelleyin\n2. Bir öğeyi kaldırın\n3. Satın al\n4. Ana menüye dön\n\nSeçiminiz:"))
            if secim == 1:
                oge = int(input("Lütfen miktarını değiştireceğiniz öğeyi seçin:"))
                if tempSepet[oge - 1] in sepet:
                    miktar = int(input("Lütfen yeni miktarı yazın:"))
                    sepet[tempSepet[oge - 1]] = [miktar, sepet[tempSepet[oge - 1]][1]]
                    print("Sepetiniz artık şunları içeriyor:")
                    for name, data in sepet.items():
                        toplam = toplam + (data[1] * data[0])
                        print("\t" + str(sayac + 1) + ". " + name + " =" + str(data[1]) + "$ miktar=" + str(
                            data[0]) + " toplam=" + str(data[1] * data[0]) + "$")
                    sayac = 0
                else:
                    print("Sepette böyle bir öğe bulunmamaktadır!")
            elif (secim == 2):
                oge = int(input("Lütfen kaldıracağınız öğeyi seçin:"))
                if tempSepet[oge - 1] in sepet:
                    sepet.pop(tempSepet[oge - 1])
                    print(str(tempSepet[oge - 1]) + " öğesi başarıyla kaldırıldı!")
                    if (len(sepet) > 0):
                        for name, data in sepet.items():
                            toplam = toplam + (data[1] * data[0])
                            print("\t" + str(sayac) + ". " + name + " =" + str(data[1]) + "$ miktar=" + str(
                                data[0]) + " toplam=" + str(data[1] * data[0]) + "$")
                            sayac = sayac + 1
                    else:
                        print("Sepetinizde görüntülenecek öğe bulunmamaktadır.\nToplam: 0$")
                else:
                    print("Sepette böyle bir öğe yok")

            elif (secim == 3):
                SatinAl(username)
            elif (secim == 4):
                durum = False
                Anasayfa(username)

    else:
        print("Sepetinizde görüntülenecek öğe bulunmamaktadır.\nToplam: 0$")
        Anasayfa(username)


def UrunAra(username):
    aranan_kelime = input("Ne arıyorsunuz?: ")
    sonuclar = []
    for name, data in envanter.items():
        if (data[0] > 0 and aranan_kelime in name):
            sonuclar.append([name, data[1]])

    print(len(sonuclar), "benzer ürün bulundu:\n")

    for i in range(len(sonuclar)):
        print(str(i + 1) + ".", str(sonuclar[i][0]), str(sonuclar[i][1]) + "$")
    durum = True
    while (durum):
        secim = int(input("Lütfen sepetinize eklemek istediğiniz ürünü seçin (Ana menü için 0 girin):"))
        if secim == 0:
            Anasayfa(username)
            durum = False
        else:
            if secim > len(sonuclar):
                print("Geçersiz bir secim yaptınız. Lütfen tekrar deneyin!\n")
                continue
            else:
                durum2 = True
                while (durum2):
                    miktar = int(
                        input(str(sonuclar[secim - 1][0]) + " ekleniyor. Tutarı Girin(Ana menü için 0 girin):"))
                    if miktar == 0:
                        Anasayfa(username)
                        durum2 = False
                    else:
                        if miktar > envanter[sonuclar[secim - 1][0]][0]:
                            print("Üzgünüm! Miktar sınırı aşıyor, Lütfen daha küçük bir miktarla tekrar deneyin")
                            continue
                        else:
                            if sonuclar[secim - 1][0] in sepet:
                                urun_miktari = sepet[sonuclar[secim - 1][0]][0]
                                sepet[str(sonuclar[secim - 1][0])] = [urun_miktari + miktar, int(
                                    sonuclar[secim - 1][1])]  # sepet[uzumsuyu] = "19, 1" fiyat/adet
                                print("Sepetinize " + str(
                                    sonuclar[secim - 1][0]) + " eklendi.\nAna menüye geri dönülüyor...\n")
                                Anasayfa(username)
                            else:
                                sepet[str(sonuclar[secim - 1][0])] = [miktar, int(
                                    sonuclar[secim - 1][1])]  # sepet[uzumsuyu] = "19, 1" fiyat/adet
                                print("Sepetinize " + str(
                                    sonuclar[secim - 1][0]) + " eklendi.\nAna menüye geri dönülüyor...\n")
                                Anasayfa(username)
                            durum2 = False
                durum = False


def Anasayfa(username):
    print("Hoşgeldiniz " + username + "! Lütfen ilgili menü numarasını girerek aşağıdaki seçeneklerden birini seçin.")
    secim = int(input(
        "Lütfen aşağıdaki hizmetlerden birini seçin:\n1. Ürün ara\n2. Sepete git\n3. Satın al\n4. Oturum Kapat\n5. Çıkış yap\n\nSeçiminiz:"))
    if (secim == 1):
        UrunAra(username)
    elif (secim == 2):
        SepeteGit(username)
    elif (secim == 3):
        SatinAl(username)
    elif (secim == 4):
        print("Oturum sona erdi!")
        GirisYap()
    elif (secim == 5):
        print("Uygulamadan çıkış yapılıyor...")
        exit()


def GirisYap():
    print(
        "**** İstinye Online Market’e Hoşgeldiniz ****\nLütfen kullanıcı kimlik bilgilerinizi sağlayarak giriş yapın:\n")
    durum = True
    while (durum):
        kullanici_adi = input("Kullanıcı adı:")
        sifre = input("Şifre:")
        if (kullanici_adi in kullanicilar.keys() and sifre == kullanicilar[kullanici_adi]):
            durum = False
        else:
            print("Kullanıcı adınız ve / veya şifreniz doğru değil. Lütfen tekrar deneyin!")
    print("Başarıyla giriş yapıldı!")
    Anasayfa(kullanici_adi)


GirisYap()
