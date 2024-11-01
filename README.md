# Türk Kimlik Kartı OCR Okuyucu

Bu proje, Türk kimlik kartlarından T.C. kimlik numarası, ad ve soyadı gibi bilgileri optik karakter tanıma (OCR) teknolojisi kullanarak okuyabilen bir uygulama geliştirmeyi amaçlamaktadır. Uygulama, kullanıcıların kimlik kartı fotoğraflarını yükleyerek bu bilgileri otomatik olarak ayıklamalarını sağlar.

## Proje Hedefleri

- Eski ve yeni Türk kimlik kartlarından bilgileri tanımlamak.
- PaddleOCR kütüphanesini kullanarak Türkçe dil desteği ile metinleri doğru bir şekilde okumak.
- Kullanıcı dostu bir arayüz ile fotoğraf yükleme ve sonuçları gösterme.

## Kullanılan Teknolojiler

- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR): OCR işlemleri için kullanılan Python kütüphanesi.
- [Streamlit](https://streamlit.io/): Web tabanlı arayüz geliştirmek için kullanılan Python kütüphanesi.
- Python 3.7 ve üzeri.

## Kurulum

Projenin çalışması için gerekli olan bağımlılıkları yüklemek için aşağıdaki adımları izleyin:

1. Bu repoyu klonlayın:
   ```bash
   git clone https://github.com/kullanici_adiniz/turk-kimlik-ocr.git
   cd turk-kimlik-ocr
