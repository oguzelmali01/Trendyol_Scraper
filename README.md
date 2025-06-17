# Trendyol Scraper - Airfryer Fiyat Toplayıcı

Bu proje, Python ve Selenium kullanarak Trendyol'da "airfryer" anahtar kelimesiyle arama yapar, ürün isimlerini ve fiyatlarını toplar ve `trendyol_airfryer.csv` adlı bir CSV dosyasına kaydeder.

## 🚀 Özellikler

- Trendyol üzerinde **airfryer** veya **fritöz** içeren ürünleri listeler
- "kağıt" veya "aksesuar" içeren ürünleri **filtreler**
- Ürünlerin adını ve fiyatını çeker
- En ucuz 5 ürünü terminalde listeler
- Sonuçları `trendyol_airfryer.csv` dosyasına yazar

## 🛠️ Kullanılan Teknolojiler

- Python
- Selenium (Web Scraping için)
- pandas (CSV oluşturmak ve sıralama işlemi için)

## ⚙️ Gereksinimler

- Python 3.x
- [Google ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)
- Aşağıdaki Python kütüphaneleri:
  ```bash
  pip install selenium pandas
