def colorcode_pair(MAJOR_COLORS,MINOR_COLORS):
         pair_number = 1
         print("---------------------------------------------------------")
         print ("{:<21} {:<21} {:<21}".format('Pair Number','Major Color', 'Minor Color'))
         print("---------------------------------------------------------")
         for major_color in MAJOR_COLORS:
            for minor_color in MINOR_COLORS:
               print ("    {:<20} {:<21} {:<21}".format(pair_number,major_color, minor_color))
               pair_number=pair_number+1
