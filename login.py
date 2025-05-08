from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

def mg():
	email=email_input.get()
	password=password_input.get()
	if email=='gunanimohit1221@gmail.com' and password=='1234':
		messagebox.showinfo('yayy','login successful')
	else:
		messagebox.showinfo('error','login failed')


root=Tk()
root.title("LOGIN")
# root.iconbitmap('C:\\Users\\MOHIT\\Downloads\\th.ico')
root.minsize(500,700)
root.maxsize(500,700)
# root.geometry('100x100')
root.configure(background='orange')

img1=Image.open("C:\\Users\\MOHIT\\OneDrive\\Desktop\\cars\\th (4).jpeg")
resized_img=img1.resize((300,250))

img=ImageTk.PhotoImage(resized_img)
img_label=Label(root,image=img)
img_label.pack(pady=(10,10))

text_label=Label(root,text="WELCOME",fg='blue',bg='orange')
text_label.configure(font=('algerian',60))
text_label.pack()

text_label1=Label(root,text="Enter Your Email",fg='black',bg='orange')
text_label1.configure(font=('verdana',20))
text_label1.pack(pady=(10,10))

email_input=Entry(root,width=38)
email_input.config(font=("bold"))
email_input.pack(ipady=10)

text_label2=Label(root,text="Enter Password",fg='black',bg='orange')
text_label2.configure(font=('verdana',20))
text_label2.pack(pady=(10,10))

password_input=Entry(root,width=38)
password_input.config(font=("bold"))
password_input.pack(ipady=10)

login_btn=Button(root,text='Login Here',bg='gray',fg='white',width=30,height=3,command=mg)
login_btn.pack(pady=(50,20))




root.mainloop()