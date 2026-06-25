import datetime
import sys
import file_operations

# girilen argüman kontrol

argümanlar = sys.argv 


if len(argümanlar) < 2:
    print("Lutfen formata uygun komut giriniz  '<dosya_adi> <komut> <görev>' ")
    sys.exit(1)

print("girilen argümanlar",argümanlar)



# Görev Sınıf yaspısı


class Task:

    def __init__(self,id,description):
        
        self.id = id
        self.description = description
        self.status = "todo"

        anlik_zaman = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.createdAt = anlik_zaman
        self.updatedAt = anlik_zaman

    def to_dict(self):

        return {
            "id":self.id,
            "description":self.description,
            "status":self.status,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
        }
    



# komut kontrolu

if argümanlar[1] == "add":
    
    gorev_metni = argümanlar[2]

    #Yeni görevleri eklemek için mevcut görev listesini getirme

    mevcut_gorevler = file_operations.gorevleri_getir()

    #Uygun id bulmak için görev listesinde son kalınan yer

    id = len(mevcut_gorevler) + 1

    # Görevi json formatında kullanmak için yapı

    yeni_gorev_nesnesi = Task(id,gorev_metni)
    yeni_gorev = yeni_gorev_nesnesi.to_dict()

    # Görevi mevcut görevlerin üzerine yaz

    mevcut_gorevler.append(yeni_gorev)

    # Görev listesine ekle

    file_operations.gorevleri_kaydet(mevcut_gorevler)






elif argümanlar[1] == "list":

    # Farklı durumlara göre listeleme

    if len(argümanlar) < 3:
        print("Lutfen komutlari dogru giriniz")
        sys.exit(1)


    mevcut_gorevler = file_operations.gorevleri_getir()


    if argümanlar[2] == "done":

        for gorev in mevcut_gorevler:
            if gorev["status"] == "done":
                print(f"ID: {gorev['id']} | Durum: {gorev['status']} | Görev: {gorev['description']}")

    

    elif argümanlar[2] == "todo":
    
        for gorev in mevcut_gorevler:
            if gorev["status"] == "todo":
                print(f"ID: {gorev['id']} | Durum: {gorev['status']} | Görev: {gorev['description']}")

    
    elif argümanlar[2] == "in-progress":

        for gorev in mevcut_gorevler:
            if gorev["status"] == "in-progress":
                print(f"ID: {gorev['id']} | Durum: {gorev['status']} | Görev: {gorev['description']}")


    else:

        for gorev in mevcut_gorevler:
                print(f"ID: {gorev['id']} | Durum: {gorev['status']} | Görev: {gorev['description']}")

    






       


elif argümanlar[1] == "update":
    print("güncelleme işlemi yapilacak")

    
elif argümanlar[1] == "delete":
    print("Silme işlemi yapilacak")

else:
    print("Bilinmeyen komut girildi")

    






