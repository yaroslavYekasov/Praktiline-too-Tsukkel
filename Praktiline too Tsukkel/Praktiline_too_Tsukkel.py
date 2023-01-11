#print("Ülesanne 0")

#while 1:
#    try:
#        a = (abs(int(input("Sisesta täisarv => "))))
#        break
#    except ValueError:
#         print("See pole täisarv.")
#if a==0:
#    print("Nulliga pole mõtet midagi teha.")
#else:
#    print("Määrake, kui palju on paaris- ja mitu paaritut numbrit")
#    print()
#    c=b=a
#    paaris =0
#    paaritu = 0
#    while b > 0:
#        if b % 2 == 0:
#            paaris += 1
#        else:
#            paaritu += 1
#        b = b // 10
#print("Paaris arv:",paaris)
#print("Paaritu arv:",paaritu)

print()

print("Ülesanne 12")

print()                         

try:
    aasta =1
    skol = (int(input("Skolko vi hotite polozhit => ")))
    print("Aasta   Algsumma    Intress     Aasta lõpuks")
    for x in range (5):
        procent=int(skol/100*5)
        proc_skol=int((skol/100*5)+skol)
        print(aasta,"      ",skol,"      ",procent,"      ",proc_skol)
        aasta +=1
        skol +=procent
except:
    print("errror")
    

#10
#x=1
#while x<=100:
#    if x%5==0:
#        print(x, end=" ")
#    x+=1



