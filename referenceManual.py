def colorcode_pair(MAJOR_COLORS,MINOR_COLORS):
         pairNumber = 1
         print("---------------------------------------------------------")
         print ("{:<21} {:<21} {:<21}".format('Pair Number','Major Color', 'Minor Color'))
         print("---------------------------------------------------------")
         for major_color in MAJOR_COLORS:
            for minor_color in MINOR_COLORS:
               print ("    {:<20} {:<21} {:<21}".format(pairNumber,major_color, minor_color))
               pairNumber=pairNumber+1
