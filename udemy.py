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

multiplicando=0
multiplicador=0
producto=0
for multiplicando in range(0,10):
    multiplicando=multiplicando+1
    multiplicador = multiplicador+1
    #print(f"result for {multiplicador}")    
    print(multiplicando)
    while multiplicador <=10 and multiplicando <= 10:      
           producto= multiplicando * multiplicador
           print(f"{multiplicando} x {multiplicador} = {producto}")
           #multiplicador = multiplicador+1
           multiplicando=multiplicando+1
