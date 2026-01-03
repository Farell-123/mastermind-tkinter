from tkinter import*
import tkinter.font as tkFont
from random import*
import random


win = Tk()


liste_couleur=["yellow","blue","red","green","white","black"]
liste_M=[]
for i in range(4):
         liste_M+=[random.choice(liste_couleur)]

liste_utilisateur=[]
round=0
max_rounds = 12
round = 0

def fermer(event=None):
    win.destroy()

def afficher_regles():
    regles_texte = """
    1. Le jeu génère une combinaison secrète de 4 couleurs.
    2. Vous devez deviner la bonne combinaison en cliquant sur les couleurs.
    3. Après chaque tentative, le jeu vous indique :
       - Le nombre de pions bien placés.
       - Le nombre de pions mal placés.
    4. Vous avez 12 tentatives pour trouver la bonne combinaison.
    5. Bonne chance !
    """
    label_regles = Label(win, text=regles_texte, font=("Arial", 12))
    label_regles.place(x=730,y=190)


def afficher_reponse():
    d1=850
    d2=900
    reponse = """ La réponse était :    """
    label_reponse = Label(win, text=reponse, font=("Arial", 12), fg="green")
    label_reponse.place(x=940,y=360)
    for i in range(len(liste_M)):
              d1+=50
              d2+=50
              canvas.create_oval(d1, 400, d2, 450,fill=liste_M[i])
    win.after(8000, win.destroy)


win.title("Mastermind")

win.attributes('-fullscreen', True)
win.bind("<Escape>", fermer)


canvas = Canvas(win, width=win.winfo_screenwidth(), height=win.winfo_screenheight())
canvas.place(x=0, y=0)

bouton_quitter = Button(win, text="Quitter", font=("Arial", 14), command=win.destroy, bg="red", fg="white")
bouton_quitter.place(x=35, y=40)

bouton_regles = Button(win, text="Règles", font=("Arial", 14), command=afficher_regles, bg="blue", fg="white")
bouton_regles.place(x=1170, y=150)

bouton_reponse= Button(win, text="Réponse", font=("Arial", 14), command=afficher_reponse, bg="green", fg="white")
bouton_reponse.place(x=1050, y=150)
def draw_lines():
        canvas_width = canvas.winfo_width()
        ligne1 = canvas.create_line(725, 135, canvas_width, 135)
        ligne2 = canvas.create_line(150, 0, 150, canvas_width)

win.after(100, draw_lines)

font = tkFont.Font(family="The Augusta", size=41, weight="bold")
label = Label(win, text="Mastermind !", font=font)
label.place(x=725, y=0)

jaune=canvas.create_oval(30, 140, 110, 210, fill= "yellow")
bleu=canvas.create_oval(30, 220, 110, 295, fill="blue")
rouge=canvas.create_oval(30, 310, 110, 390, fill="red")
vert=canvas.create_oval(30, 405, 110, 485, fill="green")
blanc=canvas.create_oval(30, 500, 110, 580, fill="white")
noir=canvas.create_oval(30, 600, 110, 680, fill="black")



(y1,y2)=(740,770)
def ajouter_couleur(couleur):
    (x1,x2)=(135,165)
    global y1 , y2
    if len(liste_utilisateur) < 4:

        liste_utilisateur.append(couleur)
    if len(liste_utilisateur) == 4:
        for i in range(len(liste_utilisateur)):
              x1+=50
              x2+=50
              canvas.create_oval(x1, y1, x2, y2,fill=liste_utilisateur[i])
        y1-=60
        y2-=60
        verification()



def action_jaune(event):
    print("Cercle jaune cliqué !")
    ajouter_couleur("yellow")
def action_bleu(event):
    print("Cercle bleu cliqué !")
    ajouter_couleur("blue")
def action_rouge(event):
    print("Cercle rouge cliqué !")
    ajouter_couleur("red")
def action_vert(event):
    print("Cercle vert cliqué !")
    ajouter_couleur("green")
def action_blanc(event):
    print("Cercle blanc cliqué !")
    ajouter_couleur("white")
def action_noir(event):
    print("Cercle noir cliqué !")
    ajouter_couleur("black")



canvas.tag_bind(jaune, "<Button-1>", action_jaune)
canvas.tag_bind(bleu, "<Button-1>", action_bleu)
canvas.tag_bind(rouge, "<Button-1>", action_rouge)
canvas.tag_bind(vert, "<Button-1>", action_vert)
canvas.tag_bind(blanc, "<Button-1>", action_blanc)
canvas.tag_bind(noir, "<Button-1>", action_noir)

(b1,b2)=(730,760)
def verification():
     global round ,liste_utilisateur
     global b1 , b2
     compteur_parfait=0
     compteur_Pparfait=0
     print("il vous reste",12-round,"round")
     print("Vous avez mis",liste_utilisateur)
     if liste_utilisateur==liste_M:
          print("VOUS AVEZ RÉUSSI EN",round,"ROUND , BRAVO!")
          afficher_reponse()
          label_victoire = Label(win, text=f" VOUS AVEZ RéUSSI EN {round} ROUND , BRAVO!", font="Arial" , fg= "red")
          label_victoire.place(x=800, y=475)
          win.after(10000, win.destroy)
     if liste_utilisateur!=liste_M:
         round+= 1
         if round>12:
             print("Vous avez perdu la réponse était",liste_M)
             afficher_reponse()
         else:
             for i in range(len(liste_M)):
              if liste_M[i]==liste_utilisateur[i]:
                      compteur_parfait+=1
              for j in range(len(liste_utilisateur)):
                  if liste_M[i]==liste_utilisateur[j] and liste_M[i]!=liste_utilisateur[i]:
                      compteur_Pparfait+=1
             liste_utilisateur=[]



     font_petit = tkFont.Font(win, family="Arial", size=15, weight="bold")

     label_parfait = Label(win, text=f"{compteur_parfait} pions parfaits", font=font_petit)
     label_parfait.place(x=400, y=b1)


     label_Pparfait = Label(win, text=f"{compteur_Pparfait} pions partiellement parfaits", font=font_petit)
     label_Pparfait.place(x=400, y=b2)
     b1-=60
     b2-=60
     print("nombre de pions parfaits",compteur_parfait)
     print("nombre de pions partiellement parfait",compteur_Pparfait)

win.mainloop()



