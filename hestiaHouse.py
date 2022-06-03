import pyfirmata2
from PIL import ImageTk, Image
import tkinter as tk


window = tk.Tk()
window.title('HestiaHouse')
window.minsize(600, 750)
window.configure(bg="#15252d")
window.iconbitmap(r'hestiaico.ico')
contControles = tk.Frame(window,  padx=20, pady=20, bd=2, relief="flat")
contControles.pack()

arduino = pyfirmata2.Arduino('COM3')
pin13 = arduino.get_pin('d:13:o')
pin12 = arduino.get_pin('d:12:o')
pin11 = arduino.get_pin('d:11:o')
pin10Servo = arduino.get_pin('d:10:s')
pin10Servo.write(105)

def switchLuzCuarto():
    print(btnLuzCuarto.cget('text'))
    if (btnLuzCuarto.cget('text') == 'Encender'):
        pin13.write(1)
        btnLuzCuarto.configure(text="Apagar", background="#F07EF2")
        
        if (btnLuzPasillo.cget('text') == 'Apagar'):
            btnAllLuces.configure(text="Apagar todas las luces", background="#F07EF2")

    elif (btnLuzCuarto.cget('text') == 'Apagar'):
        pin13.write(0)
        btnLuzCuarto.configure(text="Encender", background="#63F2B0")

        if (btnLuzPasillo.cget('text') == 'Apagar'):
            btnAllLuces.configure(text="Encender todas las luces", background="#63F2B0")


def switchLuzPasillo():
    print(btnLuzPasillo.cget('text'))
    if (btnLuzPasillo.cget('text') == 'Encender'):
        pin12.write(1)
        btnLuzPasillo.configure(text="Apagar", background="#F07EF2")
        if (btnLuzCuarto.cget('text') == 'Apagar'):
            btnAllLuces.configure(text="Apagar todas las luces", background="#F07EF2")
    elif (btnLuzPasillo.cget('text') == 'Apagar'):
        pin12.write(0)
        btnLuzPasillo.configure(text="Encender", background="#63F2B0")
        if (btnLuzCuarto.cget('text') == 'Apagar'):
            btnAllLuces.configure(text="Encender todas las luces", background="#63F2B0")


def switchAllLuces():
    print(btnAllLuces.cget('text'))
    if (btnAllLuces.cget('text') == 'Encender todas las luces'):
        print("prendo")
        pin13.write(1)
        pin12.write(1)
        btnAllLuces.configure(text="Apagar todas las luces", background="#F07EF2")
        btnLuzCuarto.configure(text="Apagar", background="#F07EF2")
        btnLuzPasillo.configure(text="Apagar", background="#F07EF2")
    elif (btnAllLuces.cget('text') == 'Apagar todas las luces'):
        print("apago")
        pin13.write(0)
        pin12.write(0)
        btnAllLuces.configure(text="Encender todas las luces", background="#63F2B0")
        btnLuzCuarto.configure(text="Encender", background="#63F2B0")
        btnLuzPasillo.configure(text="Encender", background="#63F2B0")
        
def switchAbanico():
    if (btnAbanico.cget('text') == 'Encender'):
        print("prendo")
        pin11.write(1)
        btnAbanico.configure(text="Apagar", background="#F07EF2")
    elif (btnAbanico.cget('text') == 'Apagar'):
        print("apago")
        pin11.write(0)
        btnAbanico.configure(text="Encender", background="#63F2B0")

def switchPuerta():
    if (btnPuerta.cget('text') == 'Abrir'):
        print("Abrir")
        pin10Servo.write(0)
        btnPuerta.configure(text="Cerrar", background="#F07EF2")
    elif (btnPuerta.cget('text') == 'Cerrar'):
        print("Cerrar")
        pin10Servo.write(105)
        btnPuerta.configure(text="Abrir", background="#63F2B0")


frmHome = tk.Frame(contControles, padx=20, pady=20)
imagenLogo = ImageTk.PhotoImage(Image.open(r'hestia.PNG'))

logo = tk.Label(contControles, image=imagenLogo)
logo.pack()
lblWelcome = tk.Label(contControles, text="Gestione su casa desde aquí:", fg="#0D0D0D", font=("Comic Sans MS", 15))
lblWelcome.pack()

# Home Inputs
homeInputs = tk.Frame(contControles, padx=20, pady=20)
homeInputs.pack()

lblLuces = tk.Label(homeInputs, text="Luces de la casa-->", fg="#F063F2", font=("Comic Sans MS", 10))
lblLuces.grid(row=0, column=0, pady=5)

lblLuzCuarto = tk.Label(homeInputs, text="Luz del Cuarto:", fg="black", font=("Comic Sans MS", 10))
lblLuzCuarto.grid(row=1, column=0, pady=5)
btnLuzCuarto = tk.Button(homeInputs, text="Encender", command=switchLuzCuarto, background="#63F2B0", font=("Comic Sans MS", 10))
btnLuzCuarto.grid(row=1, column=1, pady=5)

lblLuzPasillo = tk.Label(homeInputs, text="Luz del Pasillo:", fg="black", font=("Comic Sans MS", 10))
lblLuzPasillo.grid(row=2, column=0, pady=5)
btnLuzPasillo = tk.Button(homeInputs, text="Encender", command=switchLuzPasillo, background="#63F2B0", font=("Comic Sans MS", 10))
btnLuzPasillo.grid(row=2, column=1, pady=5)

lblAllLuces = tk.Label(homeInputs, text="Todas las luces:", fg="black", font=("Comic Sans MS", 10))
lblAllLuces.grid(row=3, column=0, pady=5)
btnAllLuces = tk.Button(homeInputs, text="Encender todas las luces", command=switchAllLuces, background="#63F2B0", font=("Comic Sans MS", 10))
btnAllLuces.grid(row=3, column=1, pady=5)

lblLuces = tk.Label(homeInputs, text="Abanicos de la casa-->", fg="#F063F2", font=("Comic Sans MS", 10))
lblLuces.grid(row=4, column=0, pady=5)

lblAbanico = tk.Label(homeInputs, text="Abanico del cuarto:", fg="black", font=("Comic Sans MS", 10))
lblAbanico.grid(row=5, column=0, pady=5)
btnAbanico = tk.Button(homeInputs, text="Encender", command=switchAbanico, background="#63F2B0", font=("Comic Sans MS", 10))
btnAbanico.grid(row=5, column=1, pady=5)

lblPuertas = tk.Label(homeInputs, text="Puertas de la casa-->", fg="#F063F2", font=("Comic Sans MS", 10))
lblPuertas.grid(row=6, column=0, pady=5)

lblPuerta = tk.Label(homeInputs, text="Puerta del cuarto:", fg="black", font=("Comic Sans MS", 10))
lblPuerta.grid(row=7, column=0, pady=5)
btnPuerta = tk.Button(homeInputs, text="Abrir", command=switchPuerta, background="#63F2B0", font=("Comic Sans MS", 10))
btnPuerta.grid(row=7, column=1, pady=5)



contControles.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
window.mainloop()
arduino.exit()
