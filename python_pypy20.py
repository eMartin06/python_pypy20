név=None
nev_lista=[]
while név !='':
    név=input('Adj meg keresztneveket! Az enter gombbal tudsz tovább lépni. ')
    nev_lista.append(név)

nev_lista.remove('')
print(nev_lista)