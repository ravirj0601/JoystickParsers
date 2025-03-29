import configparser 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox




def get_config():
    global LeftJoystickX
    global LeftJoystickY
    global RightJoystickX
    global RightJoystickY
    global LeftTrigger
    global RightTrigger
    global LeftBumper 
    global RightBumper
    global XA 
    global XB
    global XX
    global XY
    global Back 
    global Start
    global Record
    global LeftDPad 
    global RightDPad 
    global UpDPad 
    global DownDPad
    global Xbox
    global A 
    global D 
    global W 
    global S 
    global Up 
    global Down 
    global Left 
    global Right
    global E 
    global R 
    global Z 
    global X 
    global K 
    global J 
    global I 
    global L 
    global Space
    global F 
    global T 
    global Y 
    global V 
    global B 
    global N
    global M
    global O
    global G 
    global H
    global P
    global Q
    global C
    global Disabled 
    
    static_cfg = configparser.ConfigParser()
    static_cfg.read('static.cfg') 
    Disabled = 'disabled'
    LeftJoystickX = static_cfg.get('Xbox','LeftJoystickX')
    LeftJoystickY = static_cfg.get('Xbox','LeftJoystickY')
    RightJoystickX = static_cfg.get('Xbox','RightJoystickX')
    RightJoystickY = static_cfg.get('Xbox','RightJoystickY')
    LeftTrigger = static_cfg.get('Xbox','LeftTrigger')
    RightTrigger = static_cfg.get('Xbox','RightTrigger')
    LeftBumper = static_cfg.get('Xbox','LeftBumper')
    RightBumper = static_cfg.get('Xbox','RightBumper')
    XA = static_cfg.get('Xbox','XA')
    XB = static_cfg.get('Xbox','XB')
    XX = static_cfg.get('Xbox','XX')
    XY = static_cfg.get('Xbox','XY')
    Back = static_cfg.get('Xbox','Back')
    Start = static_cfg.get('Xbox','Start')
    Record = static_cfg.get('Xbox', 'Record')
    LeftDPad = static_cfg.get('Xbox','LeftDPad')
    RightDPad = static_cfg.get('Xbox','RightDPad')
    UpDPad = static_cfg.get('Xbox','UpDPad')
    DownDPad = static_cfg.get('Xbox','DownDPad')
    Xbox = static_cfg.get('Xbox','Xbox')
    A = static_cfg.get('Keyboard','A')
    D = static_cfg.get('Keyboard','D')
    W = static_cfg.get('Keyboard','W')
    S = static_cfg.get('Keyboard','S')
    Up = static_cfg.get('Keyboard','Up')
    Down = static_cfg.get('Keyboard','Down')
    Left = static_cfg.get('Keyboard','Left')
    Right = static_cfg.get('Keyboard','Right')
    E = static_cfg.get('Keyboard','E')
    R = static_cfg.get('Keyboard','R')
    Z = static_cfg.get('Keyboard','Z')
    X = static_cfg.get('Keyboard','X')
    K = static_cfg.get('Keyboard','K')
    J = static_cfg.get('Keyboard','J')
    I = static_cfg.get('Keyboard','I')
    L = static_cfg.get('Keyboard','L')
    Space = static_cfg.get('Keyboard','Space')
    F = static_cfg.get('Keyboard','F')
    T = static_cfg.get('Keyboard','T')
    Y = static_cfg.get('Keyboard','Y')
    V = static_cfg.get('Keyboard','V')
    B = static_cfg.get('Keyboard','B')
    N = static_cfg.get('Keyboard','N')
    C = static_cfg.get('Keyboard','C')
    H = static_cfg.get('Keyboard','H')
    P = static_cfg.get('Keyboard','P')
    Q = static_cfg.get('Keyboard','Q')
    G = static_cfg.get('Keyboard','G')
    O = static_cfg.get('Keyboard','O')
    M = static_cfg.get('Keyboard','M')
     
Devices = [
    "Xbox",
    "Keyboard"
]

xbox_Buttons = [
    "Select",
    "LeftJoystickX",
    "LeftJoystickY",
    "RightJoystickX",
    "RightJoystickY",
    "LeftTrigger",
    "RightTrigger",
    "LeftBumper",
    "RightBumper",
    "XA",
    "XB",
    "XX",
    "XY",
    "Back",
    "Start",
    "Record",
    "LeftDPad",
    "RightDPad",
    "UpDPad",
    "DownDPad",
    "Xbox",
    "Disabled"       
]




keyboard_Buttons = [
    "A",
    "D",
    "W",
    "S",
    "Up",
    "Down",
    "Left",
    "Right",
    "E",
    "R",
    "Z",
    "X",
    "K",
    "J",
    "I",
    "L",
    "Space",
    "F",
    "T",
    "Y",
    "V",
    "B",
    "N",
    "C",
    "M",
    "O",
    "G",
    "H",
    "P",
    "Q",
    "C"
]
    
def save_config():
    config = configparser.ConfigParser()
    # config.read('config.ini')
   
    get_config()
    ##bla_bla_bla_bla_bla_bla
    config['system'] = {
        'Device' : device_Entry.get(),
        'ServerIP' : serverIP_Entry.get()
    }
    
    
    config[device_Entry.get()] = {
    
        'lx' : str(eval(lx_entry.get())), 
        'lxm': str(eval(lxm_entry.get())), 
        'ly' : str(eval(ly_entry.get())), 
        'lym': str(eval(lym_entry.get())),
        'rx' : str(eval(rx_entry.get())), 
        'rxm': str(eval(rxm_entry.get())),
        'ry' : str(eval(ry_entry.get())),
        'rym': str(eval(rym_entry.get())),
        'lt' : str(eval(lt_entry.get())),
        'rt' : str(eval(rt_entry.get())),
        'lb' : str(eval(lb_entry.get())),
        'rb' : str(eval(rb_entry.get())),
        'A' : str(eval(A_entry.get())),
        'X' : str(eval(X_entry.get())),
        'Y' : str(eval(Y_entry.get())),
        'B' : str(eval(B_entry.get())),
        'Back' : str(eval(Back_entry.get())),
        'Start' : str(eval(Start_entry.get())),
        'Record' : str(eval(Record_entry.get())),
        'ld' : str(eval(ld_entry.get())),
        'rd' : str(eval(rd_entry.get())),
        'ud' : str(eval(ud_entry.get())),
        'dd' : str(eval(dd_entry.get())),
        'Xbox' : str(eval(Xbox_entry.get()))
    }
    

    with open('dynamic.ini', 'w') as config_file:
        config.write(config_file)
    messagebox.showinfo("Success","Configurtation updated successfully!")
  

# Create the main window
window = Tk()
window.title("Config File generator")
window.geometry("1100x340")


def pick_Buttons(e):
    if device_Entry.get() == "Xbox":
        lx_entry.config(value= xbox_Buttons)
        lx_entry.current(1)
        ly_entry.config(value = xbox_Buttons)
        ly_entry.current(2)
        ry_entry.config(value = xbox_Buttons)
        ry_entry.current(4)
        rx_entry.config(value=xbox_Buttons)
        rx_entry.current(3)
        lt_entry.config(value=xbox_Buttons)
        lt_entry.current(5)
        rt_entry.config(value=xbox_Buttons)
        rt_entry.current(6)
        lb_entry.config(value=xbox_Buttons)
        lb_entry.current(7)
        rb_entry.config(value=xbox_Buttons)
        rb_entry.current(8)
        A_entry.config(values=xbox_Buttons)
        A_entry.current(9)
        X_entry.config(value=xbox_Buttons)
        X_entry.current(10)
        Y_entry.config(values=xbox_Buttons)
        Y_entry.current(11)
        B_entry.config(values=xbox_Buttons)
        B_entry.current(12)
        Back_entry.config(value=xbox_Buttons)
        Back_entry.current(13)
        Start_entry.config(values=xbox_Buttons)
        Start_entry.current(14)
        ld_entry.config(values=xbox_Buttons)
        ld_entry.current(16)
        rd_entry.config(values=xbox_Buttons)
        rd_entry.current(17)
        ud_entry.config(values=xbox_Buttons)
        ud_entry.current(18)
        dd_entry.config(values=xbox_Buttons)
        dd_entry.current(19)
        Record_entry.config(values = xbox_Buttons)
        Record_entry.current(15)
        Xbox_entry.config(values=xbox_Buttons)
        Xbox_entry.current(20)
        lxm_entry.config(value= xbox_Buttons)
        lxm_entry.current(21)
        lym_entry.config(value= xbox_Buttons)
        lym_entry.current(21)
        rym_entry.config(value = xbox_Buttons)
        rym_entry.current(21)
        rxm_entry.config(value= xbox_Buttons)
        rxm_entry.current(21)

    if device_Entry.get() == "Keyboard":
        lx_entry.config(value= keyboard_Buttons)
        lx_entry.current(0)
        lxm_entry.config(value= keyboard_Buttons)
        lxm_entry.current(1)
        ly_entry.config(value = keyboard_Buttons)
        ly_entry.current(2)
        lym_entry.config(value= keyboard_Buttons)
        lym_entry.current(3)
        ry_entry.config(value = keyboard_Buttons)
        ry_entry.current(14)
        rym_entry.config(valu = keyboard_Buttons)
        rym_entry.current(12)
        rx_entry.config(value=keyboard_Buttons)
        rx_entry.current(15)
        rxm_entry.config(value= keyboard_Buttons)
        rxm_entry.current(13)
        lt_entry.config(value=keyboard_Buttons)
        lt_entry.current(23)
        rt_entry.config(value=keyboard_Buttons)
        rt_entry.current(20)
        lb_entry.config(value=keyboard_Buttons)
        lb_entry.current(21)
        rb_entry.config(value=keyboard_Buttons)
        rb_entry.current(22)
        A_entry.config(values=keyboard_Buttons)
        A_entry.current(5)
        X_entry.config(value=keyboard_Buttons)
        X_entry.current(6)
        Y_entry.config(values=keyboard_Buttons)
        Y_entry.current(4)
        B_entry.config(values=keyboard_Buttons)
        B_entry.current(7)
        Back_entry.config(value=keyboard_Buttons)
        Back_entry.current(29)
        Start_entry.config(values=keyboard_Buttons)
        Start_entry.current(16)
        ld_entry.config(values=keyboard_Buttons)
        ld_entry.current(24)
        rd_entry.config(values=keyboard_Buttons)
        rd_entry.current(25)
        ud_entry.config(values=keyboard_Buttons)
        ud_entry.current(26)
        dd_entry.config(values=keyboard_Buttons)
        dd_entry.current(27)
        Record_entry.config(values=keyboard_Buttons)
        Record_entry.current(9)
        Xbox_entry.config(values=keyboard_Buttons)
        Xbox_entry.current(11)
       
  
# Choosing the Device
device_label = ttk.Label(window, text="Devices:")
device_label.grid(row = 0 ,column=1,padx=10, pady=10)
device_Entry = ttk.Combobox(window, value = Devices, width= 12)
device_Entry.current(0)
device_Entry.grid(row = 0, column=2,padx = 10,pady= 10)
device_Entry.bind("<<ComboboxSelected>>", pick_Buttons)

server_IP = ttk.Label(window, text="Server IP")
server_IP.grid(row=6,column=8,padx = 20)
serverIP_Entry = ttk.Entry(window)
serverIP_Entry.grid(row= 6, column = 9, padx = 10)

device = device_Entry.get()

ly_label = ttk.Label(window, text="ly")
ly_label.grid(row = 1 , column=1, padx=0)
ly_entry = ttk.Combobox(window, values = xbox_Buttons or keyboard_Buttons, width= 12)
ly_entry.grid(row = 1 , column=2, padx=0)
lym_entry = ttk.Combobox(window, value= xbox_Buttons or keyboard_Buttons, width=12)
lym_entry.grid(row=1, column=3) 

lx_label = ttk.Label(window, text="lx")
lx_label.grid(row= 2, column= 1, padx= 0, pady=10)
lx_entry = ttk.Combobox(window, value= xbox_Buttons or keyboard_Buttons, width=12)
lx_entry.grid(row= 2, column= 2)
lxm_entry = ttk.Combobox(window, value=xbox_Buttons or keyboard_Buttons, width=12) 
lxm_entry.grid(row=2, column=3) 

ry_label = ttk.Label(window, text="ry")
ry_label.grid(row= 3, column= 1, padx=0)
ry_entry = ttk.Combobox(window, value= xbox_Buttons or keyboard_Buttons, width=12)
ry_entry.grid(row= 3, column= 2)
rym_entry = ttk.Combobox(window, value= xbox_Buttons or keyboard_Buttons, width = 12)
rym_entry.grid(row = 3, column= 3)

rx_label = ttk.Label(window, text="rx")
rx_label.grid(row= 4, column= 1, padx=0, pady= 10)
rx_entry = ttk.Combobox(window, value= xbox_Buttons or keyboard_Buttons, width= 12)
rx_entry.grid(row= 4, column= 2)
rxm_entry = ttk.Combobox(window, value= xbox_Buttons or keyboard_Buttons, width= 12)
rxm_entry.grid(row = 4, column= 3)

lt_label = ttk.Label(window, text="lt")
lt_label.grid(row= 5, column= 1, padx=0)
lt_entry = ttk.Combobox(window, value= xbox_Buttons or keyboard_Buttons, width= 12)
lt_entry.grid(row= 5, column= 2)

rt_label = ttk.Label(window, text="rt")
rt_label.grid(row= 1, column= 4, padx=10)
rt_entry = ttk.Combobox(window, value= xbox_Buttons or keyboard_Buttons, width=12)
rt_entry.grid(row= 1, column= 5)

lb_label = ttk.Label(window, text="lb")
lb_label.grid(row= 2, column= 4, padx=10)
lb_entry = ttk.Combobox(window, value= xbox_Buttons or keyboard_Buttons, width= 12)
lb_entry.grid(row= 2, column= 5)

rb_label = ttk.Label(window, text="rb")
rb_label.grid(row= 3, column= 4, padx=10)
rb_entry = ttk.Combobox(window, value= xbox_Buttons or keyboard_Buttons, width= 12)
rb_entry.grid(row= 3, column= 5)

A_label = ttk.Label(window, text="A")
A_label.grid(row= 4, column= 4, padx=10)
A_entry = ttk.Combobox(window, value= xbox_Buttons or keyboard_Buttons, width= 12)
A_entry.grid(row= 4, column= 5)

X_label = ttk.Label(window, text="X")
X_label.grid(row= 5, column= 4, padx=10)
X_entry = ttk.Combobox(window, value= xbox_Buttons or keyboard_Buttons, width= 12)
X_entry.grid(row= 5, column= 5)

Y_label = ttk.Label(window, text="Y")
Y_label.grid(row= 1, column= 6, padx=10)
Y_entry = ttk.Combobox(window, value= xbox_Buttons or keyboard_Buttons, width= 12)
Y_entry.grid(row= 1, column= 7)

B_label = ttk.Label(window, text="B")
B_label.grid(row= 2, column= 6, padx=10)
B_entry = ttk.Combobox(window, value= xbox_Buttons or keyboard_Buttons, width= 12)
B_entry.grid(row= 2, column= 7)

Back_label = ttk.Label(window, text="Back")
Back_label.grid(row= 3, column= 6, padx=10)
Back_entry = ttk.Combobox(window, value= xbox_Buttons or keyboard_Buttons, width= 12)
Back_entry.grid(row= 3, column= 7)

Start_label = ttk.Label(window, text="Start")
Start_label.grid(row= 4, column= 6, padx=10)
Start_entry = ttk.Combobox(window, value= xbox_Buttons or keyboard_Buttons, width= 12)
Start_entry.grid(row= 4, column= 7)

ld_label = ttk.Label(window, text="ld")
ld_label.grid(row= 5, column= 6, padx=10)
ld_entry = ttk.Combobox(window, value= xbox_Buttons or keyboard_Buttons, width= 12)
ld_entry.grid(row= 5, column= 7)

rd_label = ttk.Label(window, text="rd")
rd_label.grid(row= 1, column= 8, padx=10)
rd_entry = ttk.Combobox(window, value= xbox_Buttons or keyboard_Buttons, width= 12)
rd_entry.grid(row= 1, column= 9)

ud_label = ttk.Label(window, text="ud")
ud_label.grid(row= 2, column= 8, padx=10)
ud_entry = ttk.Combobox(window, value= xbox_Buttons or keyboard_Buttons,width= 12)
ud_entry.grid(row= 2, column= 9)

dd_label = ttk.Label(window, text="dd")
dd_label.grid(row= 3, column= 8, padx=10)
dd_entry = ttk.Combobox(window, value= xbox_Buttons or keyboard_Buttons, width= 12)
dd_entry.grid(row= 3, column= 9)

Record_label = ttk.Label(window, text="Record")
Record_label.grid(row= 4, column= 8, padx=10)
Record_entry = ttk.Combobox(window, value= xbox_Buttons or keyboard_Buttons, width= 12)
Record_entry.grid(row= 4, column= 9)

Xbox_label = ttk.Label(window, text="Xbox")
Xbox_label.grid(row= 5, column= 8, padx=10)
Xbox_entry = ttk.Combobox(window, value= xbox_Buttons or keyboard_Buttons, width= 12)
Xbox_entry.grid(row= 5, column= 9)








# Create the submit buttonL
save_button = ttk.Button(window, text="Save", command=save_config)
save_button.grid(row = 6, column = 12,padx=10, pady=10)
# Start the main loop
window.mainloop()



