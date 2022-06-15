
def colorcode_pair(MAJOR_COLORS,MINOR_COLORS):
         num = 1
         print("-------------------------------------------")
         print(' | ',"PARA NO.",' | ',"MAJOR",'   | ',"MINOR",'   | ')
         print("-------------------------------------------")
         for i in MAJOR_COLORS:
            for j in MINOR_COLORS:
               print(' | ',num ,'\t | ',i,'\t | ',j,'\t | ')
               num=num+1
