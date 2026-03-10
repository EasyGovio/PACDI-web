# PACDI Global - Onur ve Analiz Motoru v1.0
import datetime

class PACDIMotor:
    def __init__(self, ulke, hedef_kitle):
        self.ulke = ulke
        self.hedef_kitle = hedef_kitle # "Genç" veya "Kıdemli"
        self.asgari_ucret = 2100 if ulke == "DE" else 17002 # Örn: Euro ve TL
        
    def refah_analizi_yap(self, puan, potansiyel_maas):
        """Gençler için (PusulaPro) Kariyer ve Refah Hesabı"""
        katsayi = potansiyel_maas / self.asgari_ucret
        refah_durumu = "Yüksek" if katsayi > 3 else "Standart"
        return f"Refah Katsayınız: {katsayi:.2f} ({refah_durumu} Yaşam Standartı)"

    def gunun_pusulasi_getir(self):
        """Tüm kullanıcılar için takvim yaprağı mesajı"""
        mesajlar = [
            "Sevginin dili evrenseldir, maya sağlamsa yol onurdur.",
            "Kendi yolunu çizen, rüzgarın yönüne takılmaz.",
            "En büyük nimet, bir gönülde hatır sormaktır."
        ]
        # Her güne farklı bir mesaj (Basit simülasyon)
        gun = datetime.datetime.now().day % len(mesajlar)
        return f"🧭 Bugünün Pusulası: {mesajlar[gun]}"

# --- Uygulama Başlatma ---
# 1. Gençler için PusulaPro (TR)
genç_pusula = PACDIMotor("TR", "Genç")
print(f"PusulaPro TR: {genç_pusula.refah_analizi_yap(85, 45000)}")

# 2. Kıdemli Dostlar için Gönül Pusulası (EU)
kıdemli_pusula = PACDIMotor("DE", "Kıdemli")
print(f"Silver Compass DE: {kıdemli_pusula.gunun_pusulasi_getir()}")
