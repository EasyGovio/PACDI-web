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
    def ekonomi_verisini_guncelle(self, yeni_asgari_ucret):
        """Asgari ücret değiştiğinde sistemin kalbini günceller."""
        self.ekonomi[self.bolge]["asgari_ucret"] = yeni_asgari_ucret
        return f"Sistem Güncellendi: Yeni Temel Ücret {yeni_asgari_ucret} {self.ekonomi[self.bolge]['birim']}"

    def ayarlar_ozeti_getir(self):
        """Kullanıcının tercih ettiği sistem ayarları paneli."""
        return {
            "Aktif Bölge": self.bolge,
            "Hedef Kitle": self.hedef_kitle,
            "Mevcut Birim": self.ekonomi[self.bolge]["birim"],
            "Mühür Durumu": "Aktif - Onur Tescilli"
        }
    def tasarim_sablonu_olustur(self):
        """Rapor ve Sertifikalar için Altın Oran görsel yerleşimi."""
        return {
            "kağıt_dokusu": "Saman Sarısı (#FFFDF5)",
            "kenar_boşluğu": "40px (Geniş ve Ferah)",
            "pusula_konumu": "Üst Orta (Odak Noktası)",
            "mühür_açısı": "15 Derece Sağ Eğik (Islak İmza Hissi)",
            "yazı_tipi": "Serif (Klasik ve Güven Verici)"
        }
    def tasarim_sablonu_olustur(self):
        """Rapor ve Sertifikalar için Altın Oran görsel yerleşimi."""
        return {
            "kağıt_dokusu": "Saman Sarısı (#FFFDF5)",
            "kenar_boşluğu": "40px (Geniş ve Ferah)",
            "pusula_konumu": "Üst Orta (Odak Noktası)",
            "mühür_açısı": "15 Derece Sağ Eğik (Islak İmza Hissi)",
            "yazı_tipi": "Serif (Klasik ve Güven Verici)"
        }
    def yetenek_rehberi_analizi(self, cevaplar):
        """10 soruluk analize göre kariyer pusulası sonucu üretir."""
        # cevaplar: [0, 1, 0, 1...] şeklinde bir liste
        toplam_puan = sum(cevaplar)
        
        if toplam_puan > 8:
            sonuc = "Yüksek Teknoloji ve Liderlik (Geleceğin Mimarı)"
        elif toplam_puan > 5:
            sonuc = "Yaratıcı Sanatlar ve Tasarım (Duyguların Ustası)"
        else:
            sonuc = "Sosyal Girişimcilik ve Eğitim (Toplumun Kalbi)"
            
        return {
            "kariyer_pusulasi": sonuc,
            "analiz_notu": f"Sayın {self.kullanici_adi}, potansiyeliniz {sonuc} alanında parlıyor."
        }
      def tesekkur_ritueli_kaydet(self, maddeler):
        """Kullanıcının o günkü manevi şükür notlarını mühürler."""
        # maddeler: ["Sağlıklıyım", "Ailemle vakit geçirdim", "Yeni bir şey öğrendim"]
        tarih = datetime.datetime.now().strftime("%d/%m/%Y")
        
        return {
            "tarih": tarih,
            "rituel_notu": f"Bugün {len(maddeler)} güzelliği mühürledin.",
            "liste": maddeler,
            "muhur": "PACDI GLOBAL - MANEVİ HUZUR TESCİLLİ"
        }
  

# --- SİSTEM TESTİ ---
if __name__ == "__main__":
    pusula = PACDIGlobal("TR", "Genç", "Ali Yılmaz")
    print(f"Sistem Hazır: {pusula.giris_animasyonu_tetikle()['mesaj']}")
    print(f"Sesli Yoldaş: {pusula.sesli_yoldas_diyaloglari('Yalnizlik')}")
