from PIL import Image
import numpy

coordinates=69,185,1050,560
a=Image.open('./Helios_1_with_dot2.jpg')
b=a.crop(coordinates)
temp_stor="./pixel_value_of_current_image.txt"
temp_file=open(temp_stor,'w')
#b.show()
list_of_pixels=list(b.getdata())
print list_of_pixel.length()
dict_pixel={}
'''
rgb=b.convert('RGB')
print rgb
for i in range(980):
    for j in range(375):
        r,g,b = rgb.getpixel((i,j))
        dict_pixel[i,j]=[r,g,b]
        st=str(i)+","+str(j)+"\t"+str(r)+","+str(g)+","+str(b)+"\n"
        temp_file.write(st)
r_high=0
b_high=0
y_high=0
tensor_dictionary={}
white_pixel=[255,255,255]
for i,j in dict_pixel.keys():
    r=dict_pixel[i,j][0]
    g=dict_pixel[i,j][1]
    b=dict_pixel[i,j][2]
    ''
    if (r in range(200,255) and b in range(0,100) and g in range(0,150)) or (r in range(130,255) and b in range(0,30) and g in range(0,30)):
        r_high+=1
    if r in range(200,255) and g in range(150,255) and b in range(0,150):
        y_high+=1
    ''
    for m in range(4):
        tensor_dictionary[m+1]={}
        tensor_dictionary[m+5]={}
    for m in range(4):
        if r in range(200+m*15,215+m*15) and g in range(0+10*m,10+10*m) and b in range(0,10):
            tensor_dictionary[m+1][i,j]=dict_pixel[i,j]
        elif r in range(200+m*15,215+m*15) and g in range(40+10*m,50+10*m) and b in range(0,10):
            tensor_dictionary[m+5][i,j]=dict_pixel[i,j]
        else:
            tensor_dictionary[m+1][i,j]=white_pixel
            tensor_dictionary[m+5][i,j]=white_pixel

for i in tensor_dictionary.keys():
    print i
#print coordinateas
print r_high,"\n",y_high
#print a
#w=list(a.getdata())
#print w
'''
