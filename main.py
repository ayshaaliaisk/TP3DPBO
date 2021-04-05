from tkinter import *
# from tkinter.ttk import *
import tkinter as tk

root = tk.Tk()
root.title("TP3 DPBO")
root.geometry('500x700')


def about():
    top = Toplevel()
    top.title("About")

    d_frame = LabelFrame(top, text="Me", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    d_summary = Label(d_frame, text="Nama : Aysha Alia Iskandar \n NIM : 1901102 ",
                      anchor="w").grid(row=0, column=0, sticky="w")
    d_exit = Button(d_frame, text="Exit", command=top.destroy)
    d_exit.grid(row=1, column=0)


frame3 = tk.Frame(root, width=250, bg="cyan")
# frame3.grid(row=0, column=0, padx=15, pady=15, ipadx=15, ipady=15)
frame3.pack(fill=tk.X, ipadx=15, ipady=15)

frame1 = tk.Frame(root, width=100)
# frame1.grid(row=1, column=0, padx=10, pady=10, ipadx=10, ipady=10)
frame1.pack(fill=tk.X, padx=10, pady=10, ipadx=10, ipady=10)

frame2 = tk.Frame(root, width=100)
# frame2.grid(row=2, column=0, padx=10, pady=10, ipadx=10, ipady=10)
frame2.pack(fill=tk.X, padx=10, pady=10, ipadx=10, ipady=10)

frame4 = tk.Frame(root, width=100)
# frame4.grid(row=3, column=0, padx=10, pady=10, ipadx=10, ipady=10)
frame4.pack(fill=tk.X, padx=10, pady=10, ipadx=10, ipady=10)

# frameX.pack(fill=tk.X)

frame5 = tk.Frame(root, width=100)
frame5.pack(fill=tk.X, padx=10, pady=10, ipadx=10, ipady=10)

judul = Label(frame3, text="STUDENT COLOUR FAV",
              font=(50), fg="blue", bg="cyan")
judul.pack()

des = Label(frame3, text="Aplikasi Pengumpulan Data Warna Favorit Mahasiswa",
            font=(50), fg="red", bg="cyan")
des.pack()

l1 = Label(frame1, text="Nama : ", font=(16))
l1.grid(row=0, column=0, padx=10, pady=10)

textbox1 = Entry(frame1, font=(16), width=15)
textbox1.grid(row=0, column=1)

l2 = Label(frame1, text="NIM : ", font=(16))
l2.grid(row=1, column=0, padx=10, pady=10)

textbox2 = Entry(frame1, font=(16), width=15)
textbox2.grid(row=1, column=1)

l3 = Label(frame1, text="Jurusan : ", font=(16))
l3.grid(row=2, column=0, padx=10, pady=10)

textbox3 = Entry(frame1, font=(16), width=15)
textbox3.grid(row=2, column=1)


CLASS = [
    "A",
    "B",
    "C1",
    "C2"
]

l4 = Label(frame1, text="Kelas : ", font=(16))
l4.grid(row=3, column=0, padx=10, pady=10)

variable = StringVar(root)
variable.set(CLASS[0])  # default value

kelas = OptionMenu(frame1, variable, *CLASS)
kelas.grid(row=3, column=1, padx=10, pady=10)

l5 = Label(frame1, text="Jenis Kelamin : ", font=(16))
l5.grid(row=4, column=0)

jk = IntVar()
R1 = Radiobutton(frame1, text="Perempuan",  variable=jk, value=1)
R1.grid(row=4, column=1)

R2 = Radiobutton(frame1, text="Laki-laki",  variable=jk, value=2)
R2.grid(row=4, column=2)

l6 = Label(frame1, text="Warna Favorit : ", font=(16))
l6.grid(row=5, column=0)

warna1 = IntVar()
warna2 = IntVar()
warna3 = IntVar()
warna4 = IntVar()
CB1 = Checkbutton(frame1, text="hitam", variable=warna1, onvalue=1, offvalue=0)
CB1.grid(row=5, column=1)

CB2 = Checkbutton(frame1, text="merah", variable=warna2, onvalue=1, offvalue=0)
CB2.grid(row=5, column=2)

CB3 = Checkbutton(frame1, text="kuning",
                  variable=warna3, onvalue=1, offvalue=0)
CB3.grid(row=5, column=3)

CB4 = Checkbutton(frame1, text="hijau", variable=warna4, onvalue=1, offvalue=0)
CB4.grid(row=5, column=4)

button1 = Button(frame2, text='OPEN PHOTO FILE', font=(16), width=20)
button1.pack()

button2 = Button(frame2, text='SUBMIT', font=(16), width=20)
button2.pack()

button3 = Button(frame4, text='SEE ALL SUBMISSONS', font=(16), width=20)
button3.pack()

button4 = Button(frame4, text='CLEAR SUBMISSONS', font=(16), width=20)
button4.pack()

button5 = Button(frame4, text='ABOUT', font=(16), width=20, command=about)
button5.pack()

button6 = Button(frame5, text='EXIT', font=(
    16), width=20, bg="red", command=root.quit)
button6.pack()

root.mainloop()
