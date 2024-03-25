import tkinter as tk
from tkinter import filedialog
from tkinter import *

from PIL import ImageTk, Image
import numpy

# We need to load the trained model from the 'Road Traffic Sign Recognition.ipynb' as saved in the hdf5 file.
from keras.models import load_model
model = load_model('model_RTSR.h5')
# To label all the traffic signs with their respective class names, we are required to create a dictionary.
classes = {1: 'Speed limit (20km/h)',
           2: 'Speed limit (30km/h)',
           3: 'Speed limit (50km/h)',
           4: 'Speed limit (60km/h)',
           5: 'Speed limit (70km/h)',
           6: 'Speed limit (80km/h)',
           7: 'End of speed limit (80km/h)',
           8: 'Speed limit (100km/h)',
           9: 'Speed limit (120km/h)',
           10: 'No passing',
           11: 'No passing veh over 3.5 tons',
           12: 'Right-of-way at intersection',
           13: 'Priority road',
           14: 'Yield',
           15: 'Stop',
           16: 'No vehicles',
           17: 'Veh > 3.5 tons prohibited',
           18: 'No entry',
           19: 'General caution',
           20: 'Dangerous curve left',
           21: 'Dangerous curve right',
           22: 'Double curve',
           23: 'Bumpy road',
           24: 'Slippery road',
           25: 'Road narrows on the right',
           26: 'Road work',
           27: 'Traffic signals',
           28: 'Pedestrians',
           29: 'Children crossing',
           30: 'Bicycles crossing',
           31: 'Beware of ice/snow',
           32: 'Wild animals crossing',
           33: 'End speed + passing limits',
           34: 'Turn right ahead',
           35: 'Turn left ahead',
           36: 'Ahead only',
           37: 'Go straight or right',
           38: 'Go straight or left',
           39: 'Keep right',
           40: 'Keep left',
           41: 'Roundabout mandatory',
           42: 'End of no passing',
           43: 'End no passing veh > 3.5 tons'}

# Initialising the user interface.
top = tk.Tk()
top.geometry('1200x700')
top.title('Road Traffic Sign Recognition')
top.configure(background='#2F4F4F')
label = Label(top, background='#2F4F4F', font=('georgia', 20, 'bold'))
sign_image = Label(top)
resu=''

# The function defined below is used to resize the image that is selected by the user.
# Also, it displays the respective class name of the selected image by using the stored predicted data in the hdf5 file created in the 'Road Traffic Sign Recognition.ipynb'
def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((30, 30))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)

    #pred = model.predict_classes([image])[0]
    result = model.predict(image)
    #predictions = (model.predict(image) > 0.5).astype("int32")

    #sign = classes[predictions + 1]
    #print(sign)

    if result[0][0] == 1:
        resu='Speed limit (20km/h)'
    elif   result[0][1] == 1:
        resu='Speed limit (30km/h)'
    elif result[0][2] == 1:
        resu = 'Speed limit (50km/h)'
    elif result[0][3] == 1:
        resu = 'Speed limit (60km/h)'
    elif result[0][4] == 1:
        resu = 'Speed limit (70km/h)'
    elif result[0][5] == 1:
        resu = 'Speed limit (80km/h)'
    elif result[0][6] == 1:
        resu = 'End of speed limit (80km/h)'
    elif result[0][7] == 1:
        resu = 'Speed limit (100km/h)'
    elif result[0][8] == 1:
        resu = 'Speed limit (120km/h)'
    elif result[0][9] == 1:
        resu = 'No passing'
    elif result[0][10] == 1:
        resu = 'No passing veh over 3.5 tons'
    elif result[0][11] == 1:
        resu = 'Right-of-way at intersection'
    elif result[0][12] == 1:
        resu = 'Priority road'
    elif result[0][13] == 1:
        resu = 'Yield'
    elif result[0][14] == 1:
        resu = 'Stop'
    elif result[0][15] == 1:
        resu = 'No vehicles'

    elif result[0][16] == 1:
        resu = 'Veh > 3.5 tons prohibited'


    elif result[0][17] == 1:
        resu = 'No entry'
    elif result[0][18] == 1:
        resu = 'General caution'
    elif result[0][19] == 1:
        resu = 'Dangerous curve left'
    elif result[0][20] == 1:
        resu = 'Dangerous curve right'
    elif result[0][21] == 1:
        resu = 'Double curve'
    elif result[0][22] == 1:
        resu = 'Bumpy road'
    elif result[0][23] == 1:
        resu = 'Slippery road'
    elif result[0][24] == 1:
        resu = 'Road narrows on the right'
    elif result[0][25] == 1:
        resu = 'Road work'
    elif result[0][26] == 1:
        resu = 'Traffic signals'
    elif result[0][27] == 1:
        resu = 'Pedestrians'
    elif result[0][28] == 1:
        resu = 'Children crossing'
    elif result[0][29] == 1:
        resu = 'Bicycles crossing'
    elif result[0][30] == 1:
        resu = 'Beware of ice/snow'
    elif result[0][31] == 1:
        resu = 'Wild animals crossing'
    elif result[0][32] == 1:
        resu = 'End speed + passing limits'
    elif result[0][33] == 1:
        resu = 'Turn right ahead'
    elif result[0][34] == 1:
        resu = 'Turn left ahead'
    elif result[0][35] == 1:
        resu = 'Ahead only'
    elif result[0][36] == 1:
        resu = 'Go straight or right'
    elif result[0][37] == 1:
        resu = 'Go straight or left'
    elif result[0][38] == 1:
        resu = 'Keep right'
    elif result[0][39] == 1:
        resu = 'Keep left'
    elif result[0][40] == 1:
        resu = 'Roundabout mandatory'
    elif result[0][41] == 1:
        resu = 'End of no passing'
    elif result[0][42] == 1:
        resu = 'End no passing veh > 3.5 tons'


    label.configure(foreground='#FFC0CB', text=resu)


# A user interactive button is required which on trigger displays the sign.
def show_classify_button(file_path):
    classify_b = Button(top, text="Recognize the Sign ?", command=lambda: classify(file_path), padx=10, pady=10)
    classify_b.configure(background='#FEBD07', foreground='#2F4F4F', font=('georgia', 15, 'bold'))
    classify_b.place(relx=0.40, rely=0.38)


# After the user selects an image we need to upload the image on the interface.
def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width() / 2.25), (top.winfo_height() / 2.25)))
        im = ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image = im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass


# Now we need to create a user interactive button so that the user can select an image from the file path.
upload = Button(top, text="Select a traffic sign", command=upload_image, padx=10, pady=10)
upload.configure(background='#FEBD07', foreground='#2F4F4F', font=('georgia', 15, 'bold'))
upload.pack(side=BOTTOM, pady=50)
sign_image.pack(side=BOTTOM, expand=True)
label.pack(side=BOTTOM, expand=True)
heading = Label(top, text="Road Traffic Sign Recognition", pady=20, font=('georgia', 30, 'bold'))
heading.configure(background='#2F4F4F', foreground='#FFD700')
heading.pack()

# The entire code should be repeated on each instance triggered by the user. For that we use the mainloop()
top.mainloop()

# In[ ]:




