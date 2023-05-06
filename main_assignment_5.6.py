from tkinter import *

# Create a window
window = Tk()

# Create a label
my_label = Label(text="Old text.")
my_label.pack()

# Change the label's text
def change_label_text():
    my_label.config(text="New text.")

# Create a button
button = Button(text="Click me!", command=change_label_text)
button.pack()

# Create an input field
input_field = Entry(width=12)
input_field.pack()

# Update the label's text with the input value
def update_label_text():
    new_text = input_field.get()
    my_label.config(text=new_text)

# Create a button to update the label's text
update_button = Button(text="Update label text", command=update_label_text)
update_button.pack()

# Run the main loop of the GUI
window.mainloop()