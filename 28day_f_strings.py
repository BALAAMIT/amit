letter = "hey my name is{1} and i am form {0}"
country= "india"
name ="amit"
l=letter.format(name,country)
m = letter.format(country,name)
print(m)
# print(l)
# f string look
tex = f"hey my name is {name} i am form {country}"
# tex = f"hey my name is {{name}} i am form {{country}}"
print(tex)