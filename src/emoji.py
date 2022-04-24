import tkinter as tk
from tkinter import *
import cv2
from PIL import Image, ImageTk
import os
import numpy as np
import cv2
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.optimizers import adam_v2
from keras.layers import MaxPooling2D
from keras_preprocessing.image import ImageDataGenerator
import threading

emotion_model = Sequential()
emotion_model.add(Conv2D(32, kernel_size=(3,3), activation='relu', input_shape=(48,48,1)))
emotion_model.add(Conv2D(64, kernel_size=(3,3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2,2)))
emotion_model.add(Dropout(0.25))
emotion_model.add(Conv2D(128, kernel_size=(3,3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2,2)))
emotion_model.add(Dropout(0.25))
emotion_model.add(Flatten())
emotion_model.add(Dense(1024, activation='relu'))
emotion_model.add(Dropout(0.5))
emotion_model.add(Dense(7, activation='softmax'))
emotion_model.load_weights('model.h5')
cv2.ocl.setUseOpenCL(False)

emotion_dict = {
    0: "Angry",
    1: "Disgusted",
    2: "Fear",
    3: "Happy",
    4: "Neutral",
    5: "Sad"
}

cur_path = os.path.dirname(os.path.abspath(__file__))

emoji_dict={
    0:cur_path+"/emoji/Angry.png",
    1:cur_path+"/emoji/Disgusted.png",
    2:cur_path+"/emoji/Fear.png",
    3:cur_path+"/emoji/Happy.png",
    4:cur_path+"/emoji/Neutral.png",
    5:cur_path+"/emoji/Sad.png"
}

global last_frame1
last_frame1 = np.zeros((480,640,3), dtype=uint8)
global cap1
show_text=[0]
global frame_number


def show_subject():
    pass











if __name__ == "__main__":
    frame_number = 0
    root = tk.Tk()
    lmain = tk.Label(master=root,padx=50,bd=10)
    lmain2 = tk.Label(master=root,bd=10)
    lmain3 = tk.Label(master=root,bd=10,fg="#CDCDCD",bg='black')
    lmain.pack(side=LEFT)
    lmain.place(x=50,y=250)
    lmain3.pack()
    lmain3.place(x=960,y=250)
    lmain2.pack(side=RIGHT)
    lmain2.place(x=900,y=350)

    root.title("Photo To Emoji")
    root.geometry("1400x900+100+10")
    root['bg']='black'
    exitButton = Button(root, text='Quit',fg='red',command=root.destroy,font=('arial',25,'bold')).pack(side=BOTTOM)
    threading.Thread(target=show_subject).start()
    threading.Thread(target=show_avatar).start()
    root.mainloop()






