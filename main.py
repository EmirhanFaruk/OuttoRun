
# Modification date: Mon Jun 26 17:07:32 2023

# Production date: Sun Sep  3 15:43:51 2023

import pygame

print(pygame.init())

#Ekran büyüklüğü
ekran_buyuklugu = (120, 120)

#Tam ekran vs olması için gereken flagler
bayraklar = pygame.SCALED | pygame.FULLSCREEN | pygame.NOFRAME
#ana pencerenin tanımlanması(buraya yansıtılacak herşey)
ana_pencere = pygame.display.set_mode(ekran_buyuklugu, bayraklar)


araba_resmi = pygame.image.load("Assets\Car\Car_Straight.png").convert_alpha()#16x16
arkaplan_resmi = pygame.image.load("Assets\Background\Background2_edit.png").convert_alpha()#120x120
#arkaplan_resmi = pygame.transform.scale(arkaplan_resmi, (120, 120))


sayac = pygame.time.Clock()
kare_hizi = 30
dongu_calisiyor = True
while dongu_calisiyor:
    sayac.tick(kare_hizi)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dongu_calisiyor = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                dongu_calisiyor = False
    
    
    #arkaplanın ekrana yansıtılması
    ana_pencere.blit(arkaplan_resmi, (0, 0))
    
    #arabanın ekrana yansıtılması
    ana_pencere.blit(araba_resmi, (ekran_buyuklugu[0]/2 - 8, ekran_buyuklugu[1]/2 - 8))
    
    
    pygame.display.flip()
pygame.quit()
