import datetime

class PACDIGlobal:
    def __init__(self, bolge, hedef_kitle, kullanici_adi):
        self.bolge = bolge  # "TR" veya "EU"
        self.hedef_kitle = hedef_kitle  # "Genç" veya "Kıdemli"
        self.kullanici_adi = kullanici_adi
        
        # Ekonomik Veri Bankası ve Fiyatlandırma
        self.ekonomi = {
            "TR": {"birim": "TL", "asgari_ucret": 17002, "pro": "149 TL", "vip": "499 TL"},
            "EU": {"birim": "€", "asgari_ucret": 2100, "pro": "9.90 €", "vip": "44.90 €"}
        }

    def gunun_pusulasi_motoru(self):
        """Karma Deneyim: Takvim Yaprağı Mesajı ve Tetikleyiciler"""
        takvim_verisi = {
            "Genç": {
                "mesaj": "Kendi yolunu çizmezsen, başkasının haritasında figüran olursun.",
                "ses": "Dinamik Piyano", "efekt": "Yükselen Işıklar"
            },
            "Kıdemli": {
                "mesaj": "Sevginin dili evrenseldir; maya sağlamsa ruh yorulmaz. Sen değerlisin.",
                "ses": "Huzurlu Ney ve Su", "efekt": "Eski Takvim Yaprağı"
            }
        }
        return takvim_verisi[self.hedef_kitle]

    def pdf_rapor_olustur(self, puan, potansiyel_maas):
        """PDF Motoru: Refah Katsayısı ve Resmi Tavsiye Metinleri"""
        ucret = self.ekonomi[self.bolge]
        katsayi = potansiyel_maas / ucret["asgari_ucret"]
        
        # Resmi Tavsiye Metinleri (Eksiksiz ve Yazım Kurallarına Uygun)
        tavsiye = (
            "Analiz sonuçlarınız, onur ve azimle birleştiğinde topluma yön verecek bir güç taşımaktadır."
            if self.hedef_kitle == "Genç" else
            "Bu rapor, yılların biriktirdiği bilgeliğin bir onur nişanesidir. Yalnız değilsiniz."
        )

        rapor_icerigi = {
            "baslik": f"PACDI GLOBAL - {self.hedef_kitle.upper()} ANALİZ RAPORU",
            "kullanici": self.kullanici_adi,
            "refah_seviyesi": f"{round(katsayi, 2)} x Asgari Ücret",
            "tavsiye_notu": tavsiye,
            "muhur": "PACDI GLOBAL - MENŞEİ: ONUR"
        }
        return rapor_icerigi

    def sosyal_medya_karti_hazirla(self):
        """Mühürlü ve Paylaşılabilir Görsel Kart Şablonu"""
        mesaj = self.gunun_pusulasi_motoru()["mesaj"]
        return {
            "tasarim": "Mühürlü Takvim Yaprağı",
            "icerik": mesaj,
            "filigran": "PACDI Global - Onur Pusulası"
    def grafik_verisi_olustur(self, katsayi):
        """Raporun içindeki görsel kadranın konumunu belirler."""
        if self.hedef_kitle == "Genç":
            # Gençler için ekonomik refah analizi
            seviye = "Gelişmekte" if katsayi < 2 else "Refah İçinde"
            return f"Refah Kadranı: {katsayi}x | Durum: {seviye}"
        else:
            # Kıdemli dostlarımız için manevi huzur endeksi
            # Burada katsayıdan bağımsız olarak 'Sevgi' vurgusu yapıyoruz.
            return "Huzur Kadranı: %100 Saf Sevgi ve Onur"


# --- Uygulama Testi ---
if __name__ == "__main__":
    pusula = PACDIGlobal("TR", "Genç", "Ali Yılmaz")
    print(f"Mesaj: {pusula.gunun_pusulasi_motoru()['mesaj']}")
    print(f"Rapor: {pusula.pdf_rapor_olustur(85, 55000)['refah_seviyesi']}")
