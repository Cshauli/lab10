##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github
from Tkinter import *
root = Tk()
# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)
#creating the house
square = drawpad.create_rectangle(200,200,350,350, fill='red')
#creating the roof
line1 = drawpad.create_line(275,100, 200, 200)
line2 = drawpad.create_line(275, 100, 350, 200)
#door
door = drawpad.create_rectangle(265,300,290, 350, fill= 'brown')
#windows
window1 = drawpad.create_rectangle(220,220,250,250, fill = 'black')
window2 = drawpad.create_rectangle(300,220,330,250,fill = 'black')
#door handle
handle = drawpad.create_oval(277,320,286,330, fill = 'yellow')
#chimney
line3 = drawpad.create_line(295,125,295,80)
line4 = drawpad.create_line(295,80,325,80)
line5 = drawpad.create_line(325,165,325,80)
root.mainloop()






