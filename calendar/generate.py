from PIL import Image
#Read the two images
image1 = Image.open('sidebar.png')
#image1.show()
image2 = Image.open('main.png')
#image2.show()
#resize, first image
#image1 = image1.resize((250, 480))
image1_size = image1.size
#image2 = image2.resize((398, 480))
##398
image2_size = image2.size
new_image = Image.new('RGB', (648, 480), color = 'white')
#new_image = Image.new('RGB',(2*image1_size[0], image1_size[1]), (250,250,250))
new_image.paste(image1,(0,0))
new_image.paste(image2,(image1_size[0],0))
new_image.save("calendar.png","PNG")
