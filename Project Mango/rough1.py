import tkinter as t
from tkinter import ttk
import customtkinter as ck
import pandas as pd
import numpy as np
import os
# 1.
# """ rt=t.Tk()
# rt.geometry('1100x630') # 1100x630 is an ideal size
# rt.mainloop() """
# 2.
# """ conobj=msc.connect(host='localhost',user='root',password='rishu1234',database='mango')
# curobj=conobj.cursor()
# curobj.execute('delete from account')
# conobj.commit() """
# """ import tkinter.ttk as ttk
# import tkinter

# app = tkinter.Tk()
# app.geometry("400x350")
# app.title("simple_example_standard_tkinter.py")


# def button_function():
#     print("button pressed")


# def slider_function(value):
#     progressbar_1["value"] = value


# s = ttk.Style()
# s.configure("TRadiobutton", fg="red")

# y_padding = 6

# frame_1 = tkinter.Frame(master=app, width=300, height=260, bg="lightgray")
# frame_1.pack(padx=60, pady=20, fill="both", expand=True)

# label_1 = tkinter.Label(master=frame_1, text="Label", bg="lightgray")
# label_1.pack(pady=y_padding, padx=10)

# progressbar_1 = ttk.Progressbar(master=frame_1, style='black.Horizontal.TProgressbar', length=150)
# progressbar_1.pack(pady=y_padding, padx=10)
# progressbar_1["value"] = 50

# button_1 = tkinter.Button(master=frame_1, command=button_function, text="Button", highlightbackground="lightgray")
# button_1.pack(pady=y_padding, padx=10)

# slider_1 = tkinter.Scale(master=frame_1, command=slider_function, orient="horizontal", bg="lightgray", length=150)
# slider_1.pack(pady=y_padding, padx=10)

# entry_1 = tkinter.Entry(master=frame_1, highlightbackground="lightgray", width=10)
# entry_1.pack(pady=y_padding, padx=10)

# checkbox_1 = tkinter.Checkbutton(master=frame_1, bg=frame_1.cget("bg"), text="CheckButton")
# checkbox_1.pack(pady=y_padding, padx=10)

# radiobutton_var = tkinter.IntVar()

# radiobutton_1 = ttk.Radiobutton(master=frame_1, variable=radiobutton_var, value=1, text="Radiobutton")
# radiobutton_1.pack(pady=y_padding, padx=10)

# radiobutton_2 = ttk.Radiobutton(master=frame_1, variable=radiobutton_var, value=2, text="Radiobutton")
# radiobutton_2.pack(pady=y_padding, padx=10)

# app.mainloop() """


# """ 
# def return_pressed(event):
#     print('Return key pressed.')


# root = t.Tk()

# btn = ttk.Button(root, text='Save')
# btn.bind('<Return>', return_pressed)


# btn.focus()
# btn.pack(expand=True)

# root.mainloop() """

# import customtkinter, tkinter

# app = customtkinter.CTk()
# app.grid_rowconfigure(0, weight=1)
# app.grid_columnconfigure(0, weight=1)

# # create scrollable textbox
# tk_textbox = tkinter.Text(app, highlightthickness=0)
# tk_textbox.grid(row=0, column=0, sticky="nsew")

# # create CTk scrollbar
# ctk_textbox_scrollbar = customtkinter.CTkScrollbar(app, command=tk_textbox.yview)
# ctk_textbox_scrollbar.grid(row=0, column=1, sticky="ns")

# # connect textbox scroll event to CTk scrollbar
# tk_textbox.configure(yscrollcommand=ctk_textbox_scrollbar.set)

# app.mainloop()


# def Sales() :
# ## Valiables    : ## - ItemName= I_N, - ItemCOde= I_C , - Quantity= Qu,  - Date= Date, 

# # Data would be in list of list
#     for i in billlst :  # i would be [I_N,I_C,Qu, Date] 

#    # **Made a data frame of  Sales(1 entry)
#         Salesdf= pd.DataFrame([i]) #  i would be [I_N,I_C,Qu, Date]

#    # **append data frame to CSV file
#         Salesdf.to_csv('Sales(2).csv', mode='a', index=False, header=False)

#    ## After sales table is updated the inventory has should also be updated

#         InventoryUpdate()    # i = [I_N,I_C,Qu, Date] """

     
""" 
def InventoryUpdate(): # i = [I_N,I_C,Qu, Date]
    Item_Code= pd.read_csv('Inventory(2).csv', usecols= ['Item_Code']) 

    ItemCode= Item_Code.to_numpy()

    for i in billlst:
     for j in ItemCode:
        if j == billlst[0]:  ##**change the Quantity 
         df= pd.read_csv('Inventory(2).csv')

     # **Replace values of columns by using DataFrame.loc[] property.
         df.loc[df['ItemCode'] == int(i[0]) ,'Quantity'] =int(df[df['Item_Code']==  int(i[0])]['Quantity'])+Qu   

         df.to_csv('Inventory(2).csv') """


def loginwindow():
    root2.withdraw()
    os.system('loginwindow.py')
    root2.destroy()

def signup(event=None):
    global entry0,entry1,root2
    uname=(entry0.get()).strip()   #entry in the entry box is of str datatye=p
    pswd=(entry1.get()).strip()
    signupdf=pd.read_csv('user data\\username.csv')
    signupdf2=signupdf[signupdf['Username']==uname]
    signuplst=signupdf2.to_numpy().tolist()
    # print(signuplst)
    # print (data)
    # print(uname,pswd, type(uname),type(pswd))

    if uname !='' and pswd !='' and uname.isspace() == False  and pswd.isspace()==False:
        if len(signuplst)==0:
            newdf=pd.DataFrame([[uname,pswd]])
            newdf.to_csv('user data\\username.csv', mode='a', index=False, header=False)
            with open ('user data\\username2.csv','w') as fo:
                pass
            newdf.to_csv('user data\\username2.csv', mode='a', index=False, header=['Last Username','Last Password'])
            root2.withdraw()
            os.system('homewindownew.py')
            root2.destroy()
        else:
            newuname=t.Label(root2,text='Please enter a different Username\t\t',fg='red',bg='white',font=('',9))
            newuname.place(x=89,y=320)
        
    else:
        nodata=t.Label(root2,text='Please enter valid Username and Password\t',fg='red',bg='white',font=('',9))
        nodata.place(x=89,y=320)

    

root2 = t.Tk()
root2.resizable(False,False)
root2.title('MANGO')
root2.iconbitmap('images\\mangoicon.ico')#ICON


# get the screen dimension
screen_width = root2.winfo_screenwidth()
screen_height = root2.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - 800/ 2)
center_y = int(screen_height/2 -  500/ 2)-40

# set the position of the root2 to the center of the screen
root2.geometry(f'800x500+{center_x}+{center_y}')

root2.configure(bg = "#ffffff")
canvas = t.Canvas(root2,bg = "#ffffff",height = 500,width = 800,bd = 0,highlightthickness = 0,relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = t.PhotoImage(file = f"images\\signupbackground.png")
background = canvas.create_image(407.0, 250.0,image=background_img)

entry0_img = t.PhotoImage(file = f"images\\img_textBox0.png")
entry0_bg = canvas.create_image(214.5, 206.0,image = entry0_img)

entry0 = t.Entry(bd = 0,bg = "#ebe9e9", highlightthickness = 0,font=('',12))
entry0.bind('<Return>',signup)
entry0.place(x = 97.0, y = 186,width = 235.0,height = 38)

hide_image=t.PhotoImage(file='images\\hide.png')
show_image=t.PhotoImage(file='images\\show.png')

def show():
    hide_button=t.Button(root2,image=hide_image,command=hide,activebackground='white',bd=0,background='white',cursor='hand2')
    hide_button.place(x=355,y=279)
    entry1.config(show='')

def hide():
    show_button=t.Button(root2,image=show_image,command=show,activebackground='white',bd=0,background='white',cursor='hand2')
    show_button.place(x=355,y=279)
    entry1.config(show='*')
    
show_button=t.Button(root2,image=show_image,command=show,activebackground='white',bd=0,background='white',cursor='hand2')
show_button.place(x=355,y=279)


entry1_img = t.PhotoImage(file = f"images\\img_textBox1.png")
entry1_bg = canvas.create_image(214.5, 299.0,image = entry1_img)

entry1 = t.Entry(bd = 0,bg = "#ebe9e9",highlightthickness = 0,font=('',12),show='*')
entry1.bind('<Return>',signup)
entry1.place(x = 97.0, y = 279,width = 235.0,height = 38)

img0 = t.PhotoImage(file = f"images\\submitbutton.png")
submitbutton = t.Button(image = img0,borderwidth = 0,highlightthickness = 0,command = signup,relief = "flat",cursor='hand2')
# submitbutton.bind('<Return>',signup)
submitbutton.place(x = 124, y = 340,width = 167,height = 61)

img1 = t.PhotoImage(file = f"images\\loginbutton.png")
loginbutton = t.Button(image = img1,borderwidth = 0,highlightthickness = 0,command = loginwindow,relief = "flat",cursor='hand2')

loginbutton.place(x = 236, y = 422,width = 102,height = 50)

root2.resizable(False, False)
root2.mainloop()
