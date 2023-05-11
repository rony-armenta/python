# sencence if, elif, else
'''password="root"
user="addmin"
if password == "root" and user=="admin":
    print("Credentials are correct")
elif user=="admin" and password!="root":
    print("Please, retype pass to user: " + user)
elif user!="admin" and password=="roort":
    print("Pleae re-type user rigth to:" + user)
elif user!="admin" and password!="root":
    print("please re-type user rigth to: " + user + "and pass to:" + password ) '''

#sentence while
'''unidades=1
decenas=1
producto=0

while unidades <=10:

while decenas <=10 :
    producto=unidades * decenas
    print(f"{unidades} x {decenas} = {producto}")
    decenas = decenas+1'''
   
#bucle for-in
"""nombres=['Juan', 'Antonio', 'Pedro', 'Yo']
for nombre in nombres:
    print (nombre)"""
#blucle for in range
'''base =int(input("Type a number:"))
for exponente in range(1,10):
    potencia = base ** exponente
    print(f"{base} elevado a {exponente} es {potencia}")'''

unidades=0
decenas=0
producto=0
for decenas in range(0,10):
    unidades=0
    print(f"Tabla del: {decenas}")
    while unidades <=10: 
           producto= decenas * unidades
           print(f"{decenas} x {unidades} = {producto}")
           unidades=unidades+1
