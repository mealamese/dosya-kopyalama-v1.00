import sys, os, shutil  # gerekli modülleri dahil ediyoruz

class Copy():

    def copyfile(self):
        kaynak = input("Kaynak: ")  # kaynak dizinin yolunu istiyoruz
        hedef = input("Hedef: ")    # hedef dizinin yolunu istiyoruz

        cevap = input("Kopyalanacak dizinde yeni klasör oluşturulmasını ister misiniz? (E/H) : ")   # kopyanacak dosyaların yeni bir klasöre mi mevcut bir klasöre mi kopyalanacağını belirliyoruz

        if(cevap == "E" or cevap == "e"):
            yeni_dosya = input("Oluşturmak istediğiniz klasör ismi: ")  # oluşturduğumuz klasöre isim veriyoruz
            if not os.path.isdir(str(hedef + "/" + yeni_dosya)):
                os.mkdir(str(hedef + "/" + yeni_dosya)) # klasörü oluşturuyoruz
            hedef = hedef + "/" + yeni_dosya    # yeni klasör oluştuğu için hedef dizini tekrar ayarlıyoruz

        dosya_uzantisi = input("Kopyalamak istediğiniz dosya uzantısını giriniz: ").lower() # kopyalanmasını istediğimiz dosya uzantısını yazıyoruz

        for yol, klasor, dosya in os.walk(kaynak):  # kaynak dizinde geziniyoruz
            for i in dosya:
                if(i.endswith("." + dosya_uzantisi)):
                    shutil.copy(os.sep.join([yol, i]) , hedef)  # belirttiğimiz dosya uzantısında dosya varsa bu dosyayı hedef dizine kopyalıyoruz

kopyala = Copy()    # Copy sınıfından kopyala objesi oluşturuyoruz
kopyala.copyfile()  # kopyala objesinin copyfile() fonksiyonunu çağırıyoruz
