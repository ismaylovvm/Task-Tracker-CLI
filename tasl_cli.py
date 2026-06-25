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
    






