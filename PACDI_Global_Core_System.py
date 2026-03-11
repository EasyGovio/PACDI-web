# =================================================================
# PROJE: PACDI GLOBAL - CHAMPION TEAM EDITION
# VERSION: 10.6 (Karakter, Takım Ruhu & Küresel Elçiler)
# =================================================================

import datetime

class PACDI_Global_Ecosystem:
    def __init__(self, kullanici_adi, bolge="EU", dil="Türkçe"):
        self.kullanici = kullanici_adi
        self.bolge = bolge
        self.dil = dil
        self.karargah_kumbara = 0
        self.onaylar = {"TUV": False, "Hukuk": False, "Sunucu": "Frankfurt"}

    def soru_bankasi_getir(self):
        """Karakter, İş Ahlakı ve Yeteneği ölçen pırlanta soru seti."""
        return [
            # --- Yetenek & Mizaç ---
            "1. Karmaşık problemleri analiz etmekten hoşlanır mısın?",
            "2. İnsanlara yardım etmek senin için bir öncelik midir?",
            "3. Sayılar ve verilerle çalışmak sana güven verir mi?",
            # --- İş Ahlakı & Göz Seviyesi İletişim (Yeni!) ---
            "4. Kimsenin görmediği bir teknik hatayı düzeltmek için vakit harcar mısın?",
            "5. Takım arkadaşın hatanı bulduğunda 'Teşekkür eder, beraber mi çözersin'?",
            "6. 'Dilim mükemmel değil ama işim kusursuz olmalı' vizyonuna katılıyor musun?",
            "7. Farklı bir milletten olan ustanla (Hans gibi) göz seviyesinde çalışabilir misin?",
            # --- İstek & Gelişim ---
            "8. Mesleği bilmiyor olsan da öğrenme hırsın ve disiplinin yüksek mi?",
            "9. İş saatinde orada olmak ve dakiklik senin için bir onur meselesi mi?",
            "10. Gelecekteki refah beklentin asgari ücretin kaç katı olmalı? (Katsayı)"
        ]

    def karakter_analiz_motoru(self, cevaplar):
        """Kullanıcının 'Şampiyon Takım' oyuncusu olup olmadığını puanlar."""
        # Burada cevaplara göre Takım Ruhu, Ahlak ve Teknik puan hesaplanır (Temsili)
        puan_ozeti = {
            "Takım_Ruhu": "Yüksek (Hans ile tam uyum)",
            "İş_Ahlakı": "Kusursuz (Onur Mührü)",
            "Öğrenme_İsteği": "Üst Seviye"
        }
        return puan_ozeti

    def mühürlü_rapor_olustur(self, katsayi, meslek):
        """Onur, Pelin ve Hans onaylı dijital rapor içeriği."""
        asgari = 2100 if self.bolge == "EU" else 17002
        birim = "€" if self.bolge == "EU" else "₺"
        
        return {
            "Giriş": f"Sayın {self.kullanici}, PACDI Ekosistemine Hoş Geldiniz.",
            "Analiz": f"Siz, {meslek} alanında bir 'Usta' adayı ve Şampiyon Takım oyuncususunuz.",
            "Refah_Hedefi": f"Aylık Hedef: {asgari * katsayi} {birim}",
            "Mesaj": "Dilin aksanı işin kalitesini bozmaz. Onurla kalın."
        }

    def vicdan_muhuru(self):
        tarih = datetime.datetime.now().strftime("%d/%m/%Y")
        return f"PACDI GLOBAL | [MENŞEİ: ONUR, SEVGİ VE SABIR] | {tarih}"

# --- SİSTEMİ ATEŞLE ---
if __name__ == "__main__":
    pacdi = PACDI_Global_Ecosystem("Onurlu Genç", "EU", "Almanca")
    print(pacdi.vicdan_muhuru())
    print("\n--- ANALİZ BAŞLIYOR ---")
    for s in pacdi.soru_bankasi_getir(): print(f"[?] {s}")
    
    analiz = pacdi.karakter_analiz_motoru(None)
    print(f"\nKarakter Özeti: {analiz}")
    print(pacdi.mühürlü_rapor_olustur(2.5, "Trockenbau Specialist"))
