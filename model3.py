import numpy as np

from removeColor import Image_Process





class Recurrent_neural_network:

    



    def passing_image(self,image_process):
        print "instance created"
        self.time_instance=image_process.h
        self.image_width=image_process.w





    def rnn_on_events_from_image(self,image_process):
        img_copy=np.copy(image_process.non_blue_pixel_coordinate)
        events=self.event_pixel_filtering(img_copy)
        #for event in events:
        #    self.rnn_on_rectangular_event(event)






    def event_pixel_filtering(self,img_copy):
        events=[]#events initialized as emoty list
        index_non_zero= np.argwhere(img_copy!=0)
        dictionary={}
        for item in index_non_zero:
            #print item
            #print item[0],item[1]
            if item[0] in dictionary.keys():
                dictionary[item[0]].append(item[1])
            else:
                dictionary[item[0]]=[]
            #print dictionary[item[0]]
        
        for i in range(self.image_width):
            for j in range(self.time_instance):
                print i, j
    
        '''
        x_1=x_2=y_1=y_2=0
        counter=0
        for item in index_non_zero:
            if x_2 != item[0]:
                if counter != 3:
                    x_2=item[0]
                    #y_1=min(y_1,item[0])
                    y_1=min(y_1,item[1])
                    y_2=max(y_2,item[1])
                    counter+=1
                else:
                    counter=0
                    x_2=item[0]
                    y_1=min(y_1,item[1])
                    y_2=max(y_2,item[1])
                    list_t=[]
                    list_t.append(x_1)
                    list_t.append(x_2)
                    list_t.append(y_1)
                    list_t.append(y_2)
                    events.append(list_t)
            else:
                x_2=x_1
        ''
        ''
        non_zero_pixels=np.where(img_copy!=0)
        zero_pixels=np.where(img_copy==0)
        zero_pixel_transpose=np.where(img_copy.transpose()==0)
        zero_transpose_column_dictionary={}
        for i in range(zero_pixel_transpose[0].size):
            if zero_pixel_transpose[0][i] in zero_transpose_column_dictionary.keys():
                zero_transpose_column_dictionary[zero_pixel_transpose[0][i]].append(zero_pixel_transpose[1][i])
            else:
                zero_transpose_column_dictionary[zero_pixel_transpose[0][i]]=[]
                zero_transpose_column_dictionary[zero_pixel_transpose[0][i]].append(zero_pixel_transpose[1][i])
        for item in  zero_transpose_column_dictionary:
            
            if zero_transpose_column_dictionary[item]
        non_zero_dictionary={}
        zero_dictionary={}
        for i in non_zero_pixels[0]:
            
        #algorithm to identify rectangular group of pixels
        '''
        return events

    #def rnn_on_rectangular_event(self,event):
        #rnn applied on event

def main():
    image_process=Image_Process()
    image_process.cropping_images()
    rnn=Recurrent_neural_network()
    rnn.passing_image(image_process)#image_process)
    #image_process.classification_of_colors_pixels_per_image() 
    #image_process.distance_and_time_for_high_red_pixels() 
    image_process.clipping_group_of_pixel()
    #training phase
    rnn.rnn_on_events_from_image(image_process)

if __name__=="__main__":main()
