from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Green Light Signal")
        self.geometry("450x550")
        self.values = [tk.IntVar(value=0) for i in range(3)] # initialize the values to 0
        self.create_widgets()
        #self.maxsize(400,600)
        
    def create_widgets(self):
        self.toggle_btn1 = tk.Button(self, text="S3", command=lambda: self.toggle_value(0),borderwidth=6, padx=40, pady=5)
        self.toggle_btn1.grid(row=0, column=0, padx=10, pady=10)
        self.value_label1 = tk.Label(self, text="Value 1: 0")
        self.value_label1.grid(row=1, column=0, padx=10, pady=10)

        self.toggle_btn2 = tk.Button(self, text="S2", command=lambda: self.toggle_value(1),borderwidth=6, padx=40, pady=5)
        self.toggle_btn2.grid(row=0, column=1, padx=10, pady=10)
        self.value_label2 = tk.Label(self, text="Value 2: 0")
        self.value_label2.grid(row=1, column=1, padx=10, pady=10)

        self.toggle_btn3 = tk.Button(self, text="S1", command=lambda: self.toggle_value(2),borderwidth=6, padx=40, pady=5)
        self.toggle_btn3.grid(row=0, column=2, padx=10, pady=10)
        self.value_label3 = tk.Label(self, text="Value 3: 0")
        self.value_label3.grid(row=1, column=2, padx=10, pady=10)

        self.submit_btn = tk.Button(self, text="Submit", command=self.submit_values,borderwidth=6, padx=40, pady=5)
        self.submit_btn.grid(row=3, column=1, padx=15, pady=10)

        # Add the image label to display the images
        self.image_label = tk.Label(self, image=None)
        self.image_label.grid(row=4, column=1, padx=10, pady=10)

    def toggle_value(self, index):
        self.values[index].set(1 - self.values[index].get()) # toggle the value between 0 and 1
        value_label = [self.value_label1, self.value_label2, self.value_label3][index]
        value_label.config(text="Value {}: {}".format(index+1, self.values[index].get())) # update the value label

    def submit_values(self):
        abc = (self.values[0].get() << 2) + (self.values[1].get() << 1) + self.values[2].get()
        # reset the toggle buttons to 0
        for i in range(3):
            self.values[i].set(0)
        # reset the value labels to show 0
        for label in [self.value_label1, self.value_label2, self.value_label3]:
            label.config(text="Value {}: 0".format(label.grid_info()["column"] + 1))

        # update the label to display the value of abc
        value_label = tk.Label(self, text="Binary to Decimal value is: {}".format(abc))
        value_label.grid(row=5, column=1, padx=10, pady=10)


        image_dict = {
                        0: "INVALID_FINAL.png",
                        1: "B1_B2_FINAL.png",
                        2: "A1_A2_FINAL.png",
                        3: "A1_B1_FINAL.png",
                        4: "INVALID_FINAL.png",
                        5: "D1_D2_FINAL.png",
                        6: "C1_C2_FINAL.png",
                        7: "C1_D1_FINAL.png",
                         
                     }   
       
        # display the corresponding image based on the value of abc
        if   abc == 0:
            image = ImageTk.PhotoImage(Image.open("INVALID_FINAL.png"))
        elif abc == 1:
            image = ImageTk.PhotoImage(Image.open("B1_B2_FINAL.png"))
        elif abc == 2:
            image = ImageTk.PhotoImage(Image.open("A1_A2_FINAL.png"))
        elif abc == 3:
            image = ImageTk.PhotoImage(Image.open("A1_B1_FINAL.png"))
        elif abc == 4:
            image = ImageTk.PhotoImage(Image.open("INVALID_FINAL.png"))
        elif abc == 5:
            image = ImageTk.PhotoImage(Image.open("D1_D2_FINAL.png"))
        elif abc == 6:
            image = ImageTk.PhotoImage(Image.open("C1_C2_FINAL.png"))
        elif abc == 7:
            image = ImageTk.PhotoImage(Image.open("C1_D1_FINAL.png"))
        
        

        # get the filename of the image to display
        image_filename = image_dict.get(abc, "default_image.png")

        # open the image and create a PhotoImage object
        image = ImageTk.PhotoImage(Image.open(image_filename))

        # create a label to display the image
        image_label = tk.Label(self, image=image)
        image_label.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

        # keep a reference to the PhotoImage object to prevent it from being garbage collected
        #self.image = image
        image_label.config(image=image)
        image_label.image = image
app=App()
app.mainloop()    
    