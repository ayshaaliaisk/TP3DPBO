from tkinter import *
# from tkinter.ttk import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog

root = tk.Tk()
root.title("TP3 DPBO")
root.geometry('500x600')


def about():
    top = Toplevel()
    top.title("About")

    d_frame = LabelFrame(top, text="Me", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    d_summary = Label(d_frame, text="Nama : Aysha Alia Iskandar \n NIM : 1901102 ",
                      anchor="w").grid(row=0, column=0, sticky="w")
    d_exit = Button(d_frame, text="Exit", command=top.destroy)
    d_exit.grid(row=1, column=0)


def photo():
    global my_image
    root.filename = filedialog.askopenfilename(
        initialdir="C:/gui/images", title="Select A File", filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename)).pack()
    my_image_label = Label(image=my_image).pack()


def save_data():
    nama_info = nama.get()
    nim_info = nim.get()
    jurusan_info = jurusan.get()
    kelas_info = kelas.get()
    jk_info = jk.get()

    file = open("data.txt", "w")
    file.write("Nama : " + nama_info + "\n")
    file.write("NIM : " + nim_info + "\n")
    file.write("Jurusan : " + jurusan_info + "\n")
    # file.write("Kelas : " + kelas_info + "\n")
    # file.write("Jenis Kelamin : " + jk_info + "\n")

    file.close()

    print("Data Berhasil Dimasukkan")

    nama_entry.delete(0, END)
    nim_entry.delete(0, END)
    jurusan_entry.delete(0, END)


def read_data():
    file = open("data.txt", "r")

    data = file.read()

    print("SUBMISSONS : \n")
    print(data)

    file.close()


################################## FRAME #######################################
frame3 = tk.Frame(root, width=250, bg="cyan")
frame3.pack(fill=tk.X, ipadx=15, ipady=15)

frame1 = tk.Frame(root, width=100)
frame1.pack(fill=tk.X, padx=10, pady=10, ipadx=10, ipady=10)

frame2 = tk.Frame(root, width=100)
frame2.pack(fill=tk.X, padx=5, pady=5, ipadx=5, ipady=5)

frame4 = tk.Frame(root, width=100)
frame4.pack(fill=tk.X, padx=5, pady=5, ipadx=5, ipady=5)

frame5 = tk.Frame(root, width=100)
frame5.pack(fill=tk.X, padx=5, pady=5, ipadx=5, ipady=5)

############################# HEADER #################################

judul = Label(frame3, text="STUDENT COLOUR FAV",
              font=(50), fg="blue", bg="cyan")
judul.pack()

des = Label(frame3, text="Aplikasi Pengumpulan Data Warna Favorit Mahasiswa",
            font=(50), fg="red", bg="cyan")
des.pack()

############################### INISIALISASI #######################################

nama = StringVar()
nim = StringVar()
jurusan = StringVar()
kelas = StringVar()
jk = StringVar()

warna1 = StringVar()
warna2 = StringVar()
warna3 = StringVar()
warna4 = StringVar()

#######################################################################

l1 = Label(frame1, text="Nama : ", font=(16))
l1.grid(row=0, column=0, padx=10, pady=10)

nama_entry = Entry(frame1, textvariable=nama, font=(16), width=15)
nama_entry.grid(row=0, column=1)

l2 = Label(frame1, text="NIM : ", font=(16))
l2.grid(row=1, column=0, padx=10, pady=10)

nim_entry = Entry(frame1, textvariable=nim, font=(16), width=15)
nim_entry.grid(row=1, column=1)

l3 = Label(frame1, text="Jurusan : ", font=(16))
l3.grid(row=2, column=0, padx=10, pady=10)

jurusan_entry = Entry(frame1, textvariable=jurusan, font=(16), width=15)
jurusan_entry.grid(row=2, column=1)


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

kelas_input = OptionMenu(frame1, *CLASS)
kelas_input.grid(row=3, column=1, padx=10, pady=10)

l5 = Label(frame1, text="Jenis Kelamin : ", font=(16))
l5.grid(row=4, column=0)


R1 = Radiobutton(frame1, text="Perempuan", variable=jk, value=1)
R1.grid(row=4, column=1)

R2 = Radiobutton(frame1, text="Laki-laki", variable=jk, value=2)
R2.grid(row=4, column=2)

l6 = Label(frame1, text="Warna Favorit : ", font=(16))
l6.grid(row=5, column=0)


CB1 = Checkbutton(frame1, text="hitam", variable=warna1, onvalue=1, offvalue=0)
CB1.grid(row=5, column=1)

CB2 = Checkbutton(frame1, text="merah", variable=warna2, onvalue=1, offvalue=0)
CB2.grid(row=5, column=2)

CB3 = Checkbutton(frame1, text="kuning",
                  variable=warna3, onvalue=1, offvalue=0)
CB3.grid(row=5, column=3)

CB4 = Checkbutton(frame1, text="hijau", variable=warna4, onvalue=1, offvalue=0)
CB4.grid(row=5, column=4)

################################### BUTTON ###########################################

button1 = Button(frame2, text='OPEN PHOTO FILE',
                 font=(16), width=20, command=photo)
button1.pack()

button2 = Button(frame2, text='SUBMIT', font=(16), width=20, command=save_data)
button2.pack()

button3 = Button(frame4, text='SEE ALL SUBMISSONS',
                 font=(16), width=20, command=read_data)
button3.pack()

button4 = Button(frame4, text='CLEAR SUBMISSONS', font=(16), width=20)
button4.pack()

button5 = Button(frame4, text='ABOUT', font=(16), width=20, command=about)
button5.pack()

button6 = Button(frame5, text='EXIT', font=(
    16), width=20, bg="red", command=root.quit)
button6.pack()

root.mainloop()
