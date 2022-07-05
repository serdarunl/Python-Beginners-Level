def asal_mi(sayı):
     if(sayı == 1):
         return False
     elif(sayı == 2):
        return True
     else:
        for i in range(2,sayı):
            if(sayı % i == 0):
                return False
            return True


while True:
     sayı  = input("Lütfen bir sayı giriniz:")
     if(sayı == "q" ):
         print("Çıkış Yaptınız...")
         break
     else:
         sayı = int(sayı)
         if(asal_mi(sayı)):
            print("{} bir asal sayıdır".format(sayı))
         else:
             print(" {} bir asal sayı değildir".format(sayı))
