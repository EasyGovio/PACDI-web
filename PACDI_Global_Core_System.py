# =================================================================
# PROJE: PACDI GLOBAL - EASYGOV & APARTMENTS PARTNER SİSTEMİ
# SÜRÜM: v8.0 (Geniş Yataklı Nehir - Bayi Modüllü)
# İLKELER: ONUR, SEVGI, SABIR
# =================================================================

import datetime

class PACDI_Global_Core:
    def __init__(self, partner_adi="Merkez", partner_tipi="Ana Yönetim"):
        self.partner_adi = partner_adi
        self.partner_tipi = partner_tipi # Caritas, Diakoni, Arzuhalci, Bayi
        self.tarih = datetime.datetime.now().strftime("%d/%m/%Y")
        
    def yetki_dogrula(self):
        """İşlemi yapan paydaşın yetki seviyesini belirler."""
        return f"[{self.partner_tipi}] {self.partner_adi} - Yetki Doğrulandı. İşlem Başlatılıyor..."

    def apartments_yonetim_paneli(self, daire_no, kiraci_adi, bedel_katsayisi):
        """Mülk yönetimi ve kiralama modülü."""
        kira_bedeli = 17002 * bedel_katsayisi  # Asgari ücret üzerinden dinamik hesap
        return {
            "islem": "Apartments Kiralama",
            "detay": f"Daire {daire_no} - Kiracı: {kiraci_adi}",
            "mali_durum": f"Kira: {kira_bedeli} TL (Katsayı: {bedel_katsayisi}x)",
            "muhur": f"Yöneten: {self.partner_adi} | Onurla Mühürlenmiştir."
        }

    def easygov_islem_motoru(self, evrak_tipi, kullanıcı):
        """EasyGov bürokrasi çözücü ve dilekçe hazırlayıcı."""
        return {
            "evrak": f"Hatasız {evrak_tipi} Hazırlandı.",
            "kullanici": kullanıcı,
            "servis_noktasi": f"EasyGov Partner: {self.partner_adi}",
            "not": "Bürokrasinin karmaşasında bir nefes borusu.",
            "motto": "Adalet bir nehir gibidir, paylaştıkça çoğalır."
        }

    def vicdan_muhuru_bas(self):
        """Tüm paydaş işlemlerinin altına basılan kadim mühür."""
        return {
            "ana_ilkeler": ["Onur", "Sevgi", "Sabır"],
            "izlenebilirlik": f"İşlem Kaynağı: {self.partner_adi}",
            "mesaj": "Bu evrak sabırla hazırlanmış, sevgiyle mühürlenmiştir."
        }

# --- SİSTEM SİMÜLASYONU (Örnek Kullanım) ---
if __name__ == "__main__":
    # Örnek 1: Caritas üzerinden bir EasyGov işlemi
    caritas_panel = PACDI_Global_Core("Caritas Berlin", "Kurumsal Paydaş")
    print(caritas_panel.yetki_dogrula())
    print(caritas_panel.easygov_islem_motoru("İkametgah İzni", "Ali Yılmaz"))
    
    print("-" * 50)
    
    # Örnek 2: Bir yakınının kiraladığı Apartment Paneli
    bayi_paneli = PACDI_Global_Core("Öztürk Gayrimenkul", "Bayi")
    print(bayi_paneli.yetki_dogrula())
    print(bayi_paneli.apartments_yonetim_paneli(102, "Hansa Müller", 2.5))
    
    print("-" * 50)
    print(caritas_panel.vicdan_muhuru_bas())
