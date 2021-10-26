from tkinter import *
from tkinter import messagebox
from pytube import YouTube
from tkinter import filedialog
import os
from tkinter import ttk
import moviepy.editor as mp
#----------------------foeget frame---------------
def forget():
    for w in convert_frame.winfo_children():
        w.destroy()
    for w in download_frame.winfo_children():
        w.destroy()
    main_frame.pack_forget()
    convert_frame.pack_forget()
    download_frame.pack_forget()
#---------------------------------------about------------------------------
def about_func():
    messagebox.showinfo("About", "This application is developed by Md. Rakibul Hasan Asif.       Email: rakibul4210@gmail.com")

#___________________________________--back--___________________________________--
def back():
    forget()
    main_frame.pack(fill="both", expand=1)

#------------------------------------downloader---------------------------
def click():
    try:
        path = "/home/asif/Videos/"
        path_a = "/home/asif/Music/"
        global link_var
        song = YouTube(link_var.get())
        global rb
        if rb.get() == 1:
            try:
                song = song.streams.get_highest_resolution()
                song = song.download(path)
                messagebox.showinfo("Completed", "The video has been downloaded")
                link_var.set("")
            except:
                messagebox.showerror("Error", "Failed to download the Video")
        elif rb.get() == 2:
            try:
                song = song.streams.filter(only_audio=True).first()
                out_file = song.download(output_path=path_a)

                # save the file
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)
                messagebox.showinfo("Completed", "The mp3 has been downloaded")
                link_var.set("")
            except:
                messagebox.showerror("Error", "Failed to download the Audio!")
                link_var.set("")
        else:
            rb.set(1)
            try:
                song = song.streams.get_highest_resolution()
                song = song.download(path)
                messagebox.showinfo("Completed", "The video has been downloaded")
            except:
                messagebox.showerror("Error", "Failed to download the Video")
    except:
        messagebox.showerror("Error", "Enter the link first")


    

def download():
    forget()
    download_frame.pack(fill="both", expand=1)
    global menu_d
    menu_d = LabelFrame(download_frame, bg="Cornsilk", relief=RIDGE, bd=5)
    menu_d.pack(pady=40) 
    greet = Label(menu_d, text="Paste the song link", bg="crimson", fg="white", font=("roboto",20), relief=RAISED, bd=3)
    greet.pack(pady=5, ipady=5, ipadx=20, padx=5)

    global link_var
    link_var = StringVar()
    link_box = Entry(menu_d, font=("roboto"), bd=2, relief="sunken", bg="white", fg="black", textvariable=link_var)
    link_box.pack(pady=5, ipady=5, ipadx=20, padx=5)
    global rb
    rb = IntVar()

    video = Radiobutton(menu_d, text="video", bg="aqua", fg="darkred", font=("roboto",14), bd=3, value=1, variable=rb, activeforeground="white", activebackground="darkred")
    video.place(x=50, y=110)
    audio = Radiobutton(menu_d, text="audio", bg="aqua", fg="darkred", font=("roboto",14), bd=3, value=2, variable=rb, activeforeground="white", activebackground="darkred")
    audio.place(x=160, y=110)
    rb.set(1)
    down_btn = Button(menu_d, text="Download", bg="crimson", fg="white", font=("roboto"), relief=RAISED, activebackground="red", activeforeground="white", command=click)
    down_btn.pack(padx=5, pady=40, ipadx=5, ipady=5)

    back_btn = Button(menu_d, text="Back", bg="crimson", fg="white", font=("roboto"), relief=RAISED, activebackground="red", activeforeground="white", command=back)
    back_btn.place(x=120, y=195)

#___________________________---converter---_________________________________
def choose():
    files = filedialog.askopenfilenames(initialdir="/home/asif/Videos/", title="Choose files",filetypes=(("mp4 files", "*.mp4"),("ALL FILES", "*.*"),))
    global file_new
    file_new = files[0]
    file_p = file_new.split("/")
    global name
    name = file_p[-1]
    global file_box
    file_box.delete(0, END)
    file_box.insert(0,name)

def convert_func():
    forget()
    convert_frame.pack(fill="both", expand=1)
    global menu_c

    menu_c = LabelFrame(convert_frame, bg="Cornsilk", relief=RIDGE, bd=5)
    menu_c.pack(pady=20)

    l3 = Label(menu_c, text="Video to Audio Converter ",  bg="crimson", fg="white", font=("roboto",20), relief=RIDGE)
    l3.place(x=10, y=20)

    ch_file = Button(menu_c,text="Choose file", bg="crimson", fg="white", font=("roboto"), relief=RAISED, activebackground="red", activeforeground="white", command=choose)
    ch_file.pack(pady=110, padx=100, ipady=8, ipadx=20)

    l1 = Label(menu_c, text="selected file: ",  bg="crimson", fg="white", font=("roboto",14), relief=RAISED)
    l1.place(x=10, y=165)
    global file_box
    file_box = Entry(menu_c, font=("roboto"), bd=2, relief="sunken", bg="white", fg="black")
    file_box.place(x=140, y=165)

    l2 = Label(menu_c, text="File format : ",  bg="crimson", fg="white", font=("roboto",14), relief=RAISED)
    l2.place(x=10, y=200)
    lists = [".mp3", ".ogg", ".wav"]
    global s
    s = ttk.Combobox(menu_c, font=("roboto"), value=lists)
    s.current(0)
    s.place(x=140, y=200)
    convert1_btn = Button(menu_c, text="Convert", bg="crimson", fg="white", font=("roboto"), relief=RAISED, activebackground="red", activeforeground="white", command=conversion)
    convert1_btn.place(x=50, y=233)

    clear_btn = Button(menu_c, text="Clear", bg="crimson", fg="white", font=("roboto"), relief=RAISED, activebackground="red", activeforeground="white", command=clear)
    clear_btn.place(x=150, y=233)

    back1_btn = Button(menu_c, text="Back", bg="crimson", fg="white", font=("roboto"), relief=RAISED, activebackground="red", activeforeground="white", command=back)
    back1_btn.place(x=230, y=233)

def conversion():
    try:
        global file_new
        file_p = file_new.split("/")
        name = file_p[-1]
        name = name.replace(".mp4", "")
        file_p[-1] = ""
        new =[]
        for i in file_p:
            new.append("/"+i)
        new_a = ""
        for j in new:
            new_a += j
        if s.get() == ".mp3": 
            video = mp.VideoFileClip(file_new)
            audio = video.audio
            audio.write_audiofile(os.path.join(new_a, name+".mp3"))
            messagebox.showinfo("Completed!","The song has been converted!")
        elif s.get() == ".ogg":
            video = mp.VideoFileClip(file_new)
            audio = video.audio
            audio.write_audiofile(os.path.join(new_a, name+".ogg"))
            messagebox.showinfo("Completed!","The song has been converted!")
        elif s.get() == ".wav":
            video = mp.VideoFileClip(file_new)
            audio = video.audio
            audio.write_audiofile(os.path.join(new_a, name +".wav"))
            messagebox.showinfo("Completed!","The song has been converted!")
        else:
            messagebox.showwarning("Error!", "Invalid file type!")
    except:
        messagebox.showerror("Invalid","Please select the video first!")

def clear():
    global file_box
    file_box.delete(0,END)
    global s
    s.current(0)
    pass


root = Tk()
root.title("Downloader")
root.geometry("400x400")

#main_frame
main_frame = Frame(root, bg="Crimson")
main_frame.pack(fill="both", expand=1)

download_frame = Frame(root, bg="Crimson")
convert_frame = Frame(root, bg="Crimson")
#menu_frame
menu = LabelFrame(main_frame, bg="Cornsilk", relief=RIDGE, bd=5)
menu.pack(pady=80)

downloader = Button(menu, text="Song Downloader", bg="crimson", fg="white", font=("roboto"), relief=RAISED, activebackground="red", activeforeground="white", command=download)
downloader.pack(padx=5, pady=5, ipadx=5, ipady=5)
converter = Button(menu, text="Converter", bg="crimson", fg="white", font=("roboto"), relief=RAISED, activebackground="red", activeforeground="white", command=convert_func)
converter.pack(padx=5, pady=5, ipadx=37, ipady=5)
about = Button(menu, text="About", bg="crimson", fg="white", font=("roboto"), relief=RAISED, activebackground="red", activeforeground="white", command= about_func)
about.pack(padx=5, pady=5, ipadx=52, ipady=5)
exit = Button(menu, text="Exit", bg="crimson", fg="white", font=("roboto"), relief=RAISED, activebackground="red", activeforeground="white", command=root.quit)
exit.pack(padx=5, pady=5, ipadx=60, ipady=5)

my_image = PhotoImage(file="/home/asif/Documents/python3/GUI/downloader/logo.png")
image_label = Label(main_frame,image=my_image)
image_label.place(x=5, y=310)



root.mainloop()
