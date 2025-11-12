# Şifreli Not Defteri 🔒📝

Basit bir Python uygulaması: kullanıcı tarafından belirlenen şifre ile korunan bir not defteri.  
Doğru şifre girildiğinde notları görüntüleyebilir ve yeni notlar ekleyebilirsiniz.
---
## Özellikler
- İlk çalıştırmada şifre belirleme (metin/parola)
- Parola ile doğrulama (3 deneme hakkı)
- Not ekleme (dosyaya ekleme)
- Notları görüntüleme
- Notlar UTF-8 formatında `sifreli_not.txt` dosyasında saklanır
---
## Gereksinimler
- Python 3.x
---
## Kullanım
1. Depoyu klonlayın:
bash
git clone https://github.com/mucahit-source/sifreli-not-defteri
cd sifreli-not-defteri
Programı çalıştırın:

bash
Kodu kopyala
python sifreli_not_defteri.py
İlk çalıştırmada sizden bir şifre belirlemeniz istenir. Sonrasında aynı şifreyi girerek notlarınıza ulaşabilirsiniz.

---

## Güvenlik Notu

Bu uygulama üretim/gerçek hayatta güçlü bir güvenlik sağlamaz. Parolalar lokal olarak hashlenmiş şekilde saklansa da bu bir tam güvenlik çözümü değildir. Gerçek gizlilik gereksinimleri için profesyonel şifreleme ve güvenli anahtar yönetimi gerekir.
---
## Geliştirme Fikirleri

Notları AES gibi bir algoritma ile şifrelemek

Parolayı güvenli bir şekilde (salt + hash) saklamak

Basit GUI (Tkinter) ile görsel arayüz

Not arama/silme/güncelleme fonksiyonları
