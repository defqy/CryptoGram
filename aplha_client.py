#It's only prototype of app

# from tkinter import *
# from tkinter import ttk

# main = Tk()
# #canvas = Canvas(width=500, height=500)

# main.geometry('500x500')
# main.update_idletasks()
# main.title('Cryptor v1.0')

# # label = ttk.Label(text = 'Cryptor v1.0', font = ('Arial', 14))
# # label.pack()

# entry = ttk.Entry()
# id_var = StringVar()
# length_var = StringVar()
# key_var = StringVar()

# id = Label(text = 'Enter id of your oponent:', )
# length = Label(text = 'Enter length of key:')
# key = Label(text = 'Enter your key:')

# id.grid(column = 1, row = 1)
# length.grid(column = 2, row = 1)
# key.grid(column = 3, row = 1)

# id_ent = Entry(main, width = 20, textvariable = id_var)
# length_ent = Entry(main, width = 10, textvariable = length_var)
# key_ent = Entry(main, width = 10, textvariable = key_var)

# id_ent.grid(column = 1, row = 2)
# length_ent.grid(column = 2, row = 2)
# key_ent.grid(column = 3, row = 2)

# position = {"padx":6, "pady":6, "anchor":NW}
# type_crypt = ['CBC', 'Other encryption algorithms are coming soon']

# def encrypt():
#     print(f'{id_var.get()}\n{length_var.get()}\n{key_var.get()}')

# button = ttk.Button(text = 'Encrypt', command = encrypt)
# button1 = ttk.Button(text = 'Decrypt')
# button.place(relx = .1, rely = .5, anchor = 'center')
# button1.place(relx = 0.9, rely = .5, anchor = 'center')

# main.mainloop()