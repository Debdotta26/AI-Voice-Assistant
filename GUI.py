from tkinter import*
from PIL import Image, ImageTk
import action
import speech_to_text

root = Tk()
root.title("AI Assistant")
root.geometry("550x675")
root.resizable(False , False)
root.config(bg="#A76D8E")
#ask fun
def ask():
    user_val = speech_to_text.speech_to_text()
    bot_val = action.Action(user_val)
    text.insert(END,'User--->'+ user_val + "\n")
    if bot_val != None:
        text.insert(END, 'BOT<---' + str(bot_val) + "\n")
    if bot_val == "ok, shutting down":
        root.destroy()
def send():
    send = entry.get()
    bot = action.Action(send)
    text.insert(END, 'User--->' + send + "\n")
    if bot != None:
        text.insert(END, 'BOT<---' + str(bot) + "\n")
    if bot == "ok, shutting down":
        root.destroy()
def del_text():
    text.delete('1.0',"end")
#frame
Frame = LabelFrame(root,padx=80,pady=12,borderwidth=3,relief="raised")
Frame.config(bg="#A44C7E")
Frame.grid(row=0,column=1,padx=55,pady=10)
#text label
text_label = Label(Frame , text="AI Assistant" , font=("ALGERIAN" , 18 ,"bold", "italic") , bg="#4F5297")
text_label.grid(row=0 , column=0 ,padx=50 ,pady=10)
#image
original_image = Image.open("assistant.png")
resized_image = original_image.resize((200, 200))  # Adjust dimensions as needed
image = ImageTk.PhotoImage(resized_image)
image_label= Label(Frame , image = image)
image_label.grid(row=1,column=0 ,pady=20)
#adding a text widget
text=Text(root , font=("Colonna MT" , 16 ,"bold"), bg="#A44C7E")
text.grid(row=2,column=0)
text.place(x=80,y=350,width=400 ,height=155)
#entry widget
entry=Entry(root ,font=("Colonna MT" , 16 ,"bold"), justify=CENTER)
entry.place(x=100 , y =515 , width=350 , height=40)
#button1
Button1=Button(root , text="ASK", bg="#A44C7E" ,font=("Comic Sans ms" , 14 ,"bold","underline"), padx=35 , pady=14 , borderwidth=3 , relief=SOLID , command=ask)
Button1.place(x=50 , y=570)
#button2
Button2=Button(root , text="SEND", bg="#A44C7E" , font=("Comic Sans ms" , 14 ,"bold" ,"underline") ,padx=35 , pady=14 , borderwidth=3 , relief=SOLID , command=send)
Button2.place(x=375,y=570)
#button3
Button3=Button(root , text="DELETE", bg="#A44C7E" , font=("Comic Sans ms" , 14 ,"bold","underline") , padx=35 , pady=14 , borderwidth=3 , relief=SOLID , command=del_text)
Button3.place(x=200,y=570)
root.mainloop()