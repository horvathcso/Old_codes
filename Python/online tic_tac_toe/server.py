# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:35:02 2020

@author: Csoni
"""
##Amőba config, tabla setup
teruletmeret=25
hany_nyer=4



#pubnub
"""
try:
    import graphic
except:
    print("Failed")
"""  
import os
import sys
from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from texttable import Texttable

#pub config
pnconfig = PNConfiguration()
pnconfig.subscribe_key = "****"
pnconfig.publish_key = "****"
pnconfig.uuid = "serverUUID-SUB"

pubnub = PubNub(pnconfig)
CHANNEL_lis = "the_guide"
CHANNEL_send = "send"
global atvitel
atvitel=""
oldatvitel=""
ENTRY="SERVER"


class MySubscribeCallback(SubscribeCallback):
  def presence(self, pubnub, event):
      pass
    #print("[PRESENCE: {}]".format(event.event))
    #print("uuid: {}, channel: {}".format(event.uuid, event.channel))

  def status(self, pubnub, event):
    if event.category == PNStatusCategory.PNConnectedCategory:
      pass
      #print("[STATUS: PNConnectedCategory]")
      #print("connected to channels: {}".format(event.affected_channels))

  def message(self, pubnub, event):
      pass
    #print("[MESSAGE received]")

      if event.message["update"] == "q":
          print("A másik játékos kilépett.")
          #sys.exit()
          global kilepes
          kilepes=False
          global jatekoskarakter
          jatekoskarakter=" "
          global rerun2
          rerun2=False
          
      else:
          #print("{}: {}".format(event.publisher, event.message["update"]))
          global atvitel
          atvitel=event.message["update"]
          #print(atvitel)
      
pubnub.add_listener(MySubscribeCallback())
pubnub.subscribe().channels(CHANNEL_lis).with_presence().execute()

def clr_consol_buffer():
    if os.name=="posix":
        from termios import tcflush, TCIFLUSH
        tcflush(sys.stdin, TCIFLUSH)
    elif os.name=="nt":
        im10port msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()

def print_table(sorok):
    print('\033[H\033[J')
    t=Texttable()
    t.__init__( max_width=0)
    t.add_rows(sorok,False)
    print(t.draw())
 
def karaktercsere(karakter):
    if karakter == 'O':
        print("Az X jön")
        return 'X'
    elif karakter == 'X': 
        print("Az O jön")
        return 'O'
#"""
def nyert_valaki(tabla):
    global teruletmeret
    global hany_nyer
    for i in range (teruletmeret-hany_nyer):
        for j in range (teruletmeret-hany_nyer):
            
            osszehas_jobb=0
            osszehas_le=0
            osszehas_jl=0
            osszehas_bl=0
            
            for k in range (hany_nyer):
                if tabla[i+1][j+1]==tabla[i+1+k][j+1] and tabla[i+1][j+1] != ' ':
                    osszehas_le +=1
                if tabla[i+1][j+1]==tabla[i+1][j+1+k]and tabla[i+1][j+1] != ' ':
                    osszehas_jobb +=1
                if tabla[i+1][j+1]==tabla[i+1+k][j+1+k]and tabla[i+1][j+1] != ' ':
                    osszehas_jl +=1
                if tabla[i+hany_nyer][j+1]==tabla[i+hany_nyer-k][j+1+k] and tabla[i+hany_nyer][j+1] != ' ':
                    osszehas_bl +=1
            if osszehas_bl==hany_nyer:
                print("Nyert a " +tabla[i+1][j+hany_nyer-1]+ " jatékos")
                return False
            elif osszehas_jl==hany_nyer:
                print("Nyert a " +tabla[i+1][j+1]+ " jatékos")
                return False
            elif osszehas_le==hany_nyer:
                print("Nyert a " +tabla[i+1][j+1]+ " jatékos")
                return False
            elif osszehas_jobb==hany_nyer:
                print("Nyert a " +tabla[i+1][j+1]+ " jatékos")
                return False
            
    for i in range(teruletmeret-hany_nyer,teruletmeret-1):
        for j in range (teruletmeret-hany_nyer):
            osszehas_jobb=0
            osszehas_le=0
            for k in range (hany_nyer):
                if tabla[j+1][i+1]==tabla[j+1+k][i+1] and tabla[j+1][i+1] !=' ':
                    osszehas_le+=1
                if tabla[i+1][j+1]==tabla[i+1][j+1+k] and tabla[i+1][j+1] !=' ':
                    osszehas_jobb+=1
            if osszehas_le==hany_nyer:
                print("Nyert a " +tabla[i+1][j+1]+ " jatékos")
                return False
            elif osszehas_jobb==hany_nyer:
                print("Nyert a " +tabla[i+1][j+1]+ " jatékos")
                return False
    return True
            
"""            


def nyert_valaki(tabla):
    for i in range (3):
        if tabla[i+1][1]==tabla[i+1][2]==tabla[i+1][3] != ' ':
            print("Nyert a " +tabla[i+1][1]+ " jatékos")
            return False
        elif tabla[3][i]==tabla[1][i]==tabla[2][i] !=' ':
            print("Nyert a " +tabla[1][i]+ " jatékos")
            return False
        elif tabla[1][1]==tabla[2][2]==tabla[3][3] !=' ':
            print("Nyert a " +tabla[2][2]+ " jatékos")
            return False
        elif tabla[1][3]==tabla[2][2]==tabla[3][1] !=' ':
            print("Nyert a " +tabla[2][2]+ " jatékos")
            return False
    return True
"""    
    
def input_elhelyezese (table, bemenet, karakter):
    oszlop=ord(bemenet[0])-96
    global szam
    sor=szam
    if table[sor][oszlop]==' ':
        table[sor][oszlop]=karakter
    else:
        print("Már van elem ezen a mezőn. Adj meg másikat.")
        bemenet=str(input()).lower()
        while input_is_valid(bemenet)==False and bemenet!='q':
            pass
        if bemenet=='q':
            print("Kilépés")
            the_message = {"entry": ENTRY, "update": 'q',"hany_nyer": hany_nyer, "teruletmeret": teruletmeret}
            envelope = pubnub.publish().channel(CHANNEL_send).message(the_message).sync()
            sys.exit()
        else:
            input_elhelyezese(table,bemenet,karakter)


def input_is_valid(beolvas):
    global teruletmeret
    global szam
    szam=0
    for i in range(len(beolvas)-1):
        if ord(beolvas[i+1]) in range(48,58):
            szam=szam+int(beolvas[i+1])*pow(10,(len(beolvas)-i-2))
        else:
            print("Itt false")
            return False
    #print(szam)
    if (ord(beolvas[0]))>=97 and ord(beolvas[0])<(97+teruletmeret) and szam>0 and szam<(teruletmeret):
        return True
    else:
        return False
        
def beolvas_szam ():
    try:
            return int(input())
    except:
        print("Egy nem 0 számot adj meg")
        return beolvas_szam()
    
def beolvas_szam_0_1 ():
    beolvas=input()
    if len(beolvas)==1:
        if ord(beolvas)==48 or ord(beolvas)==49:
            return int(beolvas)
        else:
            print("0-át vagy 1-et adj meg")
            return beolvas_szam_0_1 ()
    else:
        print("0-át vagy 1-et adj meg")
        return beolvas_szam_0_1 ()

#set up
print("Add meg a játék paramétereit:")
print("A tábla mérete:")
teruletmeret=beolvas_szam()+1

print("Add meg, hány keljen egy sorban a győzelemhez (ne legyen nagyobb, mint a táblaméret):")
hany_nyer=beolvas_szam()
while hany_nyer>=teruletmeret:
    print("Túl nagy számot adtál meg. Add meg, hány keljen egy sorban a győzelemhez (ne legyen nagyobb, mint a táblaméret):")
    hany_nyer=beolvas_szam()

print("Add meg hogy ki kezd (0, ha te, 1, ha a másik játékos):")
kikezd=beolvas_szam_0_1()

#init table and set ups
table=[[None] for i in range(teruletmeret)]
for i in range(teruletmeret-1):
    table[0].append(chr(65+i))    
for i in range(teruletmeret-1):
    table[i+1][0]=i+1
    for j in range(teruletmeret-1):
        table[j+1].append(' ')
table[0][0]=":)"


jatekoskarakter_serv='O'
jatekoskarakter_kliens='X'
if kikezd==1:
    jatekoskarakter_serv='X'
    jatekoskarakter_kliens='O'

# comunicate setups
the_message = {"hany_nyer": hany_nyer, "teruletmeret": teruletmeret, "update": kikezd}
envelope = pubnub.publish().channel(CHANNEL_send).message(the_message).sync()



print_table(table)
print("Tic-Tac-Toe server mode. To Quite enter q. To make a move enter the cell's name. Good luck")
kilepes=True
jatekoskarakter='O'
rerun=False



# Game
while kilepes==True:
   
    #itteni adatbemenet:
    if jatekoskarakter==jatekoskarakter_serv:
        beolvas=""        
        clr_consol_buffer()
        print("Your turn pleas enter a valid coordinate:")
        beolvas=str(input())
        while beolvas =="":
            print("Nem sikeres beolvasás, add meg újra a parancsot")
            beolvas=str(input())
            
        beolvas=beolvas.lower()
        
        
        valid=input_is_valid(beolvas)
        #print(valid)
        if valid==True:
            input_elhelyezese(table,beolvas,jatekoskarakter)
             #print('\033[H\033[J')
            print_table(table)
            jatekoskarakter=karaktercsere(jatekoskarakter)
            kilepes=nyert_valaki(table)
            rerun=False
        elif beolvas.lower()=='q':
            the_message = {"entry": ENTRY, "update": 'q',"hany_nyer": hany_nyer, "teruletmeret": teruletmeret}
            envelope = pubnub.publish().channel(CHANNEL_send).message(the_message).sync()
            kilepes = False
            rerun=True
        else:
            print("Helytelen bemenet")
            rerun=True
            
        # táblaküldés    
        if rerun==False:
            the_message = {"entry": ENTRY, "update": table, "hany_nyer": hany_nyer, "teruletmeret": teruletmeret}
            envelope = pubnub.publish().channel(CHANNEL_send).message(the_message).sync()
        else:
            rerun=False
        
    #fogadott adat    
    elif jatekoskarakter==jatekoskarakter_kliens and kilepes==True: 
        print("Waiting for client turn...")
        rerun=False
        rerun2=True
        while rerun2==True:
            if atvitel != oldatvitel:
                beolvas = atvitel
                if beolvas=='q':
                    kilepes=False
                #print(beolvas)
                szam=beolvas[1]
                input_elhelyezese(table,beolvas,jatekoskarakter)
                #print('\033[H\033[J')
                print_table(table)
                jatekoskarakter=karaktercsere(jatekoskarakter)
                kilepes=nyert_valaki(table)
                rerun2=False
                oldatvitel=atvitel
            else:
                rerun2=True
    
        # táblaküldés    
        if rerun==False:
            the_message = {"entry": ENTRY, "update": table, "hany_nyer": hany_nyer, "teruletmeret": teruletmeret}
            envelope = pubnub.publish().channel(CHANNEL_send).message(the_message).sync()
        else:
            rerun=False