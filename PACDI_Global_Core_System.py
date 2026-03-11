# =================================================================
# PROJE: PACDI GLOBAL - GERMANY & PARTNER EDITION
# VERSION: 9.0 (Onur, Sevgi ve Sabır Mührüyle)
# PARA BİRİMİ: € (Euro) | DİLLER: Almanca & Türkçe
# =================================================================

import datetime

class PACDIGlobal:
    def __init__(self, kullanici_adi, dil="Almanca", partner="Merkez"):
        self.kullanici_adi = kullanici_adi
        self.dil = dil # "Almanca" veya "Türkçe"
        self.partner = partner # Caritas, Diakoni, Hukuk Derneği vb.
        self.para_birimi = "€"
        self.asgari_ucret = 2100 # Almanya brüt asgari ücret (yaklaşık)

    def hosgeldin_mesaji(self):
        """Kullanıcıyı seçtiği dilde karşılar."""
        mesajlar = {
            "Almanca": f"Willkommen bei PACDI Global, {self.kullanici_adi}. [EHRE, LIEBE, GEDULD]",
            "Türkçe": f"PACDI Global'e hoş geldiniz, {self.kullanici_adi}. [ONUR, SEVGİ, SABIR]"
        }
        return mesajlar.get(self.dil, mesajlar["Almanca"])

    def refah_analizi(self, katsayi):
        """Refah katsayısını Euro üzerinden hesaplar."""
        tutar = self.asgari_ucret * katsayi
        if self.dil == "Almanca":
            return f"Wohlstandsindex: {tutar}{self.para_birimi} (Faktor: {katsayi}x)"
        return f"Refah Endeksi: {tutar}{self.para_birimi} (Katsayı: {katsayi}x)"

    def kurumsal_indirim(self, kurum_adi):
        """Sigorta veya Hukuk Derneği üyelerine özel alan açar."""
        indirimler = {"HUKUK_DERNEGI": 0.50, "SIGORTA_GURUP": 0.20}
        oran = indirimler.get(kurum_adi, 0)
        durum = "Indirim uygulandı" if self.dil == "Türkçe" else "Rabatt angewendet"
        return f"{kurum_adi}: %{oran*100} {durum}."

    def easygov_islem(self, evrak_adi):
        """EasyGov bürokrasi çözücü (Partner bazlı)."""
        detay = "Bürokraside bir nefes." if self.dil == "Türkçe" else "Ein Atemzug in der Bürokratie."
        return {
            "Partner": self.partner,
            "Evrak": evrak_adi,
            "Durum": "Bereit / Hazır",
            "Mesaj": detay
        }

    def vicdan_muhuru(self):
        """Evrensel mühür."""
        muhur = "HERKUNFT: EHRE, LIEBE UND GEDULD" if self.dil == "Almanca" else "MENŞEİ: ONUR, SEVGİ VE SABIR"
        return f"[{self.partner}] - {muhur}"

# --- SİSTEM SİMÜLASYONU ---
if __name__ == "__main__":
    # Örnek: Caritas üzerinden Almanca işlem yapan bir kullanıcı
    app = PACDIGlobal("Onur Dostu", "Almanca", "Caritas Berlin")
    print(app.hosgeldin_mesaji())
    print(app.refah_analizi(2.8))
    print(app.kurumsal_indirim("HUKUK_DERNEGI"))
    print(app.easygov_islem("Widerspruch Rente (Emeklilik İtirazı)"))
    print(app.vicdan_muhuru())
