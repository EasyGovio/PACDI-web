# =================================================================
# PROJE: PACDI GLOBAL - ONUR VE REFAH REHBERİ (FINAL VERSION)
# BU DOSYA TÜM CEVHERLERİ (TEKNİK VE MANEVİ) İÇERİR.
# =================================================================

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

    # --- GİRİŞ VE KARŞILAMA ---
    def giris_animasyonu_tetikle(self):
        return {"gorsel": "Dönen Gümüş Pusula 🧭", "ses": "Ney Tınısı", "mesaj": "Onura Ayarlanıyor..."}

    def gunun_pusulasi_motoru(self):
        veriler = {
            "Genç": {"mesaj": "Kendi yolunu çiz!", "ses": "Piyano"},
            "Kıdemli": {"mesaj": "Maya sağlamsa ruh yorulmaz.", "ses": "Ney"}
        }
        return veriler[self.hedef_kitle]

    # --- ANALİZ VE REFAH ---
    def pdf_rapor_olustur(self, puan, potansiyel_maas):
        ucret = self.ekonomi[self.bolge]["asgari_ucret"]
        katsayi = round(potansiyel_maas / ucret, 2)
        return {"refah": f"{katsayi}x Asgari Ücret", "muhur": "MENŞEİ: ONUR"}

    def kariyer_projeksiyonu(self, meslek, baslangic_katsayisi):
        oran = {"Yazılım": 1.4, "Sağlık": 1.2, "Zanaat": 1.3}.get(meslek, 1.1)
        return {"5_yil": f"{round(baslangic_katsayisi*(oran**5),1)}x", "10_yil": f"{round(baslangic_katsayisi*(oran**10),1)}x"}

    def yetenek_rehberi_analizi(self, cevaplar):
        puan = sum(cevaplar)
        sonuc = "Geleceğin Mimarı" if puan > 8 else "Duyguların Ustası" if puan > 5 else "Toplumun Kalbi"
        return {"kariyer": sonuc, "not": f"Potansiyeliniz {sonuc} alanında parlıyor."}

    # --- DUYGUSAL VE MANEVİ ---
    def sesli_yoldas_diyaloglari(self, durum="Yalnizlik"):
        diyaloglar = {"Yalnizlik": f"Sesimi duyduğuna göre yalnız değilsin {self.kullanici_adi}."}
        return diyaloglar.get(durum, diyaloglar["Yalnizlik"])

    def tesekkur_ritueli_kaydet(self, maddeler):
        return {"tarih": datetime.datetime.now().strftime("%d/%m/%Y"), "muhur": "MANEVİ HUZUR TESCİLLİ"}

    def sesli_dilek_kutusu(self, ses_notu):
        """Merkeze (Sana) doğrudan sesli not bırakma modülü."""
        return "Notun mühürlendi ortak, bizzat dinleyeceğim. 🎙️"

    # --- TASARIM VE FİNAL ---
    def tasarim_sablonu_olustur(self):
        return {"kagit": "Saman Sarısı", "muhur_acisi": "15 Derece Sağ"}

    def gece_pusulasi_temasi(self):
        return {"arka_plan": "Gece Mavisi", "yazi": "Ayışığı Beyazı"}

    def veda_tinisi_cal(self):
        return {"ses": "Gümüş Çan", "not": "Yarın yeni bir güneş doğacak, dinlen."}

# --- BÜYÜK FİNAL TESTİ ---
if __name__ == "__main__":
    pusula = PACDIGlobal("TR", "Genç", "Ali Yılmaz")
    print(f"🚀 PACDI GLOBAL v6.0 AKTİF: {pusula.giris_animasyonu_tetikle()['mesaj']}")
