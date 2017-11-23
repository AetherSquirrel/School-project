import datetime
import easygui

USERS1=open('users.txt','r')
USERS2=open('users.txt','a+')
users1=USERS1.readlines()
for i in range(len(users1)):
    users1[i]=users1[i].split(':: ')
USERS1.close()

CARDS1=open('cards.txt','r')
CARDS2=open('cards.txt','a+')
cards1=CARDS1.readlines()
for i in range(len(cards1)):
    cards1[i]=cards1[i].split(':: ')
CARDS1.close()

OPERATIONS=open('operations.txt','a+')
operations=OPERATIONS.readlines()

BALANCE1=open('balances1.txt','r')
balance=BALANCE1.readlines()
BALANCE1.close()
#print(balance)

BALANCE2=open('balances.txt','w')

for i in range(len(balance)):
    balance[i]=balance[i].split(':: ')

user=easygui.enterbox("Input user: ")
z=1
q=[]

for i in range(len(users1)):
    if users1[i][1]==user or users1[i][1]==user+'\n':
        q.append(1)

if len(q)==0: 
    
    card=easygui.enterbox('Not registered.'+'\n'+"Input card: ")
    try: 
        s=int(card)
        z=1
    except: z=0
    while len(card)!=8 or not z: 
        easygui.msgbox('ERROR. Not a number.')
        card=easygui.enterbox("Input card: ")
        try: 
            s=int(card)
            z=1
        except: z=0        
    easygui.msgbox('OK. Creating...')
    USERS2.write(str((len(users1))+1)+':: ')
    USERS2.write(user+'\n')
    CARDS2.write(str((len(cards1))+1)+':: ')
    CARDS2.write(card+'\n')
    bal=str(0)
elif len(q)>1:
    
    card=easygui.enterbox('Oops... Do you have a clone?'+'\n'+"Input card to identificate: ")
    o=q[0]-1
    bal=balance[o][1]
else:
    o=q[0]-1
    card=cards1[o][1]
    bal=balance[o][1]
    
easygui.msgbox('OK. Wait a second...'+'\n'+'Ready to work.')

easygui.msgbox('User:'+user+'\n'+'Card:'+card+'\n'+'Balance:'+bal)

OPERATIONS.write('User: '+user+'\n')

z=easygui.enterbox('What do you want to do?'+'\n'+'"Get" + summ to get money from your card.'+'\n'+'"Get all" to get all money from your card.'+'\n'+'"Put" + summ to put money on your card.'+'\n'+'"Balance" to know your balance.'+'\n'+'"Send" + card number + summ to send your money to someone'+'"Exit" or "End" to finish work.')  
while z!='Exit' or z!='exit' or z!='end' or z!='End':
    s=z.split()
    if s[0]=='Put' or s[0]=='put':
        bal=str(int(bal)+int(s[1]))
        z=easygui.enterbox('Done. Your balance now: '+bal)
    elif z=='Get all' or z=='get all':
        bal='0'
        z=easygui.enterbox('Done. Your balance now: '+bal)
    elif s[0]=='Get' or s[0]=='get':
        if int(s[1])>int(bal):
            z=easygui.enterbox('ERROR. Money limit: '+bal)
        else:
            bal=str(int(bal)-int(s[1]))
            z=easygui.enterbox('Done. Your balance now: '+bal)
    elif s[0]=='Send' or s[0]=='send':
        bal=str(int(bal)-int(s[2]))
        z=easygui.enterbox('Done. You have sent: '+s[2]+'\n'+'Your balance now:'+bal)
        
        
        
        
    elif s[0]=='Balance':
        z=easygui.enterbox('Your balance now: '+bal)
    else:
        z=easygui.enterbox('Incorrect command.')
    now=datetime.datetime.now()
    OPERATIONS.write(z+' | '+(now.strftime("%d-%m-%Y %H:%M"))+'\n')
balance[o][1]=str(int(bal))+'\n'
for i in range(len(balance)):
    BALANCE2.write(balance[i][0]+':: '+balance[i][1])

USERS2.close()
CARDS2.close()
OPERATIONS.close()
BALANCE2.close()
BALANCEZ=open('balances1.txt','w')
for i in range(len(balance)):
    BALANCEZ.write(balance[i][0]+':: '+balance[i][1])
