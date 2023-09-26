import tkinter as tk
from tkinter import*
import random
import pyperclip



   
   
def code():
   
    a=chr(random.randint(97,122)).upper()
    b=chr(random.randint(97,122)).upper()
   
    c=chr(random.randint(97,122)).lower()
    d=chr(random.randint(97,122)).lower()
   
    e=random.randint(0,9)
    f=random.randint(0,9)
   
    g=chr(random.randint(33,47))
    h=chr(random.randint(58,64))
    i=chr(random.randint(91,96))
    j=chr(random.randint(123,126))
   
    k=random.choice((g,h,i,j))
    l=random.choice((g,h,i,j))
   
    while l==k:
        l=random.choice((g,h,i,j))
   
    list=[a,b,c,d,e,f,k,l]
   
   
    longueur=len(list)
    code=''
    while len(code)<longueur:
        pos=random.randint(0,longueur-1)
        if str(list[pos]) not in code:
            code+=str(list[pos])
           
    resultat1.config(font=("Arial",25), text=f"{code}")
    pyperclip.copy(code)
   
   
fenetre=Tk(className='générateur mot de passe')
fenetre.geometry('400x400')

bouton_generer=tk.Button(fenetre, font=("Arial",20),text="Générer", command=code)
bouton_generer.pack(padx=20, pady=20)

resultat1=tk.Label(fenetre,font=("Arial",10), text="")
resultat1.pack(pady=100)

text_label=tk.Label(fenetre, font=("Arial",20), text="mdp copié !")
text_label.pack(pady=200)



fenetre.mainloop()    

