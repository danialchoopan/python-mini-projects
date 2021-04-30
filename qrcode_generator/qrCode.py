
import qrcode
import qrcode.image.svg as svgImage 
png = False
svg = False
# get user information 
firstname = input('enter your firstname: ')
lastname = input('enter your lastname: ')
phone = input('enter your phone: ')
website = input('enter your website URL: ')
print ('***************************')

print ("You want save PNG or SVG ?")
print ("1) PNG")
print ("2) SVG")
image_type = int(input('=>'))


if image_type == 1: 
    png = True
if image_type == 2:
    svg = True

filename = input('enter filename: ')



qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)

qr.add_data("name: " + firstname + "\n")
qr.add_data("lastname: " + lastname + "\n")
qr.add_data("phone: " + phone + "\n")
qr.add_data("website: " + website + "\n")
qr.make(fit=True)
if png == True:
    img = qr.make_image(fill='black', back_color='white')
    img.save(filename + ".png")

if svg == True: 
    img = qr.make_image(fill_color='black', back_color='white', image_factory=svgImage.SvgImage)
    img.save(filename + ".svg")