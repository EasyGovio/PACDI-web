# =================================================================
# PROJE: PACDI GLOBAL - BÜTÜNLEŞİK ÇEKİRDEK SİSTEM (v2.0)
# İÇERİK: Kariyer Analizi, Refah Katsayısı, Takvim Yaprağı, PDF Motoru
# =================================================================

import datetime
import json

class PACDIGlobal:
    def __init__(self, bolge, hedef_kitle, kullanıcı_adı):
        self.bolge = bolge  # "TR" veya "EU"
        self.hedef_kitle = hedef_kitle  # "Genç" veya "Kıdemli"
        self.kullanıcı_adı = kullanıcı_adı
        
        # Dinamik Veri Kaynakları
        self.ekonomi = {
            "TR": {"birim": "TL", "asgari_ucret": 17002, "pro_bedel": "149 TL", "vip_bedel": "499 TL"},
            "EU": {"birim": "€", "asgari_ucret": 2100, "pro_bedel": "9.90 €", "vip_bedel": "44.90 €"}
        }

    def gunun_pusulasi_motoru(self):
        """Karma Deneyim: Görsel, İşitsel ve Metinsel Tetikleyici"""
        takvim_verisi = {
            "Genç": {
                "mesaj": "Kendi yolunu çizmezsen, başkasının haritasında figüran olursun.",
                "ses_tınısı": "Dinamik/Motivasyonel Piyano",
                "görsel_efekt": "Yükselen Işıklar"
            },
            "Kıdemli": {
                "mesaj": "Sevginin dili evrenseldir; maya sağlamsa, ruh yorulmaz. Sen değerlisin.",
                "ses_tınısı": "Huzurlu Ney ve Su Sesi",
                "görsel_efekt": "Eski Takvim Yaprağı Düşüşü"
            }
        }
        return takvim_verisi[self.hedef_kitle]

    def pdf_rapor_olustur(self, puan, potansiyel_maas):
        """PDF Motoru: Kariyer Raporu ve Sertifika Altyapısı"""
        ucret = self.ekonomi[self.bolge]
        katsayi = potansiyel_maas / ucret["asgari_ucret"]
        
        # PDF İçerik Hazırlığı
        rapor_icerigi = {
            "baslik": f"PACDI GLOBAL - {self.hedef_kitle.upper()} ANALİZ RAPORU",
            "kullanıcı": self.kullanıcı_adı,
            "refah_seviyesi": f"{round(katsayi, 2)} x Asgari Ücret",
            "durum": "Sertifika Onaylandı" if puan > 70 else "Gelişim Önerilir",
            "mühür": "PACDI GLOBAL - ONUR MÜHRÜ"
        }
        return rapor_icerigi

    def ozel_gun_kontrol(self, dogum_gunu=False):
        """Kutlama Modülü: Konfeti ve Çiçek Tetikleyicisi"""
        if dogum_gunu:
            return "🎉 KONFETİ PATLATMA: İyi ki doğdun! PACDI mührüyle onurlandırıldın."
        return "Bugün standart bir onur günü."

# --- SİSTEMİ ÇALIŞTIRMA VE TEST ---

# Örnek 1: Türkiye'deki Genç (PusulaPro)
ali = PACDIGlobal("TR", "Genç", "Ali Yılmaz")
rapor = ali.pdf_rapor_olustur(85, 60000)
print(f"--- {ali.kullanıcı_adı} İçin PDF Hazırlanıyor ---")
print(f"Rapor Özeti: {rapor['refah_seviyesi']} refah katsayısı ile yolun açık.")
print(f"Mesaj: {ali.gunun_pusulasi_motoru()['mesaj']}")

print("\n" + "="*40 + "\n")

# Örnek 2: Avrupa'daki Kıdemli Dostumuz (Silver Compass)
hans = PACDIGlobal("EU", "Kıdemli", "Hans Müller")
print(f"--- {hans.kullanıcı_adı} İçin Sabah Karşılaması ---")
print(f"Tetikleyici: {hans.gunun_pusulasi_motoru()['ses_tınısı']} çalıyor...")
print(f"Bilgelik: {hans.gunun_pusulasi_motoru()['mesaj']}")
print(hans.ozel_gun_kontrol(dogum_gunu=True))
