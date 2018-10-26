# ad ve soyad şeklinde 2 string oluşturuyorum.

ad = 'Burak Celal'

soyad = "AKYÜZ"

print("Kullanıcının adı {} ve soyadı {} ".format(ad, soyad))

# string atamadaki hatalı kullanım

# hatalı = "Hatalı String Kullanımı'


# string kullanımındaki indexlemeyi anlamak için ad ve soyad değişkenlerinin ilk harflerini yazdıralım.

ad_ilk_harf = ad[0]

soyad_ilk_harf = soyad[0]

print("Adın ilk harfi : {}".format(ad_ilk_harf))

print("Soyadın ilk harfi : {}".format(soyad_ilk_harf))

# string kullanımında metin boyunu bulma len(string_adı) ile olur.

ad_metninin_uzunluğu = len(ad)

soyad_metninin_uzunluğu = len(soyad)

print("Ad değişkeninin boyu : {}".format(ad_metninin_uzunluğu))

print("Soyad değişkeninin boyu : {}".format(soyad_metninin_uzunluğu))

# ad değişkenini ilk_ad ve ikinci_ad olarak 2 parçaya ayıralım.

ilk_ad = ad[0: 5: 1]

ikinci_ad = ad[5: len(ad)+1: 1]

print("Kullanıcının ilk adı : {}".format(ilk_ad))

print("Kullanıcının ikinci adı : {}".format(ikinci_ad))

# Pythonda iki çeşit birleştirme işlemi vardır. İlki + operatörü ile birleştirmedir.

tam_ad = ad + soyad

print("Kullanıcının adı ve soyadı : {} ".format(tam_ad))

# Diğer kullanım ise * ile tekrarlamadır.

tam_ad_3 = tam_ad * 3

print("Kullanıcının adı ve soyadının 3 kez tekrarlanmış hâli : {}".format(tam_ad_3))




