# =================================================================
# PROJE: PACDI GLOBAL - ONUR VE REFAH REHBERİ (v3.0)
# MODÜLLER: PusulaPro (Gençlik) & Silver Compass (Kıdemli Dostlar)
# ÖZELLİKLER: Refah Analizi, PDF Motoru, Sesli Yoldaş, Sosyal Mühür
# =================================================================

import datetime

class PACDIGlobal:
    def __init__(self, bolge, hedef_kitle, kullanici_adi):
        self.bolge = bolge  # "TR" veya "EU"
        self.hedef_kitle = hedef_kitle  # "Genç" veya "Kıdemli"
        self.kullanici_adi = kullanici_adi
        
        # 1. Ekonomik Veri Bankası (Asgari Ücret Katsayıları)
        self.ekonomi = {
            "TR": {"birim": "TL", "asgari_ucret": 17002, "pro": "149 TL", "vip": "499 TL"},
            "EU": {"birim": "€", "asgari_ucret": 2100, "pro": "9.90 €", "vip": "44.90 €"}
        }

    def gunun_pusulasi_motoru(self):
        """Takvim Yaprağı Masumiyetinde Günlük Rehberlik"""
        veriler = {
            "Genç": {
                "mesaj": "Kendi yolunu çizmezsen, başkasının haritasında figüran olursun.",
                "ses": "Dinamik Piyano", "efekt": "Yükselen Işıklar"
            },
            "Kıdemli": {
                "mesaj": "Sevginin dili evrenseldir; maya sağlamsa ruh yorulmaz. Sen değerlisin.",
                "ses": "Huzurlu Ney ve Su", "efekt": "Eski Takvim Yaprağı"
            }
        }
        return veriler[self.hedef_kitle]

    def pdf_rapor_olustur(self, puan, potansiyel_maas):
        """Resmi PDF Raporu ve Sertifika Metinleri (Eksiksiz ve Yazım Kurallarına Uygun)"""
        ucret_verisi = self.ekonomi[self.bolge]
        katsayi = potansiyel_maas / ucret_verisi["asgari_ucret"]
        
        tavsiye = (
            "Analiz sonuçlarınız, onur ve azimle birleştiğinde topluma yön verecek bir güç taşımaktadır."
            if self.hedef_kitle == "Genç" else
            "Bu rapor, yılların biriktirdiği bilgeliğin bir onur nişanesidir. Yalnız değilsiniz."
        )

        return {
            "baslik": f"PACDI GLOBAL - {self.hedef_kitle.upper()} ONUR RAPORU",
            "refah_seviyesi": f"{round(katsayi, 2)} x Asgari Ücret",
            "tavsiye": tavsiye,
            "muhur": "PACDI GLOBAL - MENŞEİ: ONUR"
        }

    def grafik_verisi_olustur(self, katsayi):
        """Rapor İçin Görsel Kadran Mantığı"""
        if self.hedef_kitle == "Genç":
            durum = "Refah İçinde" if katsayi >= 2.5 else "Gelişmekte"
            return f"Refah Kadranı: {katsayi}x | Durum: {durum}"
        return "Huzur Kadranı: %100 Saf Sevgi ve Onur"

    def sesli_yoldas_metni(self, zaman="Sabah"):
        """Call Center İhtiyacını Bitiren Şefkatli Ses Modülü"""
        metinler = {
            "Sabah": f"Günaydın {self.kullanici_adi}. Yeni bir gün, yeni bir umut. Seninle olmak güzel.",
            "Destek": "Buradayım, seni duyuyorum. Pusulan daima senin yanında."
        }
        return metinler.get(zaman, metinler["Sabah"])

    def sosyal_muhur_hazirla(self):
        """Mühürlü ve Paylaşılabilir Takvim Yaprağı Görseli"""
        return {
            "ikon": "Gümüş Pusula 🧭",
            "metin": self.gunun_pusulasi_motoru()["mesaj"],
            "muhur": "PACDI GLOBAL - MENŞEİ: ONUR"
        }

# --- SİSTEM TESTİ ---
if __name__ == "__main__":
    pusula = PACDIGlobal("TR", "Genç", "Ali Yılmaz")
    print(f"PACDI Core v3.0 Aktif. Kullanıcı: {pusula.kullanici_adi}")
