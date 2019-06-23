# imports
import cv2 # the computer vision library, from http://opencv.org/
import numpy as np # wasn't needed but is always imported in examples


class Image_Process:

    def __init__(self):
        # make it easy to modify the program to use other pictures
        self.img_path = './new_temp_pics/'
        self.img_base_name = 'Helios_1_with_dot2' 

        # ===== delete blue =====
        # import the picture
        self.distance=40000#width of image in meters
        self.time_width=5#time span is 5 seconds for an instance of image
        self.x=69
        self.y=201#185+10+10-5+2+1-2-2+1+1
        self.w=970
        self.h=370

    def cropping_images(self):
        self.img = cv2.imread(self.img_path+self.img_base_name+'.jpg')
        self.image_array=self.img[self.y:self.y+self.h,self.x:self.x+self.w]
        #print ig_array.shape
        #print img_array[54,:,:]



    def clipping_group_of_pixel(self):
        img_array=np.copy(self.image_array)

        #for i in range(100,256):
        #img=np.where(img_array[:,:,0] < 256 ) and np.where(img_array[:,:,0] >240)
        img=np.where(((img_array[:,:,0] < 256).astype(int) + (img_array[:,:,0]>240).astype(int))/2==1)
        #print img
        img_array[img[0],img[1],:]=0
        self.non_blue_pixel_coordinate=np.copy(img_array)




    def classification_of_colors_pixels_per_image(self):
        '''
        a=((img_array[:,:,2]  > 150 ).astype(int) +  (img_array[:,:,1]  >130).astype(int) +  (img_array[:,:,0]  < 50).astype(int) )/3
        b= np.where(a==0)
        #print b[0].shape
        img_array[b[0],b[1],:]=0
        #img_array[b[0],b[1],:]=255
        '''
        # note that [:,:,0] is blue, [:,:,1] is green, [:,:,2] is red
        #image_array[:,:,0] = 0
        #image_array[:,:,1] = 0
        #img_array[:,:,2] = 10
        # write the image
        self.r_span=49
        self.g_span=99
        self.b_span=39
        self.x_coordinate=self.image_array.shape[1]
        for i in range(200,260,self.r_span):
            for j in range(0,260,self.g_span):
                for k in range(0,80,self.b_span):
                    img_array=np.copy(self.image_array)
                    a=((img_array[:,:,2]  >= i ).astype(int) + \
                            (img_array[:,:,2]  < i+self.r_span ).astype(int) + \
                            (img_array[:,:,1]  >=j).astype(int) +  \
                            (img_array[:,:,1]  <j+self.g_span).astype(int) +  \
                            (img_array[:,:,0]  >= k).astype(int)  + \
                            (img_array[:,:,0]  < k+self.b_span).astype(int) )/6
                    b= np.where(a==0)
                    img_array[b[0],b[1],:]=0
                    cv2.imwrite(self.img_path+self.img_base_name+"r,g,b:"+str(i)+","+str(j)+","+str(k)+'.jpg',img_array) 
    def distance_and_time_for_high_red_pixels(self):
        img_array=np.copy(self.image_array)
        c =(((img_array[:,:,2] < 260 ).astype(int) +\
            (img_array[:,:,2] >=200 ).astype(int) +\
            (img_array[:,:,1] >=0).astype(int) +\
            (img_array[:,:,1] < self.g_span ).astype(int) +\
            (img_array[:,:,0] >= 0).astype(int)+\
            (img_array[:,:,0] < self.b_span ).astype(int) ))/6

        x_pixel_set=np.where(c==1)
        print x_pixel_set
        for x_pixel, y_pixel in zip(x_pixel_set[1],x_pixel_set[0]):
            print float(x_pixel*self.distance)/self.w, "\t",float(y_pixel*self.time_width)/self.h
        print self.image_array.shape




def main():
    image_process=Image_Process()
    image_process.cropping_images()
    image_process.classification_of_colors_pixels_per_image()
    image_process.distance_and_time_for_high_red_pixels()

if __name__=="__main__":main()
#

# ===== delete green =====
#img_array = cv2.imread(img_path+img_base_name+'.jpg') 
#img_array[:,:,1] = 0
#cv2.imwrite(img_path+img_base_name+'_no_green.jpg', image_array) 

# ===== delete red =====
#img_array = cv2.imread(img_path+img_base_name+'.jpg')
#img_array[:,:,2] = 0
#cv2.imwrite(img_path+img_base_name+'updated.jpg', img_array)

