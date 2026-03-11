# =================================================================
# PROJE: PACDI GLOBAL - GERMANY & PARTNER EDITION
# VERSION: 9.0 (Onur, Sevgi ve Sabır Mührüyle)
# PARA BİRİMİ: € (Euro) | DİLLER: Almanca & Türkçe
# =================================================================

import datetime

class PACDIGlobal:
    def __init__(self, kullanici_adi, dil="Almanca", partner="Merkez"):
        """
        Sistemi Almanya odağında, Euro ve Partner yapısıyla başlatır.
        """
        self.kullanici_adi = kullanici_adi
        self.dil = dil # "Almanca" veya "Türkçe"
        self.partner = partner # Caritas, Diakoni, Hukuk Derneği, Bayi vb.
        self.para_birimi = "€"
        self.asgari_ucret = 2100 # Almanya brüt asgari ücret (yaklaşık)

    def hosgeldin_mesaji(self):
        """Kullanıcıyı seçtiği dilde karşılar ve ilkeleri fısıldar."""
        mesajlar = {
            "Almanca": f"Willkommen bei PACDI Global, {self.kullanici_adi}. [EHRE, LIEBE, GEDULD]",
            "Türkçe": f"PACDI Global'e hoş geldiniz, {self.kullanici_adi}. [ONUR, SEVGİ, SABIR]"
        }
        return mesajlar.get(self.dil, mesajlar["Almanca"])

    def refah_analizi(self, katsayi):
        """Refah katsayısını Almanya şartlarında Euro üzerinden hesaplar."""
        tutar = self.asgari_ucret * katsayi
        if self.dil == "Almanca":
            return f"Wohlstandsindex: {tutar}{self.para_birimi} (Faktor: {katsayi}x)"
        return f"Refah Endeksi: {tutar}{self.para_birimi} (Katsayı: {katsayi}x)"

    def kurumsal_indirim_uygula(self, kurum_adi):
        """Hukuk dernekleri veya sigorta üyeleri için indirimli alan açar."""
        indirimler = {
            "HUKUK_DERNEGI": 0.50, # %50 İndirim/Aidat Kapsamı
            "SIGORTA_GURUP": 0.20  # %20 İndirim
        }
        oran = indirimler.get(kurum_adi, 0)
        mesaj = f"{kurum_adi} üyeliği doğrulandı. %{oran*100} indirim tanımlandı." if self.dil == "Türkçe" else \
                f"{kurum_adi} Mitgliedschaft bestätigt. %{oran*100} Rabatt angewendet."
        return mesaj

    def easygov_islem_motoru(self, evrak_adi):
        """Bürokrasiyi partner bazlı çözen EasyGov motoru."""
        detay = "Bürokrasinin karmaşasında bir nefes borusu." if self.dil == "Türkçe" else \
                "Ein Atemzug in der bürokratischen Komplexität."
        return {
            "Partner": self.partner,
            "Evrak": evrak_adi,
            "Durum": "Bereit / Hazır",
            "Motto": "Adalet bir nehir gibidir, paylaştıkça çoğalır.",
            "Bilgi": detay
        }

    def vicdan_muhuru(self):
        """Tüm işlemlerin altına basılan evrensel mühür."""
        muhur = "HERKUNFT: EHRE, LIEBE UND GEDULD" if self.dil == "Almanca" else "MENŞEİ: ONUR, SEVGİ VE SABIR"
        return f"[{self.partner} Onaylı] - {muhur} - {datetime.datetime.now().strftime('%d/%m/%Y')}"

# --- SİSTEM SİMÜLASYONU (Lansman Öncesi Son Test) ---
if __name__ == "__main__":
    # Örnek: Hukuk Derneği paydaşlığıyla Türkçe kullanan bir emekli
    app = PACDIGlobal("Onur Dostu", "Türkçe", "Hukuk Derneği Üyesi")
    
    print(app.hosgeldin_mesaji())
    print(app.refah_analizi(2.5))
    print(app.kurumsal_indirim_uygula("HUKUK_DERNEGI"))
    print(app.easygov_islem_motoru("Emeklilik İtiraz Dilekçesi (Widerspruch)"))
    print(app.vicdan_muhuru())
