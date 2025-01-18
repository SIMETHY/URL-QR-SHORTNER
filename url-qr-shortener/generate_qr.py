import os
import qrcode
from tkinter import Tk
from qrcode.image.styles.moduledrawers import *
from qrcode.image.styledpil import StyledPilImage

# Initialize the Tkinter root
root = Tk()
root.withdraw()  # Hide the main window

# Chooses the QR code style
def choose_qr_style():
    st = int(input('''
Choose a QR code Style:
1. Square (Normal) 
2. Gapped Square
3. Vertical Bars
4. Horizontal Bars
5. Circles
6. Rounded
>> '''))
    style_dict = {
        1: SquareModuleDrawer(),
        2: GappedSquareModuleDrawer(),
        3: VerticalBarsDrawer(),
        4: HorizontalBarsDrawer(),
        5: CircleModuleDrawer(),
        6: RoundedModuleDrawer()
    }
    return style_dict.get(st, SquareModuleDrawer())  # Default to Square if invalid input

# QR code generation
def gen_qr(url):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
    qr.add_data(url)
    img = qr.make_image(image_factory=StyledPilImage, module_drawer=choose_qr_style())
    return img

# Saving the generated QR code
def save_qr(img):
    imgnumber = 0
    while os.path.exists(f'QR{imgnumber}.png'):
        imgnumber += 1
    img.save(f'QR{str(imgnumber)}.png')
    print(f'\nGenerated QR{imgnumber}.png on {os.getcwd()}')

# Close the Tkinter root when done
root.destroy()
