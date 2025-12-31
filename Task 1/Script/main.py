import cv2

f=open('D:\IntelliDent AI\Task 1\Printed_Stats\info.txt','w')   #Opening a file 

img_data={}

for i in range(12):

    image=cv2.imread(f'D:\\IntelliDent AI\\Task 1\\Images\\{i+1}.jpg') #Reading images 

    gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #Converting to grayscale

    gray_image_resized=cv2.resize(gray_image,(500,500)) #Resizing to 500x500

    cv2.imwrite(f'D:\\IntelliDent AI\\Task 1\\Processed_Images\\gray_resized_{i+1}.jpg',gray_image_resized) #Saving processed images

    img_data[f'img{i+1}']={'resolution':gray_image_resized.shape,'mean_intensity':gray_image_resized.mean()} #Storing image data

    f.write(f'img{i+1}:\nResolution: {gray_image_resized.shape}\nMean Intensity: {gray_image_resized.mean()}\n\n') #Writing data to file

f.close()   #Closing the file

for key,value in img_data.items():
    print(f'{key}: Resolution={value["resolution"]}, Mean Intensity={value["mean_intensity"]}\n')  #Printing data of images