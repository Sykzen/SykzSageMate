import tkinter as tk
from tkinter import *
import tkinter.filedialog
import PIL
from PIL import ImageTk
from PIL import Image
import os
import shutil
from Client import SendFile
print (" --------------------------------------------------------------------")
print (" # AWS SageMaker Cluster ")
print (" #  Créez, entraînez et déployez rapidement et facilement des modèles de machine learning (ML)  ")
print (" # pour tous les cas d'utilisation avec une infrastructure, des outils et des flux entièrement gérés")
print (" -----------------------------------------------------------------")
#Fonction AskopenFilename pour ouvrir un dossier courant
LST_Types = [( "Script python" , ".py" )]
def Send(host,nomFich):
    if nomFich != "":
        try:
            fich = open(nomFich, "rb") # test si le fichier existe
        except:
            print (" >> le fichier '" + nomFich + "' est introuvable.")
            time.sleep(2)
            exit()
        octets = os.path.getsize(nomFich) / 1024
        print (" Envoie du fichier " + nomFich + "' [" + str(octets) + " Ko]")
        try:
            socket.connect((host, 8080)) # test si le serveur existe
        except:
            print ("le serveur '" + host + "' est introuvable.")
            time.sleep(2)
            exit()
        BUFFER_SIZE = 4096
       # socket.send(nomFich.encode())
        #stroctets=str(octets)
        #socket.send(stroctets.encode())
        while True:
            bytes_read = fich.read(BUFFER_SIZE)
            if not bytes_read:
                break
            socket.sendall(bytes_read)
        

            #octets = octets * 1024 # Reconverti en octets
            #fich = open(nomFich, "rb")
            #num=0
            #if octets > 1024:	# Si le fichier est plus lourd que 1024 on l'envoi par paquet   
            #    for i in range(int(octets / 1024)):                        
             #       fich.seek(num, 0) # on se deplace par rapport au numero de caractere (de 1024 a 1024 octets)
              #      donnees = fich.read(1024) # Lecture du fichier en 1024 octets
               #     socket.sendall(donnees) 
                #    num = num + 1024
            
            #else: # Sinon on envoi tous d'un coup
             #   donnees = fich.read()
              #  socket.send(donnees)
            #fich.close()
        
        fich.close()
        global myIp
        myIp=socket.getsockname()[0].encode()
        socket.close()
    else:
        print("fichier vide")
def Receive():
    socket.bind((myIp, 8080)) # Creation du serveur
    socket.listen(3) # Mise en ecoute d'un client
    BUFFER_SIZE = 4096

    print( " >> Attente d'une nouvelle connexion...")
    conn, adresse = socket.accept() # accepte le client

    print (" >> Vous etes connecte avec : " + adresse[0])
    with open("Compiled_"+str(file), "wb") as f:
        while True:
            bytes_read = conn.recv(BUFFER_SIZE)
            if not bytes_read:    
                break
            f.write(bytes_read)
    conn.close()
    socket.close()
    
def Make():
    Send(host,file)
    print("Fichier Reçu par le serveur Main ")
    print("Recherche des Serveur Disponible ...")
    print("Fichier transferer vers le Host "+myIp)
    print("Fichier Compiler et prêt à être retranferer ")
    print("Fichier fichier Transferer ")
    Receive()
    root.destroy()


def askopenfile():
        global host
        global file
        p=tk.filedialog.askopenfilename ( title = "Sélectionnez un fichier ..." , filetypes = LST_Types )
        file=p
        host="10.3.141.1"
            
#Interface Graphique
root = tk.Tk()
root.title("AmazonSageMaker")
canvas1 = tk.Canvas(root, width = 1000, height = 600, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()
#canvas1.grid()


button1=tk.Button(text='Déposer votre Fichier' , command=askopenfile)
canvas1.create_window(500,50,window=button1)
canvas1.pack()
button2=tk.Button(text='Compiler' , command=Make)
canvas1.create_window(450,500,window=button2)
canvas1.pack()

imageLogo  = Image.open("static/logo.png")
imageLogo  =imageLogo.resize((200,130),Image.ANTIALIAS)
imageLogo  =ImageTk.PhotoImage(imageLogo)
canvas1.create_image(0,1, anchor = tk.NW, image=imageLogo)
canvas1.pack()

frames = [PhotoImage(file='static/on.gif',format = 'gif -index %i' %(i)) for i in range(2)]
frames2 = [PhotoImage(file='static/offe.gif',format = 'gif -index %i' %(i)) for i in range(2)]
class Server:
    def __init__(self,ide,ip,status,position):
        self.ide=ide
        self.ip=ip
        self.status=status
        self.position=position
    def setStatus(self):
        ide = tk.Label(root, text="ID :"+self.ide,bg = 'lightsteelblue2')
        ip=  tk.Label(root, text="IP :"+self.ip,bg = 'lightsteelblue2')
        status=tk.Label(root, text="STATUS :"+self.status,bg = 'lightsteelblue2')
        canvas1.create_window(self.position[0]+20, self.position[1], window=ide)
        canvas1.create_window(self.position[0]+20, self.position[1]+50, window=ip)
        canvas1.create_window(self.position[0]+20, self.position[1]+100, window=status)
def setStatusServerX(ide):
    return ide
def update(ind):

    frame = frames[ind]
    frame2 = frames2[ind]
    ind += 1
    ind=ind%2
    label.configure(image=frame,width="120")
    label2.configure(image=frame,width="120")
    label3.configure(image=frame,width="120")
    label4.configure(image=frame2,width="120")
    #canvas1.configure(image=frame)
    root.after(250, update, ind)
label = Label(root,width="120")
label2 = Label(root,width="120")
label3 = Label(root,width="120")
label4 = Label(root,width="120")
canvas1.create_window(100,250,window=label)
canvas1.create_window(100,450,window=label2)
canvas1.create_window(600,250,window=label3)
canvas1.create_window(600,450,window=label4)
#label.pack()
canvas1.pack()
root.after(0, update, 0)
#Server 1
Srv1=Server("Raspbery#0001","10.3.141.14","Disponible",(220,200))
Srv1.setStatus()
#
Srv2=Server("Raspbery#0002","10.3.141.88","Disponible",(220,400))
Srv2.setStatus()
#
Srv3=Server("Raspbery#0003","10.3.141.14","Disponible",(720,200))
Srv3.setStatus()
#
Srv4=Server("Raspbery#0004","10.3.141.44","Occupé",(720,400))
Srv4.setStatus()




#tk.Label(frm,text='Browse').grid(column=2, row=9)
#tk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=10)
root.mainloop()



