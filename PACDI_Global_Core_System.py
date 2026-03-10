import datetime

class PACDIGlobal:
    def __init__(self, bolge, hedef_kitle, kullanici_adi):
        self.bolge = bolge
        self.hedef_kitle = hedef_kitle
        self.kullanici_adi = kullanici_adi
        self.ekonomi = {
            "TR": {"birim": "TL", "asgari_ucret": 17002},
            "EU": {"birim": "€", "asgari_ucret": 2100}
        }

    def giris_animasyonu_tetikle(self):
        """Açılış Şöleni: Ney ve Pusula"""
        return {
            "gorsel": "Dönen Gümüş Pusula 🧭",
            "ses": "Huzurlu Ney Tınısı",
            "mesaj": "Pusulanız Onura Ayarlanıyor..."
        }

    def gunun_pusulasi_motoru(self):
        """Günlük Takvim Yaprağı Mesajları"""
        veriler = {
            "Genç": {"mesaj": "Kendi yolunu çizmezsen, başkasının haritasında figüran olursun.", "ses": "Piyano"},
            "Kıdemli": {"mesaj": "Sevginin dili evrenseldir; maya sağlamsa ruh yorulmaz. Sen değerlisin.", "ses": "Ney"}
        }
        return veriler[self.hedef_kitle]

    def pdf_rapor_olustur(self, puan, potansiyel_maas):
        """Refah Analizi ve Resmi PDF Metni"""
        ucret = self.ekonomi[self.bolge]["asgari_ucret"]
        katsayi = round(potansiyel_maas / ucret, 2)
        return {
            "baslik": f"PACDI GLOBAL - {self.hedef_kitle.upper()} ONUR RAPORU",
            "kullanici": self.kullanici_adi,
            "refah_seviyesi": f"{katsayi}x Asgari Ücret",
            "muhur": "PACDI GLOBAL - MENŞEİ: ONUR"
        }

    def kariyer_projeksiyonu(self, meslek, baslangic_katsayisi):
        """5 ve 10 Yıllık Gelecek Vizyonu"""
        oranlar = {"Yazılım": 1.4, "Sağlık": 1.2, "Zanaat": 1.3}
        oran = oranlar.get(meslek, 1.1)
        bes_yil = round(baslangic_katsayisi * (oran ** 5), 1)
        on_yil = round(baslangic_katsayisi * (oran ** 10), 1)
        return {"5_yil": f"{bes_yil}x", "10_yil": f"{on_yil}x"}

    def sesli_yoldas_diyaloglari(self, durum="Yalnizlik"):
        """Call Center İhtiyacını Bitiren Şefkatli Sesler"""
        diyaloglar = {
            "Yalnizlik": f"Sesimi duyduğuna göre artık yalnız değilsin {self.kullanici_adi}. Ben buradayım.",
            "Basari": "Bugün bir adım daha attın, seninle gurur duyuyorum.",
            "Huzur": "Gözlerini kapat ve sadece nefes al. Pusulan seni huzura götürecek."
        }
        return diyaloglar.get(durum, diyaloglar["Yalnizlik"])

    def altin_muhurlu_sertifika_mantigi(self):
        """Sosyal Medya İçin Paylaşılabilir Onur Belgesi"""
        return {
            "cerceve": "Altın Yaldızlı Kenarlar",
            "baslik": "PACDI ONUR SERTİFİKASI",
            "onay": f"Sayın {self.kullanici_adi} onuruyla tescillenmiştir.",
            "muhur": "Gümüş Pusula & Menşei: Onur"
        }

# --- SİSTEM TESTİ ---
if __name__ == "__main__":
    pusula = PACDIGlobal("TR", "Genç", "Ali Yılmaz")
    print(f"Sistem Hazır: {pusula.giris_animasyonu_tetikle()['mesaj']}")
    print(f"Sesli Yoldaş: {pusula.sesli_yoldas_diyaloglari('Yalnizlik')}")
