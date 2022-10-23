# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:37:31 2020

@author: Csoni
"""

teruletmeret=""
hany_nyer=""


#pubnub
import os
import sys
from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
#pub config
pnconfig = PNConfiguration()
pnconfig.subscribe_key = "****"
pnconfig.publish_key = "****"
pnconfig.uuid = "serverUUID-SUB"

ENTRY="Client"
pubnub = PubNub(pnconfig)
CHANNEL_lis = "send"
CHANNEL_send = "the_guide"
atvitel=""
verziold=0
verzuj=0
fut=True




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
    #print("[MESSAGE received]")
    global verzuj
    if event.message["update"] == "q":
      print("A másik játékos kilépett.")
      global fut
      fut=False
      verzuj=verzuj+1
    else:
      #print("{}: {}".format(event.publisher, event.message["update"]))
      global atvitel
      atvitel=event.message["update"]
      verzuj=verzuj+1
      global teruletmeret
      teruletmeret=event.message["teruletmeret"]
      global hany_nyer
      hany_nyer=event.message["hany_nyer"]
     
      
pubnub.add_listener(MySubscribeCallback())
pubnub.subscribe().channels(CHANNEL_lis).with_presence().execute()




from texttable import Texttable


def clr_consol_buffer():
    if os.name=="posix":
        from termios import tcflush, TCIFLUSH
        tcflush(sys.stdin, TCIFLUSH)
    elif os.name=="nt":
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()

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

def print_table(sorok):
    print('\033[H\033[J')
    t=Texttable()
    t.__init__( max_width=0)
    t.add_rows(sorok,False)
    print(t.draw())
    
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
    print(szam)
    print(ord(beolvas[0]))
    if (ord(beolvas[0]))>=97 and ord(beolvas[0])<(97+teruletmeret) and szam>0 and szam<(teruletmeret):
        return True
    else:
        return False
    
def input_kezeles(tabla):
    clr_consol_buffer()
    beolvas=""
    print("Your turn pleas enter a valid coordinate:")
    beolvas=str(input())
    while beolvas =="":
        print("Nem sikeres beolvasás, add meg újra a parancsot")
        beolvas=str(input())
    beolvas=beolvas.lower()
    
    if input_is_valid(beolvas)==True:
        oszlop=ord(beolvas[0])-96
        global szam
        sor=szam
        if tabla[sor][oszlop]==' ':  
            global verziold
            global verzuj
            verziold=verzuj
            the_message = {"entry": ENTRY, "update": [chr(oszlop+96),szam]}
            envelope = pubnub.publish().channel(CHANNEL_send).message(the_message).sync()
            while verziold==verzuj:
                pass
            table=atvitel
            #print('\033[H\033[J')
            print_table(table)
            
            return nyert_valaki(table)
        else:
            print("Már van ezen a mezőn")
            return input_kezeles(tabla)
    elif beolvas=='q':
        the_message = {"entry": ENTRY, "update": 'q'}
        envelope = pubnub.publish().channel(CHANNEL_send).message(the_message).sync()
        return False
    else :
        print("Helytelen bemenet")
        return input_kezeles(tabla)
    
    
#setups fogadasa
print("Várakozás, hogy a másik játékos megadja a játékparamétereket...")
while teruletmeret=="" or hany_nyer=="":
    pass
kikezd=atvitel

table=[[None] for i in range(teruletmeret)]
for i in range(teruletmeret-1):
    table[0].append(chr(65+i))    
for i in range(teruletmeret-1):
    table[i+1][0]=i+1
    for j in range(teruletmeret-1):
        table[j+1].append(' ')
table[0][0]=":)"
        
    
print_table(table)
print("Amőba játék. Irányítás: kilépéshez a saját körödben adj meg egy q-t, a jelölőd elhelyezéséhez, pedig a cella koordinátáit betű szám (pl: A1)")
print("A játék megnyeréséhez ", hany_nyer, " korong kell egymás mellett.")
if kikezd==0:
    print("A másik játékos kezd. ")
    while fut==True:
        print("Várakozás a másik játékos lépésére...")
        verziold=verzuj
       # if atvitel !="":
        #    table=atvitel
        #print('\033[H\033[J')
        while verziold==verzuj:
            pass
        if fut==True:
            table=atvitel
            print_table(table)
            fut=nyert_valaki(table)
            if fut==True :
                fut=input_kezeles(table)
                
else:
    print("Te kezdesz. ")
    
    while fut==True:
        fut=input_kezeles(table)
        print("Várakozás a másik játékos lépésére...")
        verziold=verzuj
       # if atvitel !="":
        #    table=atvitel
        #print('\033[H\033[J')
        while verziold==verzuj:
            pass
        if fut==True:
            table=atvitel
            print_table(table)
            fut=nyert_valaki(table)
        