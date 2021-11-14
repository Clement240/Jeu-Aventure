"""
Programme réalisé par Dubois, Clément, 1G7
"""
import pygame

Longueur=1100
Largeur=734
#initialisation graphique
pygame.init()
fenetre = pygame.display.set_mode((Longueur, Largeur), pygame.FULLSCREEN)
pygame.display.set_caption("jeu d'aventure")
font = pygame.font.Font('freesansbold.ttf', 35)
font2 = pygame.font.Font('freesansbold.ttf', 20)
image0=pygame.image.load("Devanture.jpg")
image1=pygame.image.load("vestibule.jpg")
image2=pygame.image.load("salle-a-manger.jpg")
image3=pygame.image.load("cuisine.jpg")
image4=pygame.image.load("salle-de-bain.jpg")
image5=pygame.image.load("salon.jpg")
image6=pygame.image.load("jardin.jpg")
image7=pygame.image.load("chambre.jpg")
image8=pygame.image.load("chambre dami.jpg")
image9=pygame.image.load("map.jpg")
image10=pygame.image.load("fond-gris.png")
image11=pygame.image.load("fond-clair.jpg")
image12=pygame.image.load("Menu.jpg")
text0 = font.render("Vous vous trouvez devant votre maison", True, (231, 62, 1))
text1 = font.render("Vous vous trouvez dans le vestibule", True, (231, 62, 1))
text2 = font.render("Vous vous trouvez dans la salle à manger", True, (231, 62, 1))
text3 = font.render("Vous vous trouvez dans la cuisine", True, (231, 62, 1))
text4 = font.render("Vous vous trouvez dans la salle de bain", True, (231, 62, 1))
text5 = font.render("Vous vous trouvez dans le salon", True, (231, 62, 1))
text6 = font.render("Vous vous trouvez dans le jardin", True, (231, 62, 1))
text7 = font.render("Vous vous trouvez dans la chambre", True, (231, 62, 1))
text8 = font.render("Vous vous trouvez dans la chambre d'ami", True, (231, 62, 1))
text9 = font2.render("Touches :", True, (30, 127, 203))
text10 = font2.render("n=nord", True, (30, 127, 203))
text11 = font2.render("s=sud", True, (30, 127, 203))
text12 = font2.render("o=ouest", True, (30, 127, 203))
text13 = font2.render("e=est", True, (30, 127, 203))
text14 = font2.render("Attention, une fois rentré, vous ne pourrez plus ressortir !", True, (255, 0, 0))
text15 = font2.render("q=quitter", True, (30, 127, 203))

dansQuellePierceEstLePersonnage=9

def decrireLaPiece(piece):
    if piece==9:
        fenetre.blit(image12,(0,0))  # Menu
    elif piece==0:
        fenetre.blit(image0,(0,0))  #afficher l'image à la prochaine actualisation #Vestibule
        fenetre.blit(image10,(0,650)) # Fond Texte
        fenetre.blit(image11,(0,0)) # Fond Texte2
        fenetre.blit(text14,(0,20)) # Attention
        fenetre.blit(text9,(890,655)) # Touches
        fenetre.blit(text10,(990,655)) # Touches nord
        fenetre.blit(text11,(990,675)) # Touches sud
        fenetre.blit(text12,(990,695)) # Touches ouest
        fenetre.blit(text13,(990,715)) # Touches est
        fenetre.blit(text15,(890,675)) # Touches quitter
        fenetre.blit(text0,(0,670)) #afficher le texte à la prochaine actualisation
    elif piece==1:
        fenetre.blit(image1,(0,0))  #afficher l'image à la prochaine actualisation #Vestibule
        fenetre.blit(image9,(800,0)) # Carte
        fenetre.blit(image10,(0,650)) # Fond Texte
        fenetre.blit(text9,(890,655)) # Touches
        fenetre.blit(text10,(990,655)) # Touches nord
        fenetre.blit(text11,(990,675)) # Touches sud
        fenetre.blit(text12,(990,695)) # Touches ouest
        fenetre.blit(text13,(990,715)) # Touches est
        fenetre.blit(text15,(890,675)) # Touches quitter
        fenetre.blit(text1,(0,670)) #afficher le texte à la prochaine actualisation
    elif piece==2:
        fenetre.blit(image2,(0,0)) #Salle a manger
        fenetre.blit(image9,(800,0)) # Carte
        fenetre.blit(image10,(0,650)) # Fond Texte
        fenetre.blit(text9,(890,655)) # Touches
        fenetre.blit(text10,(990,655)) # Touches nord
        fenetre.blit(text11,(990,675)) # Touches sud
        fenetre.blit(text12,(990,695)) # Touches ouest
        fenetre.blit(text13,(990,715)) # Touches est
        fenetre.blit(text15,(890,675)) # Touches quitter
        fenetre.blit(text2,(0,670))
    elif piece==3:
        fenetre.blit(image3,(0,0)) #Cuisine
        fenetre.blit(image9,(800,0)) # Carte
        fenetre.blit(image10,(0,650)) # Fond Texte
        fenetre.blit(text9,(890,655)) # Touches
        fenetre.blit(text10,(990,655)) # Touches nord
        fenetre.blit(text11,(990,675)) # Touches sud
        fenetre.blit(text12,(990,695)) # Touches ouest
        fenetre.blit(text13,(990,715)) # Touches est
        fenetre.blit(text15,(890,675)) # Touches quitter
        fenetre.blit(text3,(0,670))
    elif piece==4:
        fenetre.blit(image4,(0,0)) #Salle de bain
        fenetre.blit(image9,(800,0)) # Carte
        fenetre.blit(image10,(0,650)) # Fond Texte
        fenetre.blit(text9,(890,655)) # Touches
        fenetre.blit(text10,(990,655)) # Touches nord
        fenetre.blit(text11,(990,675)) # Touches sud
        fenetre.blit(text12,(990,695)) # Touches ouest
        fenetre.blit(text13,(990,715)) # Touches est
        fenetre.blit(text15,(890,675)) # Touches quitter
        fenetre.blit(text4,(0,670))
    elif piece==5:
        fenetre.blit(image5,(0,0)) # Salon
        fenetre.blit(image9,(800,0)) # Carte
        fenetre.blit(image10,(0,650)) # Fond Texte
        fenetre.blit(text9,(890,655)) # Touches
        fenetre.blit(text10,(990,655)) # Touches nord
        fenetre.blit(text11,(990,675)) # Touches sud
        fenetre.blit(text12,(990,695)) # Touches ouest
        fenetre.blit(text13,(990,715)) # Touches est
        fenetre.blit(text15,(890,675)) # Touches quitter
        fenetre.blit(text5,(0,670))
    elif piece==6:
        fenetre.blit(image6,(0,0)) # Jardin
        fenetre.blit(image9,(800,0)) # Carte
        fenetre.blit(image10,(0,650)) # Fond Texte
        fenetre.blit(text9,(890,655)) # Touches
        fenetre.blit(text10,(990,655)) # Touches nord
        fenetre.blit(text11,(990,675)) # Touches sud
        fenetre.blit(text12,(990,695)) # Touches ouest
        fenetre.blit(text13,(990,715)) # Touches est
        fenetre.blit(text15,(890,675)) # Touches quitter
        fenetre.blit(text6,(0,670))
    elif piece==7:
        fenetre.blit(image7,(0,0)) # Chambre
        fenetre.blit(image9,(800,0)) #Carte
        fenetre.blit(image10,(0,650)) # Fond Texte
        fenetre.blit(text9,(890,655)) # Touches
        fenetre.blit(text10,(990,655)) # Touches nord
        fenetre.blit(text11,(990,675)) # Touches sud
        fenetre.blit(text12,(990,695)) # Touches ouest
        fenetre.blit(text13,(990,715)) # Touches est
        fenetre.blit(text15,(890,675)) # Touches quitter
        fenetre.blit(text7,(0,670))
    elif piece==8:
        fenetre.blit(image8,(0,0)) # Chambre d'ami
        fenetre.blit(image9,(800,0)) # Carte
        fenetre.blit(image10,(0,650)) # Fond Texte
        fenetre.blit(text9,(890,655)) # Touches
        fenetre.blit(text10,(990,655)) # Touches nord
        fenetre.blit(text11,(990,675)) # Touches sud
        fenetre.blit(text12,(990,695)) # Touches ouest
        fenetre.blit(text13,(990,715)) # Touches est
        fenetre.blit(text15,(890,675)) # Touches quitter
        fenetre.blit(text8,(0,670))

def decision(direction,piece):
    print("Vous désirez allez au", direction)
    memorisePiece=piece
    #N : le personnage désire aller au nord
    if direction=='n':
        if piece==9:
            piece=0
        elif piece==0:
            piece=1
        elif piece==1:
            piece=2
        elif piece==5:
            piece=1
        elif piece==6:
            piece=5
    #S : le personnage désire aller au sud
    elif direction=='s':
        if piece==2:
            piece=1
        elif piece==1:
            piece=5
        elif piece==5:
            piece=6
    #E : le personnage désire aller à l'est
    elif direction=='e':
        if piece==3:
            piece=2
        elif piece==5:
            piece=4
        elif piece==2:
            piece=6
        elif piece==7:
            piece=1
        elif piece==1:
            piece=8
    #O : le personnage désire aller à l'ouest
    elif direction=='o':
        if piece==2:
            piece=3
        elif piece==4:
            piece=5
        elif piece==6:
            piece=2
        elif piece==1:
            piece=7
        elif piece==8:
            piece=1
    if memorisePiece==piece:
        print("Déplacement Impossible")
    else:
        print("C'est possible")
    return piece

loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenetre (croix rouge)
        elif event.type == pygame.KEYDOWN:  #lecture du clavier
            dansQuellePierceEstLePersonnage=decision(event.unicode,dansQuellePierceEstLePersonnage)
            if event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                loop = False
    decrireLaPiece(dansQuellePierceEstLePersonnage)
    # Actualisation de l'affichage
    pygame.display.flip()
pygame.quit()

