import tkinter as t
from tkinter import ttk
from tkinter import messagebox
from PIL import Image
import os
import customtkinter as ck     
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style as sty
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
from matplotlib.backend_bases import key_press_handler
import datetime as dt
# root.geometry("700x500")

# # Create frame
# my_frame = Frame(root)
# my_frame.pack(pady=20)

# # Create treeview
# my_tree = ttk.Treeview(my_frame)

# # File open function
# """ def file_open():
# 	filename = filedialog.Open(
# 		initialdir="C:/gui/",
# 		title = "Open A File",
# 		filetype=(("csv files", "*.csv"), ("All Files", "*.*"))
# 		)

# 	if filename:
# 		try:
# 			filename = r"{}".format(filename)
# 			df = pd.read_csv(filename)
# 		except ValueError:
# 			my_label.config(text="File Couldn't Be Opened...try again!")
# 		except FileNotFoundError:
# 			my_label.config(text="File Couldn't Be Found...try again!")
# 	# Clear old treeview
# 	clear_tree() """

# stockdf= pd.read_csv('Stock_Entry.csv')

# 	# Set up new treeview
# my_tree["column"] = list(stockdf.columns)
# my_tree["show"] = "headings"
# # Loop thru column list for headers
# for column in my_tree["column"]:
#     my_tree.heading(column, text=column)

# # Put data in treeview
# df_rows = stockdf.to_numpy().tolist()
# for row in df_rows:
#     my_tree.insert("", "end", values=row)

# # Pack the treeview finally
# my_tree.pack()




# """ def clear_tree():
# 	my_tree.delete(*my_tree.get_children()) """

# # Add a menu
# my_menu = Menu(root)
# root.config(menu=my_menu)

# # Add menu dropdown
# """ file_menu = Menu(my_menu, tearoff=False)
# my_menu.add_cascade(label="Spreadsheets", menu=file_menu)
# file_menu.add_command(label="Open", command=file_open) """

# my_label = Label(root, text='')
# my_label.pack(pady=20)

# root.mainloop()






# Labelling Graohs 
# plt.title('Product Vs Quantitiy Sold')
# plt.xlabel('Product')
# plt.ylabel('Quantity')
#===================================================================
# rt=t.Tk()
# rt.geometry("700x500")
# frame2=t.Frame(master=rt,width=700,height=100)
# frame2.grid(row=0,column=0)
# frame1=t.Frame(master=rt,width=700,height=400)
# frame1.grid(row=1,column=0)

# canvas=t.Canvas(master=frame1,width=650,height=450)
# canvas.place(x=10,y=10)

# def abc():
# 	fig = Figure(figsize=(6,6), dpi = 90) 
# 	plot1 = fig.add_subplot(111)
# 	plot1.plot([1,2,3,4],[5,6,7,8])

# 	# df= pd.read_csv('sales().csv').sort_values(by='Item_Name')
# 	# df1= df[["Quantity",'Item_Name']].groupby("Item_Name").sum() 
# 	# plot1.bar((df["Item_Name"].unique()), df1['Quantity'] )


# 	canvas1 = FigureCanvasTkAgg(fig , master = canvas)
# 	canvas1.draw()
# 	canvas1.get_tk_widget().pack(padx=250, pady=81)
# 	toolbar = NavigationToolbar2Tk(canvas1, frame1)
# 	toolbar.update()
# 	canvas1.get_tk_widget().pack(side='top', fill= 'both')

    


# b=t.Button(master=frame2,text='Graph it', command=abc)
# b.pack()



# rt.mainloop()
#====================================================================
# print(str(dt.datetime.today()),type(str(dt.datetime.today())))



""" def signupwindow():
    root1.withdraw()
    os.system('signupwindow.py')
    root1.destroy()

def login(event=None):
    global entry0,entry1,root1,uname,pswd
    uname=entry0.get()
    pswd=entry1.get() 
    logindf=pd.read_csv('user data\\username.csv')
    logindf2=logindf[logindf['Username']==uname] 
    logindf3=logindf2[logindf2['Password']==pswd] 
    loginlst=logindf3.to_numpy().tolist()
    # print(logindf)
    # print(logindf3)
    # print(loginlst)
    
    # use this to count no. of rows-logindf.count().to_numpy().tolist()

    if  len(loginlst) !=0:
        if loginlst[0][1] == pswd:
            correctdata=t.Label(root1,text='\t\t\t\t\t',fg='red',bg='white',font=('',9))
            correctdata.place(x=89,y=320)
            with open ('user data\\username2.csv','w') as fo:
                pass
            logindf3.to_csv('user data\\username2.csv', mode='w', index=False, header=['Last Username','Last Password'])
            root1.withdraw()
            os.system('homewindownew.py')
            root1.destroy()
            return (uname,pswd)
        else:
            wrongdata=t.Label(root1,text='Incorrect Username or Password',fg='red',bg='white',font=('',9))
            wrongdata.place(x=89,y=320)
    else:
        
        wrongdata=t.Label(root1,text='Incorrect Username or Password',fg='red',bg='white',font=('',9))
        wrongdata.place(x=89,y=320)


root1 = t.Tk()
root1.resizable(False,False)
root1.title('MANGO')
root1.iconbitmap('images\\mangoicon.ico')#ICON
# get the screen dimension
screen_width = root1.winfo_screenwidth()
screen_height = root1.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - 800/ 2)
center_y = int(screen_height/2 -  500/ 2)-40

# set the position of the root1 to the center of the screen
root1.geometry(f'800x500+{center_x}+{center_y}')

#root1.geometry("800x500")
root1.configure(bg = "#ffffff")
canvas = t.Canvas(root1,bg = "#ffffff",height = 500,width = 800,bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = t.PhotoImage(file = "images\\loginbackground.png")
background = canvas.create_image(407.0, 250.0,image=background_img)
#entry0 - username , entry1- password
entry0_img = t.PhotoImage(file = "images\\img_textBox0.png")
entry0_bg = canvas.create_image(214.5, 206.0,image = entry0_img)

entry0 = t.Entry(bd = 0,bg = "#ebe9e9",highlightthickness = 0 ,font=('',12))
entry0.bind('<Return>',login)
entry0.place(x = 97.0, y = 186,width = 235.0,height = 38)
hide_image=t.PhotoImage(file='images\\hide.png')
show_image=t.PhotoImage(file='images\\show.png')

def show():
    hide_button=t.Button(root1,image=hide_image,command=hide,activebackground='white',bd=0,background='white',cursor='hand2')
    hide_button.place(x=355,y=279)
    entry1.config(show='')

def hide():
    show_button=t.Button(root1,image=show_image,command=show,activebackground='white',bd=0,background='white',cursor='hand2')
    show_button.place(x=355,y=279)
    entry1.config(show='*')

show_button=t.Button(root1,image=show_image,command=show,activebackground='white',bd=0,background='white',cursor='hand2')
show_button.place(x=355,y=279)

entry1_img =t.PhotoImage(file = "images\\img_textBox1.png")
entry1_bg = canvas.create_image(214.5, 299.0,image = entry1_img)
entry1 = t.Entry(bd = 0,bg = "#ebe9e9",highlightthickness = 0,show="*",font=('',12))
entry1.bind('<Return>',login) #can also use lambda event: login()
entry1.place(x = 97.0, y = 279,width = 235.0,height = 38)

img0 = t.PhotoImage(file = "images\\submitbutton.png")
submitbutton = t.Button(image = img0,borderwidth = 0,highlightthickness = 0,command = login,relief = "flat",cursor='hand2')
submitbutton.place(x = 124, y = 340,width = 167,height = 61)

img1 = t.PhotoImage(file = "images\\signupbutton.png")
signupbutton = t.Button(image = img1,borderwidth = 0,highlightthickness = 0,command = signupwindow,relief = "flat",cursor='hand2')

signupbutton.place(x = 250, y = 418,width = 102,height = 50)
root1.resizable(False, False)
root1.mainloop() """ 
# with open('user data\\inventory.csv','w') as fo:
#     pass
