
import pygame
import random

# Pygame başlat
pygame.init()
# Ekran boyutu ve başlık
ekran_genislik = 800
ekran_yukseklik = 600
ekran = pygame.display.set_mode((ekran_genislik, ekran_yukseklik))
pygame.display.set_caption("Taş, Kağıt, Makas Oyunu")

# Renkler
beyaz = (255, 255, 255)

# Nesne sınıfı
class Nesne:
    def __init__(self, x, y,tur):
        self.tur = tur
        self.hiz_x = random.uniform(-5, 5)
        self.hiz_y = random.uniform(-5, 5)

        if tur == "tas":
            self.resim = pygame.image.load("tas.png")  # Kendi nesnenizin resmini ekleyin
        elif tur == "makas":
            self.resim = pygame.image.load("makas.png")  # Kendi nesnenizin resmini ekleyin
        elif tur == "kagit":
            self.resim = pygame.image.load("kagit.png")  # Kendi nesnenizin resmini ekleyin

        self.genislik = self.resim.get_width()
        self.yukseklik = self.resim.get_height()
        self.resim = pygame.transform.scale(self.resim, (self.genislik, self.yukseklik))

        self.x = random.randint(0, ekran_genislik - self.genislik)
        self.y = random.randint(0, ekran_yukseklik - self.yukseklik)
    def hareket_et(self):
        self.x += self.hiz_x
        self.y += self.hiz_y

        # Ekran sınırları dışına çıkmayı kontrol et
        if self.x < 0:
            self.x = 0
            self.hiz_x *= -1
        elif self.x > ekran_genislik - self.genislik:
            self.x = ekran_genislik - self.genislik
            self.hiz_x *= -1

        if self.y < 0:
            self.y = 0
            self.hiz_y *= -1
        elif self.y > ekran_yukseklik - self.yukseklik:
            self.y = ekran_yukseklik - self.yukseklik
            self.hiz_y *= -1

    def ciz(self):
        ekran.blit(self.resim, (self.x, self.y))



def carpisti_mi(nesne1, nesne2):
    return (nesne1.x < nesne2.x + nesne2.genislik and
            nesne1.x + nesne1.genislik > nesne2.x and
            nesne1.y < nesne2.y + nesne2.yukseklik and
            nesne1.y + nesne1.yukseklik > nesne2.y)


nesneler = []
nesne_sayisi = 10

for _ in range(nesne_sayisi):
    nesneadi = Nesne(random.randint(0, ekran_genislik), random.randint(0, ekran_yukseklik), "tas")
    nesneler.append(nesneadi)

    nesneadi = Nesne(random.randint(0, ekran_genislik), random.randint(0, ekran_yukseklik), "kagit")
    nesneler.append(nesneadi)

    nesneadi = Nesne(random.randint(0, ekran_genislik), random.randint(0, ekran_yukseklik), "makas")
    nesneler.append(nesneadi)


calisiyor = True
while calisiyor:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            calisiyor = False
    for i in range(len(nesneler)):
        for j in range(i + 1, len(nesneler)):
            nesne1 = nesneler[i]
            nesne2 = nesneler[j]

            if carpisti_mi(nesne1, nesne2):
                if (nesne1.tur == "tas" and nesne2.tur == "kagit") or (nesne1.tur == "kagit" and nesne2.tur == "tas"):
                    # Tas ile kagit carpisti, iki tas yerine iki kagit olacak
                    nesne1.tur = "kagit"
                    nesne2.tur = "kagit"
                elif (nesne1.tur == "kagit" and nesne2.tur == "makas") or (
                        nesne1.tur == "makas" and nesne2.tur == "kagit"):
                    # Kagit ile makas carpisti, iki kagit yerine iki makas olacak
                    nesne1.tur = "makas"
                    nesne2.tur = "makas"
                elif (nesne1.tur == "makas" and nesne2.tur == "tas") or (nesne1.tur == "tas" and nesne2.tur == "makas"):
                    # Makas ile tas carpisti, iki makas yerine iki tas olacak
                    nesne1.tur = "tas"
                    nesne2.tur = "tas"
                nesne1.hiz_x *= -1
                nesne1.hiz_y *= -1
                nesne2.hiz_x *= -1
                nesne2.hiz_y *= -1



            nesne1.resim = pygame.image.load(nesne1.tur + ".png")
            nesne2.resim = pygame.image.load(nesne2.tur + ".png")

    for nesne in nesneler:
        nesne.hareket_et()
        nesne.ciz()

    pygame.display.update()
    ekran.fill(beyaz)  # Ekranı her çerçeve başında temizle

pygame.quit()