import sys
import json
import os

# Verilerin tutulacağı dosyanın adı
DOSYA_ADI = "tasks.json"

def gorevleri_getir():
    # Dosya klasörde yoksa boş bir liste (array) döndür
    if not os.path.exists(DOSYA_ADI):
        return []
    
    # Dosya varsa okuma ("r" - read) modunda aç ve veriyi Python listesine çevir
    with open(DOSYA_ADI, "r", encoding="utf-8") as dosya:
        return json.load(dosya)

def gorevleri_kaydet(gorevler):
    # Verileri yazma ("w" - write) modunda aç ve JSON olarak dosyaya kaydet
    with open(DOSYA_ADI, "w", encoding="utf-8") as dosya:
        json.dump(gorevler, dosya, indent=4)

# Şimdilik sadece çalışıp çalışmadığını test ediyoruz
if __name__ == "__main__":
    # Sistemdeki argümanları tekrar alalım
    argumanlar = sys.argv
    
    # Dosyadaki mevcut görevleri çek
    mevcut_gorevler = gorevleri_getir()
    print("Sistemde kayitli görevler:", mevcut_gorevler)