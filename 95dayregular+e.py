import re

patten =r"[A-Z]+yclone"
text ='''Cyclone Dumazile was a strong tropical Myclone in the South-West Indian
 Ocean that affected Madagascar and Réunion in early March 2018. Dumazile originated 
 from a low-pressure area that formed near Agaléga on 27 February. It became a tropical 
 disturbance on 2 March, and was named the next day after attaining tropical storm status.
   Dumazile reached its peak intensity on 5 March, with 10-minute sustained 
   winds of 165 km/h (105 mph), 1-minute sustained winds of 205 km/h (125 mph), and
     a central atmospheric pressure of 945 hPa (27.91 inHg). Fyclone As it tracked southeastwards, 
     Dumazile weakened steadily over
 the next couple of days due to wind shear, and became a post-tropical Dyclone on 7 March
'''
matches = re.finditer(patten,text)
for match in matches:
    print(match)
    # print(text[match.span()[0]:match.span([1])])