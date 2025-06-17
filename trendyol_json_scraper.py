import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

# — Selenium & ChromeDriver ayarları —
options = Options()
# options.add_argument("--headless")  # Görünmeden çalıştırmak istersen bu satırı aç
options.add_argument("--disable-blink-features=AutomationControlled")
service = Service("C:/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

# — Trendyol “airfryer” arama sayfasını aç —
search_url = "https://www.trendyol.com/sr?q=airfryer"
driver.get(search_url)
time.sleep(7)  # Sayfanın tam yüklenmesini bekle

# — Ürün kartlarını seç —
cards = driver.find_elements(By.CSS_SELECTOR, "div.p-card-wrppr")
print(f" Bulunan ürün kartı sayısı: {len(cards)}")

data = []
for card in cards:
    try:
        # Ürün başlığını al
        desc = card.find_element(By.CSS_SELECTOR, "div.product-desc-sub-text")
        name = desc.get_attribute("title").strip().replace("\n", " ")
        nl = name.lower()
        # Filtre: “kağıt” veya “aksesuar” içerenleri atla
        if any(keyword in nl for keyword in ["kağı", "aksesuar"]):
            continue
        # Sadece “airfryer” veya “fritöz” içerenler
        if not ("airfryer" in nl or "fritöz" in nl):
            continue

        # Fiyatı al
        try:
            price_txt = card.find_element(By.CSS_SELECTOR, "div.price-item.discounted").text
        except:
            price_txt = card.find_element(By.CSS_SELECTOR, "div.price-item").text
        price = float(price_txt.replace("TL", "").replace(".", "").replace(",", ".").strip())

        data.append([name, price])

    except Exception:
        continue

driver.quit()

# — Verileri DataFrame’e kaydet ve CSV’ye yaz —
df = pd.DataFrame(data, columns=["Ürün Adı", "Fiyat (TL)"])
df.to_csv("trendyol_airfryer.csv", index=False)
print(" Veriler kaydedildi: trendyol_airfryer.csv")

# — En ucuz 5 ürünü sadece isim ve fiyat ile düzenli şekilde yazdır —
print("\nEn Ucuz 5 Ürün:")
for name, price in df.sort_values("Fiyat (TL)").head(5).values:
    print(f"- {name} — {price:.2f} TL")
