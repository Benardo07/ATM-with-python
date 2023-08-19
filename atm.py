import tkinter as tk
import tkinter.font as font
from tkinter import *

userpin = "123456"
usersaldo = 125000000
expression = ""
nominaluang = ""
nominaltrf = ""
norek = ""
salahpin = 0

# tujuan transfer
norektujuan = "987654321"
namatujuan = "Tuan Kil"

# Tampilan utama
root = tk.Tk()
root.title("ATM")
root.resizable(width=False, height=False)
root.geometry("800x600+300+50")


equation = tk.StringVar()
nom_uang = tk.StringVar()
nom_trf = tk.StringVar()
no_rek = tk.StringVar()

# <editor-fold desc="input pin">
def press(num):
	global expression
	expression += str(num)
	equation.set(expression)

def clear():
	global expression
	expression = ""
	equation.set("")

def enter():
	global expression
	global salahpin
	if salahpin < 2:
		if entry.get() == userpin:
			gantiframe('menu')
		else:
			salahpin += 1
			expression = ""
			equation.set("")
	else:
		gantiframe('slp')


# </editor-fold>

# <editor-fold desc="input nominal">
def pressnom(num):
	global nominaluang
	nominaluang += str(num)
	nom_uang.set(nominaluang)

def clearnom():
	global nominaluang
	nominaluang = ""
	nom_uang.set("")

def enternom():
	global nominaluang
	tariktunai(int(nom_uang.get())*100000)
	nominaluang = ""
	nom_uang.set("")
# </editor-fold>

# <editor-fold desc="input nominal trf">
def presstrf(num):
	global nominaltrf
	nominaltrf += str(num)
	nom_trf.set(nominaltrf)

def cleartrf():
	global nominaltrf
	nominaltrf = ""
	nom_trf.set("")

def entertrf():
	transf1(int(nom_trf.get()))
# </editor-fold>

# <editor-fold desc="input no rek">

def pressrek(num):
	global norek
	norek += str(num)
	no_rek.set(norek)

def clearrek():
	global norek
	norek = ""
	no_rek.set("")

def enterrek():
	global norek
	if no_rek.get() == norektujuan:
		gantiframe('trf3')
	else:
		gantiframe('trfggl')
	norek = ""
	no_rek.set("")
# </editor-fold>

def transf1(nominal):
	global usersaldo
	if nominal > usersaldo:
		gantiframe('lt2')
	else:
		usersaldo -= nominal
		print(usersaldo)
		gantiframe('saldo')
	global nominaltrf
	nominaltrf = ""
	nom_trf.set("")

def tariktunai(nominal):
	global usersaldo
	if nominal > usersaldo:
		gantiframe('lt2')
	else:
		usersaldo -= nominal
		print(usersaldo)
		gantiframe('saldo')

def hapusframe():
	menu_utama.pack_forget()
	layar_pin.pack_forget()
	layar_saldo.pack_forget()
	layar_tarik_1.pack_forget()
	layar_tarik_2.pack_forget()
	layar_tjl.pack_forget()
	layar_trf1.pack_forget()
	layar_trf2.pack_forget()
	layar_trf3.pack_forget()
	layar_sls.pack_forget()
	layar_slp.pack_forget()
	layar_trfggl.pack_forget()

def gantiframe(nama):
	hapusframe()
	if nama == 'menu':
		menu_utama.pack(fill='both', expand=1)
	elif nama == ('pin'):
		layar_pin.pack(fill='both', expand=1)
	elif nama == ('saldo'):
		global uang
		uang.config(text='Rp'+format(usersaldo,',').replace(',','.'))
		layar_saldo.pack(fill='both', expand=1)
	elif nama == ('lt1'):
		layar_tarik_1.pack(fill='both', expand=1)
	elif nama == ('lt2'):
		layar_tarik_2.pack(fill='both', expand=1)
	elif nama == ('tjl'):
		layar_tjl.pack(fill='both', expand=1)
	elif nama == ('trf1'):
		layar_trf1.pack(fill='both', expand=1)
	elif nama == ('trf2'):
		layar_trf2.pack(fill='both', expand=1)
	elif nama == ('trf3'):
		layar_trf3.pack(fill='both', expand=1)
	elif nama == ('sls'):
		layar_sls.pack(fill='both', expand=1)
	elif nama == ('slp'):
		layar_slp.pack(fill='both', expand=1)
	elif nama == ('trfggl'):
		layar_trfggl.pack(fill='both', expand=1)


# <editor-fold desc="Frame menu utama">
menu_utama = Frame(root)
# menu_utama.pack(fill='both', expand=1)

layar = tk.Canvas(menu_utama, width=800, height=600)
layar.pack()
layar.create_rectangle(140, 50, 660, 360, outline="black", fill="#05f")
layar.create_rectangle(200, 380, 600, 600, outline="black", fill="grey")

myFont = font.Font(size=18)
layarFont = font.Font(family='Fixedsys', size=18)

# frame menu utama
head = tk.Label(menu_utama, text='Silakan memilih transaksi', width=25, font=layarFont, fg='yellow', bg='#05f')
head.place(x=195, y=75)

transfer = tk.Label(menu_utama, text='< Transfer', width=10, font=layarFont, fg='yellow', bg='#05f')
transfer.place(x=145, y=150)

tarik_tunai = tk.Label(menu_utama, text='< Tarik tunai', width=13, font=layarFont, fg='yellow', bg='#05f')
tarik_tunai.place(x=145, y=220)

menucek_saldo = tk.Label(menu_utama, text='< Cek saldo', width=11, font=layarFont, fg='yellow', bg='#05f')
menucek_saldo.place(x=145, y=290)

# Tombol kiri layar
btn_a = tk.Button(menu_utama, text='>', command=lambda: gantiframe('trf1'), fg='black', bg='grey', height=0, width=5)
btn_a['font'] = myFont; btn_a.place(x=45, y=150)
btn_b = tk.Button(menu_utama, text='>', command=lambda: gantiframe('lt1'), fg='black', bg='grey', height=0, width=5)
btn_b['font'] = myFont; btn_b.place(x=45, y=220)
btn_c = tk.Button(menu_utama, text='>', command=lambda: gantiframe('saldo'), fg='black', bg='grey', height=0, width=5)
btn_c['font'] = myFont; btn_c.place(x=45, y=290)

# Tombol kanan layar
btn_x = tk.Button(menu_utama, text='<', fg='black', bg='grey', height=0, width=5)
btn_x['font'] = myFont; btn_x.place(x=675, y=150)
btn_y = tk.Button(menu_utama, text='<', fg='black', bg='grey', height=0, width=5)
btn_y['font'] = myFont; btn_y.place(x=675, y=220)
btn_z = tk.Button(menu_utama, text='<', fg='black', bg='grey', height=0, width=5)
btn_z['font'] = myFont; btn_z.place(x=675, y=290)

# Tombol input ATM
button1 = tk.Button(menu_utama, text=' 1 ', fg='black', bg='white', height=0, width=5)
button1['font'] = myFont; button1.place(x=214, y=390)

button2 = tk.Button(menu_utama, text=' 2 ', fg='black', bg='white', height=0, width=5)
button2['font'] = myFont; button2.place(x=298, y=390)

button3 = tk.Button(menu_utama, text=' 3 ', fg='black', bg='white', height=0, width=5)
button3['font'] = myFont; button3.place(x=382, y=390)

button4 = tk.Button(menu_utama, text=' 4 ', fg='black', bg='white', height=0, width=5)
button4['font'] = myFont; button4.place(x=214, y=440)

button5 = tk.Button(menu_utama, text=' 5 ', fg='black', bg='white', height=0, width=5)
button5['font'] = myFont; button5.place(x=298, y=440)

button6 = tk.Button(menu_utama, text=' 6 ', fg='black', bg='white', height=0, width=5)
button6['font'] = myFont; button6.place(x=382, y=440)

button7 = tk.Button(menu_utama, text=' 7 ', fg='black', bg='white', height=0, width=5)
button7['font'] = myFont; button7.place(x=214, y=490)

button8 = tk.Button(menu_utama, text=' 8 ', fg='black', bg='white', height=0, width=5)
button8['font'] = myFont; button8.place(x=298, y=490)

button9 = tk.Button(menu_utama, text=' 9 ', fg='black', bg='white', height=0, width=5)
button9['font'] = myFont; button9.place(x=382, y=490)

button0 = tk.Button(menu_utama, text=' 0 ', fg='black', bg='white', height=0, width=5)
button0['font'] = myFont; button0.place(x=298, y=540)

btn_cancel = tk.Button(menu_utama, text=' CANCEL ', command=lambda: gantiframe('sls'), fg='black', bg='red', height=0, width=8)
btn_cancel['font'] = myFont; btn_cancel.place(x=466, y=390)

btn_clear = tk.Button(menu_utama, text=' CLEAR ', fg='black', bg='yellow', height=0, width=8)
btn_clear['font'] = myFont; btn_clear.place(x=466, y=440)

btn_enter = tk.Button(menu_utama, text=' ENTER ', fg='white', bg='green', height=0, width=8)
btn_enter['font'] = myFont; btn_enter.place(x=466, y=490)
# </editor-fold>

# <editor-fold desc="Frame pin">
layar_pin = Frame(root)
layar_pin.pack(fill='both', expand=1)

layar = tk.Canvas(layar_pin, width=800, height=600)
layar.pack()
layar.create_rectangle(140, 50, 660, 360, outline="black", fill="#05f")
layar.create_rectangle(200, 380, 600, 600, outline="black", fill="grey")

myFont = font.Font(size=18)
layarFont = font.Font(family='Fixedsys', size=18)

# frame pin
pin1 = tk.Label(layar_pin, text='Masukkan PIN', width=15, font=layarFont, fg='yellow', bg='#05f')
pin1.place(x=390, y=135)
pin1 = tk.Label(layar_pin, text='ATM Anda', width=15, font=layarFont, fg='yellow', bg='#05f')
pin1.place(x=390, y=175)
entry = Entry(layar_pin, show='*', width=6, bd=0, font=layarFont, fg='yellow', bg='#05f', textvariable=equation)
entry.place(x=463, y=220)
img = tk.PhotoImage(file="tangan.gif")
tgn = tk.Label(layar_pin, image=img)
tgn.place(x=180, y=125)
ke_menu = tk.Label(layar_pin, text='Benar >', width=7, font=layarFont, fg='yellow', bg='#05f')
ke_menu.place(x=530, y=290)


# Tombol kiri layar
btn_a = tk.Button(layar_pin, text='>', fg='black', bg='grey', height=0, width=5)
btn_a['font'] = myFont; btn_a.place(x=45, y=150)
btn_b = tk.Button(layar_pin, text='>', fg='black', bg='grey', height=0, width=5)
btn_b['font'] = myFont; btn_b.place(x=45, y=220)
btn_b = tk.Button(layar_pin, text='>', fg='black', bg='grey', height=0, width=5)
btn_b['font'] = myFont; btn_b.place(x=45, y=290)

# Tombol kiri layar
btn_x = tk.Button(layar_pin, text='<', fg='black', bg='grey', height=0, width=5)
btn_x['font'] = myFont; btn_x.place(x=675, y=150)
btn_y = tk.Button(layar_pin, text='<', fg='black', bg='grey', height=0, width=5)
btn_y['font'] = myFont; btn_y.place(x=675, y=220)
btn_z = tk.Button(layar_pin, text='<', command=lambda: enter(), fg='black', bg='grey', height=0, width=5)
btn_z['font'] = myFont; btn_z.place(x=675, y=290)

# Tombol input ATM
button1 = tk.Button(layar_pin, text=' 1 ', command=lambda: press(1), fg='black', bg='white', height=0, width=5)
button1['font'] = myFont; button1.place(x=214, y=390)

button2 = tk.Button(layar_pin, text=' 2 ', command=lambda: press(2), fg='black', bg='white', height=0, width=5)
button2['font'] = myFont; button2.place(x=298, y=390)

button3 = tk.Button(layar_pin, text=' 3 ', command=lambda: press(3), fg='black', bg='white', height=0, width=5)
button3['font'] = myFont; button3.place(x=382, y=390)

button4 = tk.Button(layar_pin, text=' 4 ', command=lambda: press(4), fg='black', bg='white', height=0, width=5)
button4['font'] = myFont; button4.place(x=214, y=440)

button5 = tk.Button(layar_pin, text=' 5 ', command=lambda: press(5), fg='black', bg='white', height=0, width=5)
button5['font'] = myFont; button5.place(x=298, y=440)

button6 = tk.Button(layar_pin, text=' 6 ', command=lambda: press(6), fg='black', bg='white', height=0, width=5)
button6['font'] = myFont; button6.place(x=382, y=440)

button7 = tk.Button(layar_pin, text=' 7 ', command=lambda: press(7), fg='black', bg='white', height=0, width=5)
button7['font'] = myFont; button7.place(x=214, y=490)

button8 = tk.Button(layar_pin, text=' 8 ', command=lambda: press(8), fg='black', bg='white', height=0, width=5)
button8['font'] = myFont; button8.place(x=298, y=490)

button9 = tk.Button(layar_pin, text=' 9 ', command=lambda: press(9), fg='black', bg='white', height=0, width=5)
button9['font'] = myFont; button9.place(x=382, y=490)

button0 = tk.Button(layar_pin, text=' 0 ', command=lambda: press(0), fg='black', bg='white', height=0, width=5)
button0['font'] = myFont; button0.place(x=298, y=540)

btn_cancel = tk.Button(layar_pin, text=' CANCEL ', fg='black', bg='red', height=0, width=8)
btn_cancel['font'] = myFont; btn_cancel.place(x=466, y=390)

btn_clear = tk.Button(layar_pin, text=' CLEAR ', command=lambda: clear(), fg='black', bg='yellow', height=0, width=8)
btn_clear['font'] = myFont; btn_clear.place(x=466, y=440)

btn_enter = tk.Button(layar_pin, text=' ENTER ', command=lambda: enter(), fg='white', bg='green', height=0, width=8)
btn_enter['font'] = myFont; btn_enter.place(x=466, y=490)
# </editor-fold>

# <editor-fold desc="Frame cek saldo">
layar_saldo = Frame(root)
# layar_saldo.pack(fill='both', expand=1)

layar = tk.Canvas(layar_saldo, width=800, height=600)
layar.pack()
layar.create_rectangle(140, 50, 660, 360, outline="black", fill="#05f")
layar.create_rectangle(200, 380, 600, 600, outline="black", fill="grey")

myFont = font.Font(size=18)
layarFont = font.Font(family='Fixedsys', size=18)

# frame menu utama
head = tk.Label(layar_saldo, text='Saldo rekening Anda', width=25, font=layarFont, fg='yellow', bg='#05f')
head.place(x=195, y=70)

uang = tk.Label(layar_saldo, text='', width=25, font=layarFont, fg='yellow', bg='#05f')
uang.place(x=195, y=120)

komen1 = tk.Label(layar_saldo, text='Apakah ingin melakukan', width=25, font=layarFont, fg='yellow', bg='#05f')
komen1.place(x=195, y=170)

komen2 = tk.Label(layar_saldo, text='transaksi lagi?', width=25, font=layarFont, fg='yellow', bg='#05f')
komen2.place(x=195, y=220)

jmllain = tk.Label(layar_saldo, text='Ya >', width=4, font=layarFont, fg='yellow', bg='#05f')
jmllain.place(x=580, y=220)
ke_menu = tk.Label(layar_saldo, text='Tidak >', width=7, font=layarFont, fg='yellow', bg='#05f')
ke_menu.place(x=530, y=290)

# Tombol kiri layar
btn_a = tk.Button(layar_saldo, text='>', fg='black', bg='grey', height=0, width=5)
btn_a['font'] = myFont; btn_a.place(x=45, y=150)
btn_b = tk.Button(layar_saldo, text='>', fg='black', bg='grey', height=0, width=5)
btn_b['font'] = myFont; btn_b.place(x=45, y=220)
btn_b = tk.Button(layar_saldo, text='>', fg='black', bg='grey', height=0, width=5)
btn_b['font'] = myFont; btn_b.place(x=45, y=290)

# Tombol kiri layar
btn_x = tk.Button(layar_saldo, text='<', fg='black', bg='grey', height=0, width=5)
btn_x['font'] = myFont; btn_x.place(x=675, y=150)
btn_y = tk.Button(layar_saldo, text='<', command=lambda: gantiframe('menu'), fg='black', bg='grey', height=0, width=5)
btn_y['font'] = myFont; btn_y.place(x=675, y=220)
btn_z = tk.Button(layar_saldo, text='<', command=lambda: gantiframe('sls'), fg='black', bg='grey', height=0, width=5)
btn_z['font'] = myFont; btn_z.place(x=675, y=290)

# Tombol input ATM
button1 = tk.Button(layar_saldo, text=' 1 ', fg='black', bg='white', height=0, width=5)
button1['font'] = myFont; button1.place(x=214, y=390)

button2 = tk.Button(layar_saldo, text=' 2 ', fg='black', bg='white', height=0, width=5)
button2['font'] = myFont; button2.place(x=298, y=390)

button3 = tk.Button(layar_saldo, text=' 3 ', fg='black', bg='white', height=0, width=5)
button3['font'] = myFont; button3.place(x=382, y=390)

button4 = tk.Button(layar_saldo, text=' 4 ', fg='black', bg='white', height=0, width=5)
button4['font'] = myFont; button4.place(x=214, y=440)

button5 = tk.Button(layar_saldo, text=' 5 ', fg='black', bg='white', height=0, width=5)
button5['font'] = myFont; button5.place(x=298, y=440)

button6 = tk.Button(layar_saldo, text=' 6 ', fg='black', bg='white', height=0, width=5)
button6['font'] = myFont; button6.place(x=382, y=440)

button7 = tk.Button(layar_saldo, text=' 7 ', fg='black', bg='white', height=0, width=5)
button7['font'] = myFont; button7.place(x=214, y=490)

button8 = tk.Button(layar_saldo, text=' 8 ', fg='black', bg='white', height=0, width=5)
button8['font'] = myFont; button8.place(x=298, y=490)

button9 = tk.Button(layar_saldo, text=' 9 ', fg='black', bg='white', height=0, width=5)
button9['font'] = myFont; button9.place(x=382, y=490)

button0 = tk.Button(layar_saldo, text=' 0 ', fg='black', bg='white', height=0, width=5)
button0['font'] = myFont; button0.place(x=298, y=540)

btn_cancel = tk.Button(layar_saldo, text=' CANCEL ', command=lambda: gantiframe('sls'), fg='black', bg='red', height=0, width=8)
btn_cancel['font'] = myFont; btn_cancel.place(x=466, y=390)

btn_clear = tk.Button(layar_saldo, text=' CLEAR ', fg='black', bg='yellow', height=0, width=8)
btn_clear['font'] = myFont; btn_clear.place(x=466, y=440)

btn_enter = tk.Button(layar_saldo, text=' ENTER ', fg='white', bg='green', height=0, width=8)
btn_enter['font'] = myFont; btn_enter.place(x=466, y=490)
# </editor-fold>

# <editor-fold desc="Frame tarik tunai 1">
layar_tarik_1 = Frame(root)
# layar_tarik_1.pack(fill='both', expand=1)

layar = tk.Canvas(layar_tarik_1, width=800, height=600)
layar.pack()
layar.create_rectangle(140, 50, 660, 360, outline="black", fill="#05f")
layar.create_rectangle(200, 380, 600, 600, outline="black", fill="grey")

myFont = font.Font(size=18)
layarFont = font.Font(family='Fixedsys', size=18)

# frame menu utama
head = tk.Label(layar_tarik_1, text='(Pecahan uang 100.000)', width=25, font=layarFont, fg='yellow', bg='#05f')
head.place(x=195, y=75)

seratus = tk.Label(layar_tarik_1, text='< 100.000', width=10, font=layarFont, fg='yellow', bg='#05f')
seratus.place(x=145, y=150)
duaratus = tk.Label(layar_tarik_1, text='< 200.000', width=10, font=layarFont, fg='yellow', bg='#05f')
duaratus.place(x=145, y=220)
limaratus = tk.Label(layar_tarik_1, text='< 500.000', width=10, font=layarFont, fg='yellow', bg='#05f')
limaratus.place(x=145, y=290)

sejuta = tk.Label(layar_tarik_1, text='1.000.000 >', width=11, font=layarFont, fg='yellow', bg='#05f')
sejuta.place(x=470, y=150)
jmllain = tk.Label(layar_tarik_1, text='Jumlah lain >', width=13, font=layarFont, fg='yellow', bg='#05f')
jmllain.place(x=435, y=220)
ke_menu = tk.Label(layar_tarik_1, text='Menu utama >', width=12, font=layarFont, fg='yellow', bg='#05f')
ke_menu.place(x=450, y=290)

# Tombol kiri layar
btn_a = tk.Button(layar_tarik_1, text='>', command=lambda: tariktunai(100000), fg='black', bg='grey', height=0, width=5)
btn_a['font'] = myFont; btn_a.place(x=45, y=150)
btn_b = tk.Button(layar_tarik_1, text='>', command=lambda: tariktunai(200000), fg='black', bg='grey', height=0, width=5)
btn_b['font'] = myFont; btn_b.place(x=45, y=220)
btn_b = tk.Button(layar_tarik_1, text='>', command=lambda: tariktunai(500000), fg='black', bg='grey', height=0, width=5)
btn_b['font'] = myFont; btn_b.place(x=45, y=290)

# Tombol kanan layar
btn_x = tk.Button(layar_tarik_1, text='<', command=lambda: tariktunai(1000000), fg='black', bg='grey', height=0, width=5)
btn_x['font'] = myFont; btn_x.place(x=675, y=150)
btn_y = tk.Button(layar_tarik_1, text='<', command=lambda: gantiframe('tjl'), fg='black', bg='grey', height=0, width=5)
btn_y['font'] = myFont; btn_y.place(x=675, y=220)
btn_z = tk.Button(layar_tarik_1, text='<', command=lambda: gantiframe('menu'), fg='black', bg='grey', height=0, width=5)
btn_z['font'] = myFont; btn_z.place(x=675, y=290)

# Tombol input ATM
button1 = tk.Button(layar_tarik_1, text=' 1 ', fg='black', bg='white', height=0, width=5)
button1['font'] = myFont; button1.place(x=214, y=390)

button2 = tk.Button(layar_tarik_1, text=' 2 ', fg='black', bg='white', height=0, width=5)
button2['font'] = myFont; button2.place(x=298, y=390)

button3 = tk.Button(layar_tarik_1, text=' 3 ', fg='black', bg='white', height=0, width=5)
button3['font'] = myFont; button3.place(x=382, y=390)

button4 = tk.Button(layar_tarik_1, text=' 4 ', fg='black', bg='white', height=0, width=5)
button4['font'] = myFont; button4.place(x=214, y=440)

button5 = tk.Button(layar_tarik_1, text=' 5 ', fg='black', bg='white', height=0, width=5)
button5['font'] = myFont; button5.place(x=298, y=440)

button6 = tk.Button(layar_tarik_1, text=' 6 ', fg='black', bg='white', height=0, width=5)
button6['font'] = myFont; button6.place(x=382, y=440)

button7 = tk.Button(layar_tarik_1, text=' 7 ', fg='black', bg='white', height=0, width=5)
button7['font'] = myFont; button7.place(x=214, y=490)

button8 = tk.Button(layar_tarik_1, text=' 8 ', fg='black', bg='white', height=0, width=5)
button8['font'] = myFont; button8.place(x=298, y=490)

button9 = tk.Button(layar_tarik_1, text=' 9 ', fg='black', bg='white', height=0, width=5)
button9['font'] = myFont; button9.place(x=382, y=490)

button0 = tk.Button(layar_tarik_1, text=' 0 ', fg='black', bg='white', height=0, width=5)
button0['font'] = myFont; button0.place(x=298, y=540)

btn_cancel = tk.Button(layar_tarik_1, text=' CANCEL ', command=lambda: gantiframe('sls'), fg='black', bg='red', height=0, width=8)
btn_cancel['font'] = myFont; btn_cancel.place(x=466, y=390)

btn_clear = tk.Button(layar_tarik_1, text=' CLEAR ', fg='black', bg='yellow', height=0, width=8)
btn_clear['font'] = myFont; btn_clear.place(x=466, y=440)

btn_enter = tk.Button(layar_tarik_1, text=' ENTER ', fg='white', bg='green', height=0, width=8)
btn_enter['font'] = myFont; btn_enter.place(x=466, y=490)
# </editor-fold>

# <editor-fold desc="Frame tarik tunai 2">
layar_tarik_2 = Frame(root)
# layar_tarik_2.pack(fill='both', expand=1)

layar = tk.Canvas(layar_tarik_2, width=800, height=600)
layar.pack()
layar.create_rectangle(140, 50, 660, 360, outline="black", fill="#05f")
layar.create_rectangle(200, 380, 600, 600, outline="black", fill="grey")

myFont = font.Font(size=18)
layarFont = font.Font(family='Fixedsys', size=18)

# frame menu utama
head = tk.Label(layar_tarik_2, text='Saldo rekening Anda', width=25, font=layarFont, fg='yellow', bg='#05f')
head.place(x=195, y=75)

komen0 = tk.Label(layar_tarik_2, text='tidak cukup', width=25, font=layarFont, fg='yellow', bg='#05f')
komen0.place(x=195, y=125)

komen1 = tk.Label(layar_tarik_2, text='Apakah ingin melakukan', width=25, font=layarFont, fg='yellow', bg='#05f')
komen1.place(x=195, y=180)

komen2 = tk.Label(layar_tarik_2, text='transaksi lagi?', width=25, font=layarFont, fg='yellow', bg='#05f')
komen2.place(x=195, y=220)

jmllain = tk.Label(layar_tarik_2, text='Ya >', width=4, font=layarFont, fg='yellow', bg='#05f')
jmllain.place(x=580, y=220)
ke_menu = tk.Label(layar_tarik_2, text='Tidak >', width=7, font=layarFont, fg='yellow', bg='#05f')
ke_menu.place(x=530, y=290)

# Tombol kiri layar
btn_a = tk.Button(layar_tarik_2, text='>', fg='black', bg='grey', height=0, width=5)
btn_a['font'] = myFont; btn_a.place(x=45, y=150)
btn_b = tk.Button(layar_tarik_2, text='>', fg='black', bg='grey', height=0, width=5)
btn_b['font'] = myFont; btn_b.place(x=45, y=220)
btn_b = tk.Button(layar_tarik_2, text='>', fg='black', bg='grey', height=0, width=5)
btn_b['font'] = myFont; btn_b.place(x=45, y=290)

# Tombol kiri layar
btn_x = tk.Button(layar_tarik_2, text='<', fg='black', bg='grey', height=0, width=5)
btn_x['font'] = myFont; btn_x.place(x=675, y=150)
btn_y = tk.Button(layar_tarik_2, text='<', command=lambda: gantiframe('menu'), fg='black', bg='grey', height=0, width=5)
btn_y['font'] = myFont; btn_y.place(x=675, y=220)
btn_z = tk.Button(layar_tarik_2, text='<', command=lambda: gantiframe('sls'), fg='black', bg='grey', height=0, width=5)
btn_z['font'] = myFont; btn_z.place(x=675, y=290)

# Tombol input ATM
button1 = tk.Button(layar_tarik_2, text=' 1 ', fg='black', bg='white', height=0, width=5)
button1['font'] = myFont; button1.place(x=214, y=390)

button2 = tk.Button(layar_tarik_2, text=' 2 ', fg='black', bg='white', height=0, width=5)
button2['font'] = myFont; button2.place(x=298, y=390)

button3 = tk.Button(layar_tarik_2, text=' 3 ', fg='black', bg='white', height=0, width=5)
button3['font'] = myFont; button3.place(x=382, y=390)

button4 = tk.Button(layar_tarik_2, text=' 4 ', fg='black', bg='white', height=0, width=5)
button4['font'] = myFont; button4.place(x=214, y=440)

button5 = tk.Button(layar_tarik_2, text=' 5 ', fg='black', bg='white', height=0, width=5)
button5['font'] = myFont; button5.place(x=298, y=440)

button6 = tk.Button(layar_tarik_2, text=' 6 ', fg='black', bg='white', height=0, width=5)
button6['font'] = myFont; button6.place(x=382, y=440)

button7 = tk.Button(layar_tarik_2, text=' 7 ', fg='black', bg='white', height=0, width=5)
button7['font'] = myFont; button7.place(x=214, y=490)

button8 = tk.Button(layar_tarik_2, text=' 8 ', fg='black', bg='white', height=0, width=5)
button8['font'] = myFont; button8.place(x=298, y=490)

button9 = tk.Button(layar_tarik_2, text=' 9 ', fg='black', bg='white', height=0, width=5)
button9['font'] = myFont; button9.place(x=382, y=490)

button0 = tk.Button(layar_tarik_2, text=' 0 ', fg='black', bg='white', height=0, width=5)
button0['font'] = myFont; button0.place(x=298, y=540)

btn_cancel = tk.Button(layar_tarik_2, text=' CANCEL ', command=lambda: gantiframe('sls'), fg='black', bg='red', height=0, width=8)
btn_cancel['font'] = myFont; btn_cancel.place(x=466, y=390)

btn_clear = tk.Button(layar_tarik_2, text=' CLEAR ', fg='black', bg='yellow', height=0, width=8)
btn_clear['font'] = myFont; btn_clear.place(x=466, y=440)

btn_enter = tk.Button(layar_tarik_2, text=' ENTER ', fg='white', bg='green', height=0, width=8)
btn_enter['font'] = myFont; btn_enter.place(x=466, y=490)
# </editor-fold>

# <editor-fold desc="Frame tarik tunai jumlah lain">
layar_tjl = Frame(root)
# layar_tjl.pack(fill='both', expand=1)

layar = tk.Canvas(layar_tjl, width=800, height=600)
layar.pack()
layar.create_rectangle(140, 50, 660, 360, outline="black", fill="#05f")
layar.create_rectangle(200, 380, 600, 600, outline="black", fill="grey")

myFont = font.Font(size=18)
layarFont = font.Font(family='Fixedsys', size=18)

# frame pin
komentarik1 = tk.Label(layar_tjl, text='Masukkan jumlah', width=25, font=layarFont, fg='yellow', bg='#05f')
komentarik1.place(x=200, y=75)
komentarik2 = tk.Label(layar_tjl, text='penarikan tunai', width=25, font=layarFont, fg='yellow', bg='#05f')
komentarik2.place(x=200, y=115)
komentarik3 = tk.Label(layar_tjl, text='(kelipatan 100.000)', width=25, font=layarFont, fg='yellow', bg='#05f')
komentarik3.place(x=200, y=155)
komentarik4 = tk.Label(layar_tjl, text='Rp.', width=3, font=layarFont, fg='yellow', bg='#05f')
komentarik4.place(x=280, y=203)
komentarik5 = tk.Label(layar_tjl, text='00000', width=5, font=layarFont, fg='yellow', bg='#05f')
komentarik5.place(x=430, y=203)
jmltarik = tk.Entry(layar_tjl, width=7, bd=0, justify='right', font=layarFont, fg='yellow', bg='#05f', textvariable=nom_uang)
jmltarik.place(x=319, y=205)
ke_menu = tk.Label(layar_tjl, text='< Menu utama', width=12, font=layarFont, fg='yellow', bg='#05f')
ke_menu.place(x=150, y=290)
jmllain = tk.Label(layar_tjl, text='Benar >', width=7, font=layarFont, fg='yellow', bg='#05f')
jmllain.place(x=530, y=290)


# Tombol kiri layar
btn_a = tk.Button(layar_tjl, text='>', fg='black', bg='grey', height=0, width=5)
btn_a['font'] = myFont; btn_a.place(x=45, y=150)
btn_b = tk.Button(layar_tjl, text='>', fg='black', bg='grey', height=0, width=5)
btn_b['font'] = myFont; btn_b.place(x=45, y=220)
btn_c = tk.Button(layar_tjl, command=lambda: gantiframe('menu'), text='>', fg='black', bg='grey', height=0, width=5)
btn_c['font'] = myFont; btn_c.place(x=45, y=290)

# Tombol kiri layar
btn_x = tk.Button(layar_tjl, text='<', fg='black', bg='grey', height=0, width=5)
btn_x['font'] = myFont; btn_x.place(x=675, y=150)
btn_y = tk.Button(layar_tjl, text='<', fg='black', bg='grey', height=0, width=5)
btn_y['font'] = myFont; btn_y.place(x=675, y=220)
btn_z = tk.Button(layar_tjl, text='<', command=lambda: enternom(), fg='black', bg='grey', height=0, width=5)
btn_z['font'] = myFont; btn_z.place(x=675, y=290)

# Tombol input ATM
button1 = tk.Button(layar_tjl, text=' 1 ', command=lambda: pressnom(1), fg='black', bg='white', height=0, width=5)
button1['font'] = myFont; button1.place(x=214, y=390)

button2 = tk.Button(layar_tjl, text=' 2 ', command=lambda: pressnom(2), fg='black', bg='white', height=0, width=5)
button2['font'] = myFont; button2.place(x=298, y=390)

button3 = tk.Button(layar_tjl, text=' 3 ', command=lambda: pressnom(3), fg='black', bg='white', height=0, width=5)
button3['font'] = myFont; button3.place(x=382, y=390)

button4 = tk.Button(layar_tjl, text=' 4 ', command=lambda: pressnom(4), fg='black', bg='white', height=0, width=5)
button4['font'] = myFont; button4.place(x=214, y=440)

button5 = tk.Button(layar_tjl, text=' 5 ', command=lambda: pressnom(5), fg='black', bg='white', height=0, width=5)
button5['font'] = myFont; button5.place(x=298, y=440)

button6 = tk.Button(layar_tjl, text=' 6 ', command=lambda: pressnom(6), fg='black', bg='white', height=0, width=5)
button6['font'] = myFont; button6.place(x=382, y=440)

button7 = tk.Button(layar_tjl, text=' 7 ', command=lambda: pressnom(7), fg='black', bg='white', height=0, width=5)
button7['font'] = myFont; button7.place(x=214, y=490)

button8 = tk.Button(layar_tjl, text=' 8 ', command=lambda: pressnom(8), fg='black', bg='white', height=0, width=5)
button8['font'] = myFont; button8.place(x=298, y=490)

button9 = tk.Button(layar_tjl, text=' 9 ', command=lambda: pressnom(9), fg='black', bg='white', height=0, width=5)
button9['font'] = myFont; button9.place(x=382, y=490)

button0 = tk.Button(layar_tjl, text=' 0 ', command=lambda: pressnom(0), fg='black', bg='white', height=0, width=5)
button0['font'] = myFont; button0.place(x=298, y=540)

btn_cancel = tk.Button(layar_tjl, text=' CANCEL ', command=lambda: gantiframe('sls'), fg='black', bg='red', height=0, width=8)
btn_cancel['font'] = myFont; btn_cancel.place(x=466, y=390)

btn_clear = tk.Button(layar_tjl, text=' CLEAR ', command=lambda: clearnom(), fg='black', bg='yellow', height=0, width=8)
btn_clear['font'] = myFont; btn_clear.place(x=466, y=440)

btn_enter = tk.Button(layar_tjl, text=' ENTER ', command=lambda: enternom(), fg='white', bg='green', height=0, width=8)
btn_enter['font'] = myFont; btn_enter.place(x=466, y=490)
# </editor-fold>

# <editor-fold desc="Frame transfer 1">
layar_trf1 = Frame(root)
# layar_trf1.pack(fill='both', expand=1)

layar = tk.Canvas(layar_trf1, width=800, height=600)
layar.pack()
layar.create_rectangle(140, 50, 660, 360, outline="black", fill="#05f")
layar.create_rectangle(200, 380, 600, 600, outline="black", fill="grey")

myFont = font.Font(size=18)
layarFont = font.Font(family='Fixedsys', size=18)

# frame pin
komentrf1 = tk.Label(layar_trf1, text='Masukkan nomor', width=25, font=layarFont, fg='yellow', bg='#05f')
komentrf1.place(x=200, y=75)
komentrf2 = tk.Label(layar_trf1, text='rekening tujuan', width=25, font=layarFont, fg='yellow', bg='#05f')
komentrf2.place(x=200, y=115)
ke_menu = tk.Label(layar_trf1, text='< Menu utama', width=12, font=layarFont, fg='yellow', bg='#05f')
ke_menu.place(x=150, y=290)
jmllain = tk.Label(layar_trf1, text='Benar >', width=7, font=layarFont, fg='yellow', bg='#05f')
jmllain.place(x=530, y=290)

rektrf = tk.Entry(layar_trf1, width=9, bd=0, font=layarFont, fg='yellow', bg='#05f', textvariable=no_rek)
rektrf.place(x=325, y=180)

# Tombol kiri layar
btn_a = tk.Button(layar_trf1, text='>', fg='black', bg='grey', height=0, width=5)
btn_a['font'] = myFont; btn_a.place(x=45, y=150)
btn_b = tk.Button(layar_trf1, text='>', fg='black', bg='grey', height=0, width=5)
btn_b['font'] = myFont; btn_b.place(x=45, y=220)
btn_c = tk.Button(layar_trf1, text='>', command=lambda: gantiframe('menu'), fg='black', bg='grey', height=0, width=5)
btn_c['font'] = myFont; btn_c.place(x=45, y=290)

# Tombol kiri layar
btn_x = tk.Button(layar_trf1, text='<', fg='black', bg='grey', height=0, width=5)
btn_x['font'] = myFont; btn_x.place(x=675, y=150)
btn_y = tk.Button(layar_trf1, text='<', fg='black', bg='grey', height=0, width=5)
btn_y['font'] = myFont; btn_y.place(x=675, y=220)
btn_z = tk.Button(layar_trf1, text='<', command=lambda: enterrek(), fg='black', bg='grey', height=0, width=5)
btn_z['font'] = myFont; btn_z.place(x=675, y=290)

# Tombol input ATM
button1 = tk.Button(layar_trf1, text=' 1 ', command=lambda: pressrek(1), fg='black', bg='white', height=0, width=5)
button1['font'] = myFont; button1.place(x=214, y=390)

button2 = tk.Button(layar_trf1, text=' 2 ', command=lambda: pressrek(2), fg='black', bg='white', height=0, width=5)
button2['font'] = myFont; button2.place(x=298, y=390)

button3 = tk.Button(layar_trf1, text=' 3 ', command=lambda: pressrek(3), fg='black', bg='white', height=0, width=5)
button3['font'] = myFont; button3.place(x=382, y=390)

button4 = tk.Button(layar_trf1, text=' 4 ', command=lambda: pressrek(4), fg='black', bg='white', height=0, width=5)
button4['font'] = myFont; button4.place(x=214, y=440)

button5 = tk.Button(layar_trf1, text=' 5 ', command=lambda: pressrek(5), fg='black', bg='white', height=0, width=5)
button5['font'] = myFont; button5.place(x=298, y=440)

button6 = tk.Button(layar_trf1, text=' 6 ', command=lambda: pressrek(6), fg='black', bg='white', height=0, width=5)
button6['font'] = myFont; button6.place(x=382, y=440)

button7 = tk.Button(layar_trf1, text=' 7 ', command=lambda: pressrek(7), fg='black', bg='white', height=0, width=5)
button7['font'] = myFont; button7.place(x=214, y=490)

button8 = tk.Button(layar_trf1, text=' 8 ', command=lambda: pressrek(8), fg='black', bg='white', height=0, width=5)
button8['font'] = myFont; button8.place(x=298, y=490)

button9 = tk.Button(layar_trf1, text=' 9 ', command=lambda: pressrek(9), fg='black', bg='white', height=0, width=5)
button9['font'] = myFont; button9.place(x=382, y=490)

button0 = tk.Button(layar_trf1, text=' 0 ', command=lambda: pressrek(0), fg='black', bg='white', height=0, width=5)
button0['font'] = myFont; button0.place(x=298, y=540)

btn_cancel = tk.Button(layar_trf1, text=' CANCEL ', command=lambda: gantiframe('sls'), fg='black', bg='red', height=0, width=8)
btn_cancel['font'] = myFont; btn_cancel.place(x=466, y=390)

btn_clear = tk.Button(layar_trf1, text=' CLEAR ', command=lambda: clearrek(), fg='black', bg='yellow', height=0, width=8)
btn_clear['font'] = myFont; btn_clear.place(x=466, y=440)

btn_enter = tk.Button(layar_trf1, text=' ENTER ', command=lambda: enterrek(), fg='white', bg='green', height=0, width=8)
btn_enter['font'] = myFont; btn_enter.place(x=466, y=490)
# </editor-fold>

# <editor-fold desc="Frame transfer 2">
layar_trf2 = Frame(root)
# layar_trf2.pack(fill='both', expand=1)

layar = tk.Canvas(layar_trf2, width=800, height=600)
layar.pack()
layar.create_rectangle(140, 50, 660, 360, outline="black", fill="#05f")
layar.create_rectangle(200, 380, 600, 600, outline="black", fill="grey")

myFont = font.Font(size=18)
layarFont = font.Font(family='Fixedsys', size=18)

# frame pin
komentarik1 = tk.Label(layar_trf2, text='Masukkan jumlah', width=25, font=layarFont, fg='yellow', bg='#05f')
komentarik1.place(x=200, y=70)
komentarik2 = tk.Label(layar_trf2, text='transfer tunai', width=25, font=layarFont, fg='yellow', bg='#05f')
komentarik2.place(x=200, y=120)
komentarik3 = tk.Label(layar_trf2, text='Rp.', width=3, font=layarFont, fg='yellow', bg='#05f')
komentarik3.place(x=280, y=173)
jmltarik = tk.Entry(layar_trf2, width=12, bd=0, justify='right', font=layarFont, fg='yellow', bg='#05f', textvariable=nom_trf)
jmltarik.place(x=319, y=175)
jmllain = tk.Label(layar_trf2, text='Benar >', width=7, font=layarFont, fg='yellow', bg='#05f')
jmllain.place(x=530, y=290)

# Tombol kiri layar
btn_a = tk.Button(layar_trf2, text='>', fg='black', bg='grey', height=0, width=5)
btn_a['font'] = myFont; btn_a.place(x=45, y=150)
btn_b = tk.Button(layar_trf2, text='>', fg='black', bg='grey', height=0, width=5)
btn_b['font'] = myFont; btn_b.place(x=45, y=220)
btn_b = tk.Button(layar_trf2, text='>', fg='black', bg='grey', height=0, width=5)
btn_b['font'] = myFont; btn_b.place(x=45, y=290)

# Tombol kiri layar
btn_x = tk.Button(layar_trf2, text='<', fg='black', bg='grey', height=0, width=5)
btn_x['font'] = myFont; btn_x.place(x=675, y=150)
btn_y = tk.Button(layar_trf2, text='<', fg='black', bg='grey', height=0, width=5)
btn_y['font'] = myFont; btn_y.place(x=675, y=220)
btn_z = tk.Button(layar_trf2, text='<', command=lambda: transf1(int(nom_trf.get())), fg='black', bg='grey', height=0, width=5)
btn_z['font'] = myFont; btn_z.place(x=675, y=290)

# Tombol input ATM
button1 = tk.Button(layar_trf2, text=' 1 ', command=lambda: presstrf(1), fg='black', bg='white', height=0, width=5)
button1['font'] = myFont; button1.place(x=214, y=390)

button2 = tk.Button(layar_trf2, text=' 2 ', command=lambda: presstrf(2), fg='black', bg='white', height=0, width=5)
button2['font'] = myFont; button2.place(x=298, y=390)

button3 = tk.Button(layar_trf2, text=' 3 ', command=lambda: presstrf(3), fg='black', bg='white', height=0, width=5)
button3['font'] = myFont; button3.place(x=382, y=390)

button4 = tk.Button(layar_trf2, text=' 4 ', command=lambda: presstrf(4), fg='black', bg='white', height=0, width=5)
button4['font'] = myFont; button4.place(x=214, y=440)

button5 = tk.Button(layar_trf2, text=' 5 ', command=lambda: presstrf(5), fg='black', bg='white', height=0, width=5)
button5['font'] = myFont; button5.place(x=298, y=440)

button6 = tk.Button(layar_trf2, text=' 6 ', command=lambda: presstrf(6), fg='black', bg='white', height=0, width=5)
button6['font'] = myFont; button6.place(x=382, y=440)

button7 = tk.Button(layar_trf2, text=' 7 ', command=lambda: presstrf(7), fg='black', bg='white', height=0, width=5)
button7['font'] = myFont; button7.place(x=214, y=490)

button8 = tk.Button(layar_trf2, text=' 8 ', command=lambda: presstrf(8), fg='black', bg='white', height=0, width=5)
button8['font'] = myFont; button8.place(x=298, y=490)

button9 = tk.Button(layar_trf2, text=' 9 ', command=lambda: presstrf(9), fg='black', bg='white', height=0, width=5)
button9['font'] = myFont; button9.place(x=382, y=490)

button0 = tk.Button(layar_trf2, text=' 0 ', command=lambda: presstrf(0), fg='black', bg='white', height=0, width=5)
button0['font'] = myFont; button0.place(x=298, y=540)

btn_cancel = tk.Button(layar_trf2, text=' CANCEL ', command=lambda: gantiframe('sls'), fg='black', bg='red', height=0, width=8)
btn_cancel['font'] = myFont; btn_cancel.place(x=466, y=390)

btn_clear = tk.Button(layar_trf2, text=' CLEAR ', command=lambda: cleartrf(), fg='black', bg='yellow', height=0, width=8)
btn_clear['font'] = myFont; btn_clear.place(x=466, y=440)

btn_enter = tk.Button(layar_trf2, text=' ENTER ', command=lambda: transf1(int(nom_trf.get())), fg='white', bg='green', height=0, width=8)
btn_enter['font'] = myFont; btn_enter.place(x=466, y=490)
# </editor-fold>

# <editor-fold desc="Frame transfer 3">
layar_trf3 = Frame(root)
# layar_trf3.pack(fill='both', expand=1)

layar = tk.Canvas(layar_trf3, width=800, height=600)
layar.pack()
layar.create_rectangle(140, 50, 660, 360, outline="black", fill="#05f")
layar.create_rectangle(200, 380, 600, 600, outline="black", fill="grey")

myFont = font.Font(size=18)
layarFont = font.Font(family='Fixedsys', size=18)

# frame menu utama
head = tk.Label(layar_trf3, text='Konfirmasi transfer', width=25, font=layarFont, fg='yellow', bg='#05f')
head.place(x=195, y=75)

head = tk.Label(layar_trf3, text='Ke rek: '+norektujuan, anchor='w', width=20, font=layarFont, fg='yellow', bg='#05f')
head.place(x=170, y=130)
head = tk.Label(layar_trf3, text='Nama  : '+namatujuan, anchor='w', width=20, font=layarFont, fg='yellow', bg='#05f')
head.place(x=170, y=180)

jmllain = tk.Label(layar_trf3, text='Ya >', width=4, font=layarFont, fg='yellow', bg='#05f')
jmllain.place(x=580, y=220)
ke_menu = tk.Label(layar_trf3, text='Tidak >', width=7, font=layarFont, fg='yellow', bg='#05f')
ke_menu.place(x=530, y=290)

# Tombol kiri layar
btn_a = tk.Button(layar_trf3, text='>', fg='black', bg='grey', height=0, width=5)
btn_a['font'] = myFont; btn_a.place(x=45, y=150)
btn_b = tk.Button(layar_trf3, text='>', fg='black', bg='grey', height=0, width=5)
btn_b['font'] = myFont; btn_b.place(x=45, y=220)
btn_b = tk.Button(layar_trf3, text='>', fg='black', bg='grey', height=0, width=5)
btn_b['font'] = myFont; btn_b.place(x=45, y=290)

# Tombol kiri layar
btn_x = tk.Button(layar_trf3, text='<', fg='black', bg='grey', height=0, width=5)
btn_x['font'] = myFont; btn_x.place(x=675, y=150)
btn_y = tk.Button(layar_trf3, text='<', command=lambda: gantiframe('trf2'), fg='black', bg='grey', height=0, width=5)
btn_y['font'] = myFont; btn_y.place(x=675, y=220)
btn_z = tk.Button(layar_trf3, text='<', command=lambda: gantiframe('trf1'), fg='black', bg='grey', height=0, width=5)
btn_z['font'] = myFont; btn_z.place(x=675, y=290)

# Tombol input ATM
button1 = tk.Button(layar_trf3, text=' 1 ', fg='black', bg='white', height=0, width=5)
button1['font'] = myFont; button1.place(x=214, y=390)

button2 = tk.Button(layar_trf3, text=' 2 ', fg='black', bg='white', height=0, width=5)
button2['font'] = myFont; button2.place(x=298, y=390)

button3 = tk.Button(layar_trf3, text=' 3 ', fg='black', bg='white', height=0, width=5)
button3['font'] = myFont; button3.place(x=382, y=390)

button4 = tk.Button(layar_trf3, text=' 4 ', fg='black', bg='white', height=0, width=5)
button4['font'] = myFont; button4.place(x=214, y=440)

button5 = tk.Button(layar_trf3, text=' 5 ', fg='black', bg='white', height=0, width=5)
button5['font'] = myFont; button5.place(x=298, y=440)

button6 = tk.Button(layar_trf3, text=' 6 ', fg='black', bg='white', height=0, width=5)
button6['font'] = myFont; button6.place(x=382, y=440)

button7 = tk.Button(layar_trf3, text=' 7 ', fg='black', bg='white', height=0, width=5)
button7['font'] = myFont; button7.place(x=214, y=490)

button8 = tk.Button(layar_trf3, text=' 8 ', fg='black', bg='white', height=0, width=5)
button8['font'] = myFont; button8.place(x=298, y=490)

button9 = tk.Button(layar_trf3, text=' 9 ', fg='black', bg='white', height=0, width=5)
button9['font'] = myFont; button9.place(x=382, y=490)

button0 = tk.Button(layar_trf3, text=' 0 ', fg='black', bg='white', height=0, width=5)
button0['font'] = myFont; button0.place(x=298, y=540)

btn_cancel = tk.Button(layar_trf3, text=' CANCEL ', command=lambda: gantiframe('sls'), fg='black', bg='red', height=0, width=8)
btn_cancel['font'] = myFont; btn_cancel.place(x=466, y=390)

btn_clear = tk.Button(layar_trf3, text=' CLEAR ', fg='black', bg='yellow', height=0, width=8)
btn_clear['font'] = myFont; btn_clear.place(x=466, y=440)

btn_enter = tk.Button(layar_trf3, text=' ENTER ', fg='white', bg='green', height=0, width=8)
btn_enter['font'] = myFont; btn_enter.place(x=466, y=490)
# </editor-fold>

# <editor-fold desc="Frame trf gagal">
layar_trfggl = Frame(root)
# layar_trfggl.pack(fill='both', expand=1)

layar = tk.Canvas(layar_trfggl, width=800, height=600)
layar.pack()
layar.create_rectangle(140, 50, 660, 360, outline="black", fill="#05f")
layar.create_rectangle(200, 380, 600, 600, outline="black", fill="grey")

myFont = font.Font(size=18)
layarFont = font.Font(family='Fixedsys', size=18)

# frame menu utama
head = tk.Label(layar_trfggl, text='Transaksi gagal', width=25, font=layarFont, fg='yellow', bg='#05f')
head.place(x=195, y=70)

komen0 = tk.Label(layar_trfggl, text='Nomor rekening tak ditemukan', width=30, font=layarFont, fg='yellow', bg='#05f')
komen0.place(x=155, y=120)

komen1 = tk.Label(layar_trfggl, text='Apakah ingin melakukan', width=25, font=layarFont, fg='yellow', bg='#05f')
komen1.place(x=195, y=170)

komen2 = tk.Label(layar_trfggl, text='transaksi lagi?', width=25, font=layarFont, fg='yellow', bg='#05f')
komen2.place(x=195, y=220)

jmllain = tk.Label(layar_trfggl, text='Ya >', width=4, font=layarFont, fg='yellow', bg='#05f')
jmllain.place(x=580, y=220)
ke_menu = tk.Label(layar_trfggl, text='Tidak >', width=7, font=layarFont, fg='yellow', bg='#05f')
ke_menu.place(x=530, y=290)

# Tombol kiri layar
btn_a = tk.Button(layar_trfggl, text='>', fg='black', bg='grey', height=0, width=5)
btn_a['font'] = myFont; btn_a.place(x=45, y=150)
btn_b = tk.Button(layar_trfggl, text='>', fg='black', bg='grey', height=0, width=5)
btn_b['font'] = myFont; btn_b.place(x=45, y=220)
btn_b = tk.Button(layar_trfggl, text='>', fg='black', bg='grey', height=0, width=5)
btn_b['font'] = myFont; btn_b.place(x=45, y=290)

# Tombol kanan layar
btn_x = tk.Button(layar_trfggl, text='<', fg='black', bg='grey', height=0, width=5)
btn_x['font'] = myFont; btn_x.place(x=675, y=150)
btn_y = tk.Button(layar_trfggl, text='<', command=lambda: gantiframe('menu'), fg='black', bg='grey', height=0, width=5)
btn_y['font'] = myFont; btn_y.place(x=675, y=220)
btn_z = tk.Button(layar_trfggl, text='<', command=lambda: gantiframe('sls'), fg='black', bg='grey', height=0, width=5)
btn_z['font'] = myFont; btn_z.place(x=675, y=290)

# Tombol input ATM
button1 = tk.Button(layar_trfggl, text=' 1 ', fg='black', bg='white', height=0, width=5)
button1['font'] = myFont; button1.place(x=214, y=390)

button2 = tk.Button(layar_trfggl, text=' 2 ', fg='black', bg='white', height=0, width=5)
button2['font'] = myFont; button2.place(x=298, y=390)

button3 = tk.Button(layar_trfggl, text=' 3 ', fg='black', bg='white', height=0, width=5)
button3['font'] = myFont; button3.place(x=382, y=390)

button4 = tk.Button(layar_trfggl, text=' 4 ', fg='black', bg='white', height=0, width=5)
button4['font'] = myFont; button4.place(x=214, y=440)

button5 = tk.Button(layar_trfggl, text=' 5 ', fg='black', bg='white', height=0, width=5)
button5['font'] = myFont; button5.place(x=298, y=440)

button6 = tk.Button(layar_trfggl, text=' 6 ', fg='black', bg='white', height=0, width=5)
button6['font'] = myFont; button6.place(x=382, y=440)

button7 = tk.Button(layar_trfggl, text=' 7 ', fg='black', bg='white', height=0, width=5)
button7['font'] = myFont; button7.place(x=214, y=490)

button8 = tk.Button(layar_trfggl, text=' 8 ', fg='black', bg='white', height=0, width=5)
button8['font'] = myFont; button8.place(x=298, y=490)

button9 = tk.Button(layar_trfggl, text=' 9 ', fg='black', bg='white', height=0, width=5)
button9['font'] = myFont; button9.place(x=382, y=490)

button0 = tk.Button(layar_trfggl, text=' 0 ', fg='black', bg='white', height=0, width=5)
button0['font'] = myFont; button0.place(x=298, y=540)

btn_cancel = tk.Button(layar_trfggl, text=' CANCEL ', command=lambda: gantiframe('sls'), fg='black', bg='red', height=0, width=8)
btn_cancel['font'] = myFont; btn_cancel.place(x=466, y=390)

btn_clear = tk.Button(layar_trfggl, text=' CLEAR ', fg='black', bg='yellow', height=0, width=8)
btn_clear['font'] = myFont; btn_clear.place(x=466, y=440)

btn_enter = tk.Button(layar_trfggl, text=' ENTER ', fg='white', bg='green', height=0, width=8)
btn_enter['font'] = myFont; btn_enter.place(x=466, y=490)
# </editor-fold>

# <editor-fold desc="Frame selesai">
layar_sls = Frame(root)
# layar_sls.pack(fill='both', expand=1)

layar = tk.Canvas(layar_sls, width=800, height=600)
layar.pack()
layar.create_rectangle(140, 50, 660, 360, outline="black", fill="#05f")
layar.create_rectangle(200, 380, 600, 600, outline="black", fill="grey")

myFont = font.Font(size=18)
layarFont = font.Font(family='Fixedsys', size=18)

# frame menu utama
head = tk.Label(layar_sls, text='Terima kasih', width=25, font=layarFont, fg='yellow', bg='#05f')
head.place(x=195, y=120)

komen0 = tk.Label(layar_sls, text='telah menggunakan', width=30, font=layarFont, fg='yellow', bg='#05f')
komen0.place(x=155, y=170)

komen1 = tk.Label(layar_sls, text='layanan bank kami', width=25, font=layarFont, fg='yellow', bg='#05f')
komen1.place(x=195, y=220)

# Tombol kiri layar
btn_a = tk.Button(layar_sls, text='>', fg='black', bg='grey', height=0, width=5)
btn_a['font'] = myFont; btn_a.place(x=45, y=150)
btn_b = tk.Button(layar_sls, text='>', fg='black', bg='grey', height=0, width=5)
btn_b['font'] = myFont; btn_b.place(x=45, y=220)
btn_b = tk.Button(layar_sls, text='>', fg='black', bg='grey', height=0, width=5)
btn_b['font'] = myFont; btn_b.place(x=45, y=290)

# Tombol kanan layar
btn_x = tk.Button(layar_sls, text='<', fg='black', bg='grey', height=0, width=5)
btn_x['font'] = myFont; btn_x.place(x=675, y=150)
btn_y = tk.Button(layar_sls, text='<', fg='black', bg='grey', height=0, width=5)
btn_y['font'] = myFont; btn_y.place(x=675, y=220)
btn_z = tk.Button(layar_sls, text='<', fg='black', bg='grey', height=0, width=5)
btn_z['font'] = myFont; btn_z.place(x=675, y=290)

# Tombol input ATM
button1 = tk.Button(layar_sls, text=' 1 ', fg='black', bg='white', height=0, width=5)
button1['font'] = myFont; button1.place(x=214, y=390)

button2 = tk.Button(layar_sls, text=' 2 ', fg='black', bg='white', height=0, width=5)
button2['font'] = myFont; button2.place(x=298, y=390)

button3 = tk.Button(layar_sls, text=' 3 ', fg='black', bg='white', height=0, width=5)
button3['font'] = myFont; button3.place(x=382, y=390)

button4 = tk.Button(layar_sls, text=' 4 ', fg='black', bg='white', height=0, width=5)
button4['font'] = myFont; button4.place(x=214, y=440)

button5 = tk.Button(layar_sls, text=' 5 ', fg='black', bg='white', height=0, width=5)
button5['font'] = myFont; button5.place(x=298, y=440)

button6 = tk.Button(layar_sls, text=' 6 ', fg='black', bg='white', height=0, width=5)
button6['font'] = myFont; button6.place(x=382, y=440)

button7 = tk.Button(layar_sls, text=' 7 ', fg='black', bg='white', height=0, width=5)
button7['font'] = myFont; button7.place(x=214, y=490)

button8 = tk.Button(layar_sls, text=' 8 ', fg='black', bg='white', height=0, width=5)
button8['font'] = myFont; button8.place(x=298, y=490)

button9 = tk.Button(layar_sls, text=' 9 ', fg='black', bg='white', height=0, width=5)
button9['font'] = myFont; button9.place(x=382, y=490)

button0 = tk.Button(layar_sls, text=' 0 ', fg='black', bg='white', height=0, width=5)
button0['font'] = myFont; button0.place(x=298, y=540)

btn_cancel = tk.Button(layar_sls, text=' CANCEL ', fg='black', bg='red', height=0, width=8)
btn_cancel['font'] = myFont; btn_cancel.place(x=466, y=390)

btn_clear = tk.Button(layar_sls, text=' CLEAR ', fg='black', bg='yellow', height=0, width=8)
btn_clear['font'] = myFont; btn_clear.place(x=466, y=440)

btn_enter = tk.Button(layar_sls, text=' ENTER ', fg='white', bg='green', height=0, width=8)
btn_enter['font'] = myFont; btn_enter.place(x=466, y=490)
# </editor-fold>

# <editor-fold desc="Frame salah pin">
layar_slp = Frame(root)
# layar_slp.pack(fill='both', expand=1)

layar = tk.Canvas(layar_slp, width=800, height=600)
layar.pack()
layar.create_rectangle(140, 50, 660, 360, outline="black", fill="#05f")
layar.create_rectangle(200, 380, 600, 600, outline="black", fill="grey")

myFont = font.Font(size=18)
layarFont = font.Font(family='Fixedsys', size=18)

# frame menu utama
head = tk.Label(layar_slp, text='Salah PIN', width=25, font=layarFont, fg='yellow', bg='#05f')
head.place(x=195, y=120)

komen0 = tk.Label(layar_slp, text='telah melampaui batas', width=30, font=layarFont, fg='yellow', bg='#05f')
komen0.place(x=155, y=170)

# Tombol kiri layar
btn_a = tk.Button(layar_slp, text='>', fg='black', bg='grey', height=0, width=5)
btn_a['font'] = myFont; btn_a.place(x=45, y=150)
btn_b = tk.Button(layar_slp, text='>', fg='black', bg='grey', height=0, width=5)
btn_b['font'] = myFont; btn_b.place(x=45, y=220)
btn_b = tk.Button(layar_slp, text='>', fg='black', bg='grey', height=0, width=5)
btn_b['font'] = myFont; btn_b.place(x=45, y=290)

# Tombol kanan layar
btn_x = tk.Button(layar_slp, text='<', fg='black', bg='grey', height=0, width=5)
btn_x['font'] = myFont; btn_x.place(x=675, y=150)
btn_y = tk.Button(layar_slp, text='<', fg='black', bg='grey', height=0, width=5)
btn_y['font'] = myFont; btn_y.place(x=675, y=220)
btn_z = tk.Button(layar_slp, text='<', fg='black', bg='grey', height=0, width=5)
btn_z['font'] = myFont; btn_z.place(x=675, y=290)

# Tombol input ATM
button1 = tk.Button(layar_slp, text=' 1 ', fg='black', bg='white', height=0, width=5)
button1['font'] = myFont; button1.place(x=214, y=390)

button2 = tk.Button(layar_slp, text=' 2 ', fg='black', bg='white', height=0, width=5)
button2['font'] = myFont; button2.place(x=298, y=390)

button3 = tk.Button(layar_slp, text=' 3 ', fg='black', bg='white', height=0, width=5)
button3['font'] = myFont; button3.place(x=382, y=390)

button4 = tk.Button(layar_slp, text=' 4 ', fg='black', bg='white', height=0, width=5)
button4['font'] = myFont; button4.place(x=214, y=440)

button5 = tk.Button(layar_slp, text=' 5 ', fg='black', bg='white', height=0, width=5)
button5['font'] = myFont; button5.place(x=298, y=440)

button6 = tk.Button(layar_slp, text=' 6 ', fg='black', bg='white', height=0, width=5)
button6['font'] = myFont; button6.place(x=382, y=440)

button7 = tk.Button(layar_slp, text=' 7 ', fg='black', bg='white', height=0, width=5)
button7['font'] = myFont; button7.place(x=214, y=490)

button8 = tk.Button(layar_slp, text=' 8 ', fg='black', bg='white', height=0, width=5)
button8['font'] = myFont; button8.place(x=298, y=490)

button9 = tk.Button(layar_slp, text=' 9 ', fg='black', bg='white', height=0, width=5)
button9['font'] = myFont; button9.place(x=382, y=490)

button0 = tk.Button(layar_slp, text=' 0 ', fg='black', bg='white', height=0, width=5)
button0['font'] = myFont; button0.place(x=298, y=540)

btn_cancel = tk.Button(layar_slp, text=' CANCEL ', fg='black', bg='red', height=0, width=8)
btn_cancel['font'] = myFont; btn_cancel.place(x=466, y=390)

btn_clear = tk.Button(layar_slp, text=' CLEAR ', fg='black', bg='yellow', height=0, width=8)
btn_clear['font'] = myFont; btn_clear.place(x=466, y=440)

btn_enter = tk.Button(layar_slp, text=' ENTER ', fg='white', bg='green', height=0, width=8)
btn_enter['font'] = myFont; btn_enter.place(x=466, y=490)
# </editor-fold>

root.mainloop()
