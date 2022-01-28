import requests
import bs4
import cfscrape
from tkinter import *
from threading import Thread
import time

root = Tk()
root.resizable(False,False)
root.geometry("830x600")
root.configure(bg="black")
root.title("SAMP USER CHECKER 0.2")

image1 = PhotoImage(file="img/green.png")
image2 = PhotoImage(file="img/red.png")
image3 = PhotoImage(file="img/black.png")
image4 = PhotoImage(file="img/1.png")

entry1 = Entry(root,width=15,font=("Arial",15),borderwidt=0, fg="#ff3300", bg="#1a0000", highlightbackground="#ff3300")
entry1.place(x=15,y=60)

label0 = Label(root,image=image4, borderwidth=0, highlightbackground="black")
label0.place(x=520,y=50)
label1 = Label(root,image=image3, borderwidth=0, highlightbackground="black")
label1.place(x=0,y=0)
label2 = Label(root,image=image3, borderwidth=0, highlightbackground="black")
label2.place(x=83,y=0)
label3 = Label(root,image=image3, borderwidth=0, highlightbackground="black")
label3.place(x=166,y=0)
label4 = Label(root,image=image3, borderwidth=0, highlightbackground="black")
label4.place(x=249,y=0)
label5 = Label(root,image=image3, borderwidth=0, highlightbackground="black")
label5.place(x=332,y=0)
label6 = Label(root,image=image3, borderwidth=0, highlightbackground="black")
label6.place(x=415,y=0)
label7 = Label(root,image=image3, borderwidth=0, highlightbackground="black")
label7.place(x=498,y=0)
label8 = Label(root,image=image3, borderwidth=0, highlightbackground="black")
label8.place(x=581,y=0)
label9 = Label(root,image=image3, borderwidth=0, highlightbackground="black")
label9.place(x=664,y=0)
label10 = Label(root,image=image3, borderwidth=0, highlightbackground="black")
label10.place(x=747,y=0)
label11 = Label(root,text="OG-Times",bg="#ff3300", highlightbackground="black",width="11",font=("Arial",9))
label11.place(x=0,y=25)
label12 = Label(root,text="Ruby",bg="#ff3300", highlightbackground="black",width="11",font=("Arial",9))
label12.place(x=83,y=25)
label13 = Label(root,text="B-hood",bg="#ff3300",  highlightbackground="black",width="11",font=("Arial",9))
label13.place(x=166,y=25)
label14 = Label(root,text="Bzone1",bg="#ff3300",  highlightbackground="black",width="11",font=("Arial",9))
label14.place(x=249,y=25)
label15 = Label(root,text="Bzone2",bg="#ff3300",  highlightbackground="black",width="11",font=("Arial",9))
label15.place(x=332,y=25)
label16 = Label(root,text="Crowland",bg="#ff3300",  highlightbackground="black",width="11",font=("Arial",9))
label16.place(x=415,y=25)
label18 = Label(root,text="Blue",bg="#ff3300",  highlightbackground="black",width="11",font=("Arial",9))
label18.place(x=498,y=25)
label20 = Label(root,text="Username",bg="black", fg="#ff3300",  highlightbackground="black",width="11",font=("Arial",14))
label20.place(x=185,y=62)

text1 = Text(root,width=92,height=23, fg="#ff3300",bg="#330000",borderwidth=0,highlightbackground="black", font=("Arial",12))
text1.place(x=0,y=160)

text1.insert(INSERT,"\n SUC > Samp User Chcker 0.2\n SUC > Fondat si creat de ArlecchinoSec si Skyled (editat de RResTarT)\n SUC > Se asteapta un user...")

canvas1 = Canvas(root,highlightbackground="#ff0000",bg="#ff0000",width=900,height=1)
canvas1.place(x=0,y=42)
canvas2 = Canvas(root,highlightbackground="#ff0000",bg="#ff0000",width=900,height=1)
canvas2.place(x=0,y=160)

def executa():
	text1.delete("1.0",END)
	user = entry1.get()
	label1.configure(image=image3)
	label2.configure(image=image3)
	label3.configure(image=image3)
	label4.configure(image=image3)
	label5.configure(image=image3)
	label6.configure(image=image3)
	label7.configure(image=image3)
	if len(user) <= 3:

		# OG-Times

		text1.insert(INSERT,"\n SUC > Un nume are minim 3 litere , mai incearca...\n")
	else:
		text1.insert(INSERT,"\n SUC > Utilizatorul este valid...\n\n")
		text1.insert(INSERT," SUC > Cauta jucatorul in panel-ul OG-Times\n")
		url = "https://earthpanel.og-times.ro/profile/" + user
		a = requests.get(url)
		soup = bs4.BeautifulSoup(a.text,"lxml")
		if (str(user)) in (str(soup)):
			text1.insert(INSERT," SUC > Jucatorul a fost gasit in panel-ul OG-Times\n\n")
			label1.configure(image=image1)
		else:
			text1.insert(INSERT," SUC > Jucatorul nu a fost gasit in panel-ul OG-Times\n\n")
			label1.configure(image=image2)

		# Ruby

		text1.insert(INSERT," SUC > Cauta jucatorul in panel-ul Ruby\n")
		url = "https://rubypanel.nephrite.ro/profile/" + user
		a = requests.get(url)
		soup = bs4.BeautifulSoup(a.text,"lxml")
		if (str(user)) in (str(soup)):
			text1.insert(INSERT," SUC > Jucatorul a fost gasit in panel-ul Ruby\n\n")
			label2.configure(image=image1)
		else:
			text1.insert(INSERT," SUC > Jucatorul nu a fost gasit in panel-ul Ruby\n\n")
			label2.configure(image=image2)

		# Jade

		text1.insert(INSERT," SUC > Cauta jucatorul in panel-ul B-Hood\n")
		url = "https://panel.b-hood.ro/user/profile/" + user
		a = requests.get(url)
		soup = bs4.BeautifulSoup(a.text,"lxml")
		if (str(user)) in (str(soup)):
			text1.insert(INSERT," SUC > Jucatorul a fost gasit in panel-ul B-Hood\n\n")
			label3.configure(image=image1)
		else:
			text1.insert(INSERT," SUC > Jucatorul nu a fost gasit in panel-ul B-hood\n\n")
			label3.configure(image=image2)

		# B-zone 1 

		text1.insert(INSERT," SUC > Cauta jucatorul in panel-ul B-zone 1\n")
		url = "https://www.rpg1.b-zone.ro/players/general/" + user
		a = requests.get(url)
		soup = bs4.BeautifulSoup(a.text,"lxml")
		if "Player not found" in (str(soup)):
			text1.insert(INSERT," SUC > Jucatorul nu a fost gasit in panel-ul B-Zone1\n\n")
			label4.configure(image=image2)
		else:
			text1.insert(INSERT," SUC > Jucatorul a fost gasit in panel-ul B-Zone1\n\n")
			label4.configure(image=image1)

		# B-zone 2 

		text1.insert(INSERT," SUC > Cauta jucatorul in panel-ul B-zone 2\n")
		url = "https://www.rpg2.b-zone.ro/players/general/" + user
		a = requests.get(url)
		soup = bs4.BeautifulSoup(a.text,"lxml")
		if "Player not found" in (str(soup)):
			text1.insert(INSERT," SUC > Jucatorul nu a fost gasit in panel-ul B-Zone2\n\n")
			label5.configure(image=image2)
		else:
			text1.insert(INSERT," SUC > Jucatorul a fost gasit in panel-ul B-Zone2\n\n")
			label5.configure(image=image1)

		# B-zone 3 

		text1.insert(INSERT," SUC > Cauta jucatorul in panel-ul Crowland\n")
		url = "https://phoenixpanel.crowland.ro/profile/" + user
		a = requests.get(url)
		soup = bs4.BeautifulSoup(a.text,"lxml")
		if "Player not found" in (str(soup)):
			text1.insert(INSERT," SUC > Jucatorul nu a fost gasit in panel-ul Crowland\n\n")
			label6.configure(image=image2)
		else:
			text1.insert(INSERT," SUC > Jucatorul a fost gasit in panel-ul Crowland\n\n")
			label6.configure(image=image1)


		# Blue Bugged 

		text1.insert(INSERT," SUC > Cauta jucatorul in panel-ul Blue Bugged\n")
		url = "https://bluepanel.bugged.ro/profile/" + user
		scraper = cfscrape.create_scraper()
		text1.insert(INSERT," SUC > Panel-ul e protejat de CloudFlare\n")	
		text1.insert(INSERT," SUC > Asteapta 5 secunde sa trec de el ...\n")		
	
		a = scraper.get(url).content
		soup = bs4.BeautifulSoup(a,"lxml")
		if (str(user)) in (str(soup)):
			text1.insert(INSERT," SUC > Jucatorul a fost gasit in panel-ul Blue Bugged\n\n")
			label7.configure(image=image1)
		else:
			text1.insert(INSERT," SUC > Jucatorul nu a fost gasit in panel-ul Blue Bugged\n\n")
			label7.configure(image=image2)





button1 = Button(root,text="Executa", fg="#800000",bg="#1a0000",borderwidth=0,highlightbackground="black", font=("Arial",12), command=lambda : Thread(target=executa).start())
button1.place(x=15,y=100)







root.mainloop()