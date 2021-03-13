# improt enquiries for create menu 
import enquiries

# define menu options 
options = ['Draw Rectangle', 'Draw Square']

# show options 
choice = enquiries.choose('Select what you want draw:', options)

# logic for Draw Rectangle 

if(choice == "Draw Rectangle"):
  width = int(input("Enter the width of your rectangle: (insert value here): "))
  height = int(input("Enter the height of your rectangle: (insert value here): "))
  for h in range(0, height):
    print(" * " * width)

# logic for Draw Square 
if(choice == "Draw Square"):
  leng = int(input("Enter square size: "))
  for h in range(0, leng):
    print(" * " * leng)
      

