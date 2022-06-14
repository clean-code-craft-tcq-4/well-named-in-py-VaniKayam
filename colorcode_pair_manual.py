import colorcode_pair_conversions

#Print the Header
print ("Pair Number to pair(Major/Minor Color) conversion table:\n")
print ("{:<21} {:<21} {:<21}".format('Pair Number','Major Color', 'Minor Color'))

#Print the contents for Color code manual
for major_color in colorcode_pair_conversions.major_colors:
  for minor_color in colorcode_pair_conversions.minor_colors:
    pair_number = colorcode_pair_conversions.get_pair_number_from_color(major_color,minor_color)
    print ("    {:<19} {:<21} {:<20}".format(pair_number, major_color, minor_color))
