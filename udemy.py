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
'''multiplicando=1
multiplicador=1
producto=0

while multiplicando <=10:

while multiplicador <=10 :
    producto=multiplicando * multiplicador
    print(f"{multiplicando} x {multiplicador} = {producto}")
    multiplicador = multiplicador+1'''
   
#bucle for-in
"""nombres=['Juan', 'Antonio', 'Pedro', 'Yo']
for nombre in nombres:
    print (nombre)"""
#blucle for in range
'''base =int(input("Type a number:"))
for exponente in range(1,10):
    potencia = base ** exponente
    print(f"{base} elevado a {exponente} es {potencia}")'''

multiplicando=0 #int(input("Type a number to 0 from 9:3"))
multiplicador=0
producto=int
for multipicando in range(0,11):
    print(f"Resultado for {multiplicando}")
    #print(multipicando)
    while multiplicador <=10:      
           producto= multiplicando * multiplicador
           print(f"{multiplicando} x {multiplicando} = {producto}")
           #print(f"Resultado 1 {multiplicando}")
           #print(f"Resultado 2 {multiplicador}")
           #print(f"Resultado 3 {multiplo}")
           multiplicador = multiplicador+1
