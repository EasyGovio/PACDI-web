# =================================================================
# PROJE: PACDI GLOBAL - ECOSYSTEM v10.2 (Hatasız Tam Gövde)
# İÇERİK: PusulaPro, EasyGov, Karargah, Tam Soru Bankası
# =================================================================

import datetime

class PACDI_Global_Ecosystem:
    def __init__(self, kullanici_adi, bolge="EU", dil="Almanca", partner="Merkez"):
        self.kullanici = kullanici_adi
        self.bolge = bolge
        self.dil = dil
        self.partner = partner
        self.onaylar = {"TUV": False, "Hukuk": False, "Sunucu": False}

    def soru_bankasi_getir(self):
        """PusulaPro & KompassPro için mizaç ve yetenek odaklı 20 soru."""
        return [
            "1. Karmaşık problemleri analiz etmekten hoşlanır mısın?",
            "2. İnsanlara yardım etmek senin için bir öncelik midir?",
            "3. Rutin işler yerine sürekli değişen ortamları mı seversin?",
            "4. Liderlik etmek mi, uzman ekip üyesi olmak mı?",
            "5. Sayılar ve verilerle çalışmak sana güven verir mi?",
            "6. Sanatsal ve yaratıcı üretimler yapmayı sever misin?",
            "7. Teknoloji ve dijital araçları kullanma becerin nasıldır?",
            "8. Fiziksel güç gerektiren işlerde çalışabilir misin?",
            "9. Planlı ve düzenli bir çalışma takvimi mi istersin?",
            "10. İkna kabiliyetin ve iletişim becerilerin yüksek midir?",
            "11. Risk almaktan kaçınır mısın, yoksa fırsat mı görürsün?",
            "12. Detaylara odaklanmak seni yorar mı?",
            "13. Sosyal statü mü, yoksa iş tatmini mi daha önemli?",
            "14. Yabancı dillerde kendini ifade etmekte zorlanır mısın?",
            "15. Doğada ve açık havada çalışmak seni mutlu eder mi?",
            "16. Takım çalışması mı, bireysel çalışma mı?",
            "17. Gelecekte kendi işini kurma hayalin var mı?",
            "18. Problem anında soğukkanlılığını koruyabilir misin?",
            "19. El becerisi ve teknik tamirat işlerinde nasılsın?",
            "20. Asgari ücretin kaç katı bir gelir seni tatmin eder? (Refah Hedefi)"
        ]

    def kariyer_pusulasi_uret(self, cevap_puanlari, refah_katsayisi):
        """Alınan cevaplara göre rapor hazırlar."""
        asgari = 2100 if self.bolge == "EU" else 17002
        birim = "€" if self.bolge == "EU" else "₺"
        tahmini_gelir = asgari * refah_katsayisi
        
        return {
            "Kullanici": self.kullanici,
            "Analiz": "Kariyer rotanız yeteneklerinizle senkronize edildi.",
            "Refah_Hedefi": f"{tahmini_gelir} {birim}",
            "Durum": "Mühürlü Rapor Hazır."
        }

    def karargah_finans_paneli(self, toplam_gelir):
        """Finansal lojistik takip paneli."""
        paylar = {"Lojistik": toplam_gelir * 0.40, "ArGe": toplam_gelir * 0.25}
        return {"Dagitim": paylar, "Mesaj": "Onurla biriktiriyoruz."}

    def vicdan_muhuru(self):
        return f"[{self.partner}] MENŞEİ: ONUR, SEVGİ VE SABIR | {datetime.datetime.now().strftime('%d/%m/%Y')}"

# --- TEST ---
if __name__ == "__main__":
    app = PACDI_Global_Ecosystem("Genç Vizyoner", "TR", "Türkçe")
    for soru in app.soru_bankasi_getir(): print(soru)
    print(app.kariyer_pusulasi_uret(None, 3.5))
    print(app.vicdan_muhuru())
