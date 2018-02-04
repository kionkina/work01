data = open("img.ppm", "w")

str1="P3\n"
str2="500 500\n"
str3="255\n"
list_of_lines = []
color1 = [0, 135, 171]

for i in range(250000):
    c = i / 250000.0
    r = (int)(c * 225)
    g = color1[1] 
    b = color1[2]
    list_of_lines.append(str(r) + " " + str(g) + " " + str(b) + "  ");
    

#print list_of_lines


data.write(str1)
data.write(str2)
data.write(str3)
for i in list_of_lines:
    data.writelines(i)


data.close()
