from datetime import date
menu="""
1.xerci elave et 
    kateqoriya
       a.erzaq
       b.yol
       c.komunal
2.Proqramdan cix"""
xert=0
while True:
    print(menu)
    secim=input('ne etmek isteyirsen?:')
    if secim=='1':
        mebleg=input('ne qeder xerclemisen?:')
        kategoriya=input('kategoriya:')
        daxil = str(input('Tarixi qeyd et(yyyy-mm-dd): '))
        
        
        xercs={
            'xerclenen':mebleg,
             'tarix':daxil
        }
        xert+=1        
        if kategoriya=='a':
            file=open('xerc.txt','a')
            file.write(f'{xert}:{xercs["xerclenen"]} AZN {xercs["tarix"]}  tarixinde erzaqa xerc olunub  \n')
        elif kategoriya=='b':
            file=open('xerc.txt','a')
            file.write(f'{xert}:{xercs["xerclenen"]} AZN {xercs["tarix"]}  tarixinde yola xerc olunub \n')
        elif kategoriya=='c':
            file=open('xerc.txt','a')
            file.write(f'{xert}:{xercs["xerclenen"]} AZN {xercs["tarix"]}  tarixinde komunala xerc olunub \n')
            
    elif secim=='2':
        break
            