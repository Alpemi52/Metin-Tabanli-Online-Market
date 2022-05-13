import datetime  # Güncel zamanı almak icin datetime kütüphanesini import ettik
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
            }  # Envanterimizi dict olarak tanımladık
kullanicilar = {
    "ahmet": ["İstinye123", {}],
    "Meryem": ["4444", {}],
    "": ["", {}] }# Giriş yapacak kullanıcıların username/pass ve sepetlerini tuttuğumuz dicti oluşturduk (Boş kullanıcımız test kullanıcımızdır)

def SatinAl(username):  # SatinAl metodu
    toplam = 0  # Sepetteki toplam ürün fiyatını sakladığımız değişken
    sayac = 1  # Ürün sırası için sayacımız
    print("Makbuzunuz işleniyor...\n\n******* İstinye Online Market ********\n*************************************")
    print("\t0850 283 6000\n\tistinye.edu.tr")
    print("—" * 37)  # Çizgi dekorasyonumuz
    for name, data in kullanicilar[username][1].items():  # Kullanıcının sepetindeki tüm öğeleri teker teker çağırıyoruz
        toplam = toplam + (data[1] * data[0])  # Ürünlerin fiyat ve miktarını çarparak toplam değişkenine atıyoruz
        envanter[name] = [envanter[name][0] - data[0],data[1]]  # Sepetimizdeki ürünün envanter stoğunu düşürüp yeni değerini atıyoruz
        print("\t" + str(sayac) + ". " + name + " =" + str(data[1]) + "$ miktar=" + str(data[0]) + " toplam=" + str(data[1] * data[0]) + "$")
        sayac = sayac + 1
    print("—" * 37)
    print("Toplam " + str(toplam) + "$")  # Toplam miktarı yazdırıyoruz
    print("—" * 37)
    now = datetime.datetime.now()  # Şimdiki zamanı almak icin datetime now fonksiyonunu cağırıp now değişkenine atıyoruz
    print(now.strftime("%d/%m/%Y %H:%M:%S"))  # Zaman bilgisini formatlamak icin strftime yapılandırma metodunu kullandık - Bkz:https://stackoverflow.com/questions/7588511/format-a-datetime-into-a-string-with-milliseconds
    print("Online Market’imizi kullandığınız için teşekkür ederiz!\n")
    kullanicilar[username][1].clear()  # Kullanıcının sepetini temizliyoruz.
    Anasayfa(username)  # Ana sayfaya yönlendiriyoruz

def SepeteGit(username):  # Sepet metodumuz
    tempSepet = []  # Ürün adlarını, miktarlarını, fiyatlarını ve toplam fiyatlarını tutacağımız gecici sepetimiz
    print("Sepetiniz şunları içerir:\n")
    if (len(kullanicilar[username][1]) > 0):  # Kullanıcının sepeti boş değilse
        sayac = 1
        toplam = 0
        for name, data in kullanicilar[username][1].items():  # Sepetini listele
            tempSepet.append(name)  # Ürün adlarını gecici sepete ekle
            toplam = toplam + (data[1] * data[0])  # Ürünlerin toplam fiyatlarını bulmak icin toplam değişkenine her ürünün miktar*fiyatını eklettiriyoruz
            print("\t" + str(sayac) + ". " + name + " =" + str(data[1]) + "$ miktar=" + str(data[0]) + " toplam=" + str(data[1] * data[0]) + "$")
            sayac = sayac + 1  # Ürün sırasını belirtmek icin sayac kullanıyoruz
        sayac = 0
        print("Toplam " + str(toplam) + " $\n")  # Toplam fiyatı yazdırıyoruz.
        durum = True
        while (durum):  # İşlem yapana kadar alt menuyu getirir
            secim = int(input("Bir seçeneği seçiniz:\n1. Tutarı güncelleyin\n2. Bir öğeyi kaldırın\n3. Satın al\n4. Ana menüye dön\n\nSeçiminiz:"))  # int tipinde secim aldık
            if secim == 1:  # Secim 1 : Miktar değiştirme
                oge = int(input("Lütfen miktarını değiştireceğiniz öğeyi seçin:"))  # Öğe secimi
                if int(oge - 1) < len(tempSepet):  # Girilen değer sepette var olmayan index dışı bir değer değilse! (Var olan bir değerse)
                    if tempSepet[int(oge - 1)] in kullanicilar[username][1]:  # Secilen öğe kullanıcının sepetinde varsa
                        sayac = 1
                        miktar = int(input("Lütfen yeni miktarı yazın:"))  # Değiştirilecek miktarı seciyoruz
                        if miktar <= envanter[tempSepet[int(oge - 1)]][0]:  # Girdiğimiz miktar envanterdeki stok miktarından kücük ve eşitse
                            kullanicilar[username][1][tempSepet[int(oge - 1)]] = [miktar, kullanicilar[username][1][tempSepet[int(oge - 1)]][1]]  # Yeni miktar ile beraber kullanıcının sepeti güncellenir
                            tempSepet[int(oge - 1)] = [miktar, kullanicilar[username][1][tempSepet[int(oge - 1)]][1]]  # Gecici sebetimizdeki veriyi de güncelliyoruz
                            print("Sepetiniz artık şunları içeriyor:")
                            for name, data in kullanicilar[username][1].items():  # Sepetteki güncel verileri listeliyoruz
                                toplam = toplam + (data[1] * data[0])
                                print("\t" + str(sayac) + ". " + name + " =" + str(data[1]) + "$ miktar=" + str(data[0]) + " toplam=" + str(data[1] * data[0]) + "$")
                                sayac = sayac + 1
                        else:  # Girilen miktar envanterdeki miktardan büyükse uyarı mesajı verdirir ve yeniden yönlendirir
                            print("Geçersiz miktar girdiniz. Yeniden yönlendiriliyorsunuz...")
                            continue
                    else:  # Index dışı bir değerse mesaj verdirir
                        print("Sepette böyle bir öğe bulunmamaktadır!")
                        continue
                else:
                    print("Girdiğiniz numaraya ait öğe bulunamadı...")
                    continue
            elif (secim == 2):  # Secim 2 : Öğe Kaldırma
                oge = int(input("Lütfen kaldıracağınız öğeyi seçin:"))  # Kaldırılacak öğeyi alıyoruz
                if tempSepet[int(oge - 1)] in kullanicilar[username][1]:  # Sectiğimiz öğe kullanıcının sepetinde ise
                    sayac = 1
                    kullanicilar[username][1].pop(tempSepet[int(oge - 1)])  # pop metodu ile sectiğimiz öğeyi kullanıcının sepetinden çıkartıyoruz
                    print(str(tempSepet[int(oge - 1)]) + " öğesi başarıyla kaldırıldı!")  # Başarıyla kaldırıldı mesajı verdiriyoruz.
                    tempSepet.pop(int(oge - 1))  # Secilen öğeyi gecici sepetimizden de kaldırıyoruz
                    if (len(kullanicilar[username][1]) > 0):  # Sepetteki öğe miktarı 0'dan büyükse yani sepet boş değilse
                        for name, data in kullanicilar[username][1].items():  # Tüm itemleri listele
                            toplam = toplam + (data[1] * data[0])
                            print("\t" + str(sayac) + ". " + name + " =" + str(data[1]) + "$ miktar=" + str(data[0]) + " toplam=" + str(data[1] * data[0]) + "$")
                            sayac = sayac + 1
                    else:  # Sepet boş ise bilgilendirir ve ana menüye yönlendirir
                        print("Sepetinizde görüntülenecek öğe bulunmamaktadır.\nToplam: 0$")
                        print("Ana menüye yönlendiriliyorsunuz...")
                        Anasayfa(username)
                else:
                    print("Sepette böyle bir öğe yok")
            elif (secim == 3):  # Satın almaya yönlendirir
                SatinAl(username)  # Satın alma metodunu cağırıyoruz
            elif (secim == 4):  # Ana menüye dönüş
                durum = False  # Döngüyü durdur
                Anasayfa(username)
    else:  # Kullanıcının sepeti boşsa uyarı mesajı verir ve ana sayfaya yönlendirir
        print("Sepetinizde görüntülenecek öğe bulunmamaktadır.\nToplam: 0$")
        Anasayfa(username)

def UrunAra(username):
    aranan_kelime = input("Ne arıyorsunuz?: ")  # Aradığımız kelimeyi değişkene atıyoruz
    sonuclar = []  # Aranan sonucları toplayacağımız dizi
    for name, data in envanter.items():  # For döngüsüyle envanterimizde bulunan öğelerin bilgilerini tek tek alıyoruz
        if (data[0] > 0 and aranan_kelime in name):  # Aradığımız ürünün stoktaki miktarı 0'dan büyükse ve aranan kelimemiz envanterde bulunan öğenin isminin icinde varsa
            sonuclar.append([name, data[1]])  # sonuclar dizisine -> isim ve fiyattan oluşan dizi ekler
    if (len(sonuclar) < 1):  # cıkan sonucların boyutu 1den kücükse yani öğe bulunamadıysa uyarı mesajı verir ve yeniden UrunAra'ya yönlendirir.
        print("Aradığınız kriterde ürün bulunamadı. Lütfen tekrar deneyiniz...")
        UrunAra(username)
    print(len(sonuclar), "benzer ürün bulundu:\n")  # Kaç tane ürün bulunduğunu print eder
    for i in range(len(sonuclar)):  # sonucların boyutu kadar calısacak for döngüsü ile sonucların adları ve fiyatları yazdırılır.
        print(str(i + 1) + ".", str(sonuclar[i][0]), str(sonuclar[i][1]) + "$")
    durum = True
    while (durum):  # Bulunan öğelerde işlem yapmak icin menuyu getirir
        secim = int(input(
            "Lütfen sepetinize eklemek istediğiniz ürünü seçin (Ana menü için 0 girin):"))  # secim icin input alır
        if secim == 0:  # Secim 0'sa Anasayfa'ya yönlendirir
            Anasayfa(username)
            durum = False  # While döngümüzü bitir
        else:
            if secim > len(sonuclar):  # Secimimiz geçersizse
                print("Geçersiz bir secim yaptınız. Lütfen tekrar deneyin!\n")  # Uyarı mesajı verir
                continue
            else:
                durum2 = True
                while (durum2):  # Secim gecerliyse
                    miktar = int(input(str(sonuclar[secim - 1][0]) + " ekleniyor. Tutarı Girin(Ana menü için 0 girin):"))  # Eklenecek miktarı int olarak alıyoruz
                    if miktar == 0:  # Secim 0'sa Ana Menüye yönlendiriyoruz
                        Anasayfa(username)
                        durum2 = False
                    else:
                        if miktar > envanter[sonuclar[secim - 1][0]][0]:  # Girdiğimiz miktar envanterdeki ürün miktarından büyükse
                            print("Üzgünüm! Miktar sınırı aşıyor, Lütfen daha küçük bir miktarla tekrar deneyin")  # Hata mesajı verdir ve başa al
                            continue
                        else:  # Envanterde girdiğimiz miktar kadar varsa
                            if sonuclar[secim - 1][0] in kullanicilar[username][1]:  # Secim yaptığımız ürün kullanıcının sepetinde varsa
                                urun_miktari = kullanicilar[username][1][sonuclar[secim - 1][0]][0]  # Kullanıcının sepetinde var olan sectiğimiz ürünün ürün miktarını alıyoruz
                                kullanicilar[username][1][str(sonuclar[secim - 1][0])] = [urun_miktari + miktar, int(sonuclar[secim - 1][1])]  # Kullanıcının sepetine yeni miktarımız ile ekleme yapıyoruz
                                print("Sepetinize " + str(sonuclar[secim - 1][0]) + " eklendi.\nAna menüye geri dönülüyor...\n")
                                Anasayfa(username)  # Ana menüye geri dönülüyor
                            else:
                                kullanicilar[username][1][str(sonuclar[secim - 1][0])] = [miktar, int(sonuclar[secim - 1][1])]  # Kullanıcının sepetine sectimiz miktar kadar o üründen ekliyoruz (örn: sepet[urunadi] = [miktar,fiyat])
                                print("Sepetinize " + str(sonuclar[secim - 1][0]) + " eklendi.\nAna menüye geri dönülüyor...\n")
                                Anasayfa(username)  # Ana menüye geri dönülüyor
                            durum2 = False  # Secim döngüsünü sonlandırıyoruz
                durum = False  # En üst secim döngüsünü sonlandırıyoruz

def Anasayfa(username):
    print(
        "Hoşgeldiniz " + username + "! Lütfen ilgili menü numarasını girerek aşağıdaki seçeneklerden birini seçin.")  # Hoşgeldiniz metni
    secim = int(input(
        "Lütfen aşağıdaki hizmetlerden birini seçin:\n1. Ürün ara\n2. Sepete git\n3. Satın al\n4. Oturum Kapat\n5. Çıkış yap\n\nSeçiminiz:"))  # Secim inputumuzu int olarak alıyoruz
    if (secim == 1):  # Secimlere göre yönlendirme icin if-elif-else kullandık
        UrunAra(username)  # ÜrünAra metodu
    elif (secim == 2):
        SepeteGit(username)  # SepeteGit metodu
    elif (secim == 3):
        SatinAl(username)  # SatinAl metodu
    elif (secim == 4):
        print("Oturum sona erdi!")
        GirisYap()  # GirisYap metodu
    elif (secim == 5):
        print("Uygulamadan çıkış yapılıyor...")
        exit()  # Uygulamadan cıkıs yapmak icin kullandığımız sistem metodu
    else:
        print("Yaptığınız secimle eşleşen bir sayfa bulunmamakta. Tekrardan yönlendiriliyorsunuz...")
        Anasayfa(username)  # Anasayfaya yönlendiriyoruz

def GirisYap():  # Giriş yap metodumuz
    print("**** İstinye Online Market’e Hoşgeldiniz ****\nLütfen kullanıcı kimlik bilgilerinizi sağlayarak giriş yapın:\n")
    durum = True
    while (durum):  # Kullanıcıdan doğru kullanıcı adı ve sifreyi alana kadar girmesini isteyen while döngüsü
        kullanici_adi = input("Kullanıcı adı:")  # Kullanıcı adı girisi
        sifre = input("Şifre:")  # Kullanıcı adı girisi
        if (kullanici_adi in kullanicilar.keys() and sifre == kullanicilar[kullanici_adi][0]):  # Eğer girdiğimiz kullanıcı adı ve sifre kullanicilar dictionarymizde varsa döngüyü bitirir ve kullanıcıyla beraber anasayfaya yönlendirir.
            durum = False
        else:
            print("Kullanıcı adınız ve / veya şifreniz doğru değil. Lütfen tekrar deneyin!")  # Yanlışsa mesaj verdirip döngüye devam eder
            continue
    print("Başarıyla giriş yapıldı!")
    Anasayfa(kullanici_adi)  # Anasafaya yönlendiriyoruz
GirisYap()  # Build metodumuz. Başlangıc icin ilk GirisYap metodunu cağırıyoruz.