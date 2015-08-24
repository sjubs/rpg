from PIL import Image
from tkinter import *

from tkinter import *
master = Tk()

canvas_width = 480
canvas_height = 480
w = Canvas(master, 
           width=canvas_width,
           height=canvas_height,
           bg="#d3d3d3")
w.pack()

y_offset = canvas_height * 0.95;
x_offset = canvas_width * 0.05;
ear_size = canvas_width * 0.3;

# draw two ears
x0 = x_offset
y0 = canvas_height - y_offset
x1 = x0 + ear_size
y1 = y0 + ear_size
w.create_oval(
   x0, 
   y0,
   x1,
   y1,
   fill = "#000000")

x0 = canvas_width - ear_size - x_offset
y0 = canvas_height - y_offset
x1 = x0 + ear_size
y1 = y0 + ear_size
w.create_oval(
   x0, 
   y0,
   x1,
   y1,
   fill = "#000000")

# draw face
face_size = canvas_width * 0.8
x0 = (canvas_width - face_size) / 2
y0 = canvas_height - y_offset
x1 = x0 + face_size
y1 = y0 + face_size
w.create_oval(
   x0, 
   y0,
   x1,
   y1,
   fill = "#ffffff",
   outline="#ffffff")


# draw two eyes
y_offset = canvas_height * 0.8;
x_offset = canvas_width * 0.25;
eye_w = canvas_width * 0.2;
eye_h = eye_w * 1.62

x0 = x_offset
y0 = canvas_height - y_offset
x1 = x0 + eye_w
y1 = y0 + eye_h
w.create_oval(
   x0, 
   y0,
   x1,
   y1,
   fill = "#000000")

x0 = canvas_width - eye_w - x_offset
y0 = canvas_height - y_offset
x1 = x0 + eye_w
y1 = y0 + eye_h
w.create_oval(
   x0, 
   y0,
   x1,
   y1,
   fill = "#000000")

# draw whites of eyes
y_offset = canvas_height * 0.6;
x_offset = canvas_width * 0.33;
eye_w = canvas_width * 0.08;
eye_h = eye_w 

x0 = x_offset
y0 = canvas_height - y_offset
x1 = x0 + eye_w
y1 = y0 + eye_h
w.create_oval(
   x0, 
   y0,
   x1,
   y1,
   fill = "#ffffff")

x0 = canvas_width - eye_w - x_offset
y0 = canvas_height - y_offset
x1 = x0 + eye_w
y1 = y0 + eye_h
w.create_oval(
   x0, 
   y0,
   x1,
   y1,
   fill = "#ffffff")

# draw pupils
y_offset = canvas_height * 0.6 - (eye_h / 2);
x_offset = canvas_width * 0.36;
eye_w = canvas_width * 0.03;
eye_h = eye_w 

x0 = x_offset
y0 = canvas_height - y_offset
x1 = x0 + eye_w
y1 = y0 + eye_h
w.create_oval(
   x0, 
   y0,
   x1,
   y1,
   fill = "#000000")

x0 = canvas_width - eye_w - x_offset
y0 = canvas_height - y_offset
x1 = x0 + eye_w
y1 = y0 + eye_h
w.create_oval(
   x0, 
   y0,
   x1,
   y1,
   fill = "#000000")


mainloop()