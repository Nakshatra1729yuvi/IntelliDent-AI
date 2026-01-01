import cv2

img_data={}


for i in range(10):
    img_path=f'D:\\IntelliDent AI\\Task 3\\Images\\{i+1}.jpg'  #Loading Image
    img=cv2.imread(img_path)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #Converting to Grayscale

    lap_var=cv2.Laplacian(gray,cv2.CV_64F).var()  #Calculating Variance of Laplacian for Blurriness
    brightness=gray.mean()  #Calculating Mean Intensity of pixels for Brightness
    contrast=gray.std()     #Calculating Standard Deviation of pixels for Contrast

    is_blur=lap_var<200
    is_bright=brightness>100
    is_contrast=contrast>50

    is_good_quality=not is_blur and is_bright and is_contrast  #Determining Overall Quality

    blurriness="blurry" if is_blur else "not blurry"   
    brightness="bright" if is_bright else "not bright"
    contrast="high" if is_contrast else "low"
    quality="good quality" if is_good_quality else "poor quality"
    
    img_data[i+1] = {
        'blurriness': blurriness,
        'brightness': brightness,
        'contrast': contrast,
        'quality': quality
    }                                    #Storing results in dictionary

for key, value in img_data.items():    #Printing results
    print(f"Image {key}: Blurriness - {value['blurriness']}, Brightness - {value['brightness']}, Contrast - {value['contrast']}, Quality - {value['quality']}")


with open('D:\\IntelliDent AI\\Task 3\\results\\results.txt', 'w') as file:      #Writing results to a text file
    for key, value in img_data.items():
        file.write(f"Image {key}: Blurriness - {value['blurriness']}, Brightness - {value['brightness']}, Contrast - {value['contrast']}, Quality - {value['quality']}\n")

