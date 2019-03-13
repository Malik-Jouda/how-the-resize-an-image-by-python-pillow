#how the resize an image by python => pillow
# install: pip install Pillow
# import Image

from PIL import Image

image = input("Enter The Image : ")

# Open The Image
image = Image.open(image)

# show The old Image
image.show()

Width = int(input("Enter The Width Of The Image : "))
Height = int(input("Enter The Height Of The Image : "))

# img.resize(Width , Height)
new_img = image.resize((Width,Height))

# Save Image
new_img.save('result.jpg')

# show The new Image
new_img.show()
