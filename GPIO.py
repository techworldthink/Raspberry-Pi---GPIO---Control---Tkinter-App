from tkinter.ttk import *
from tkinter import*
from tkinter import font
from tkinter import messagebox

class Convert:
    def __init__(self, master):
        self.master = master
        master.title("Raspberry-Pi GPIO Control")
        master.geometry("900x300")
        master.configure(bg="white")

        ButtonVar1 = StringVar()
        
        #full window row configure
        master.grid_rowconfigure(0, weight=1)
   
        #full window column configure
        master.columnconfigure(0, weight=1)
      
        #Fonts
        self.label_frame_font = font.Font(family="Helvetica",size=10,weight="bold")
        self.frame2_font = font.Font(family="Franklin Gothic Medium",size=10)
        

        #SET INDICATORS PROPERTIES
        WIDTH_IND = 10
        WIDTH_LABEL = 10

        #PINS STATE
        IO0,IO1,IO2,IO3,IO4,IO5,IO6,IO7,IO8,IO9,IO10,IO11 = 0,0,0,0,0,0,0,0,0,0,0,0
        C0="red"
        
        #labelled frames
        self.frame_left  =  LabelFrame(master,text="GPIO -ON/OFF",labelanchor="n",bg="white",bd=10,fg="red",font=self.label_frame_font)
      
        #frame grids
        self.frame_left.grid(row=0,column=0,sticky="nsew")
   
        #frame for componants for fisrt labeled frame  row configure  1
        self.frame_left.grid_rowconfigure(0, weight=1)
        self.frame_left.grid_rowconfigure(1, weight=1)
        self.frame_left.grid_rowconfigure(2, weight=1)
        
        self.frame_left.columnconfigure(0, weight=1)
        self.frame_left.columnconfigure(1, weight=1)
        self.frame_left.columnconfigure(2, weight=1)
        self.frame_left.columnconfigure(3, weight=1)
        self.frame_left.columnconfigure(4, weight=1)
        self.frame_left.columnconfigure(5, weight=1)
        self.frame_left.columnconfigure(6, weight=1)
        self.frame_left.columnconfigure(7, weight=1)
        self.frame_left.columnconfigure(8, weight=1)
        self.frame_left.columnconfigure(9, weight=1)
        self.frame_left.columnconfigure(10, weight=1)
        self.frame_left.columnconfigure(11, weight=1)

        #componants for frame 1
        self.Ind_0 = Entry(self.frame_left,bg=C0,fg="green",textvariable = ButtonVar1,width=WIDTH_IND)
        self.Ind_1 = Entry(self.frame_left,bg="white",fg="black",textvariable = ButtonVar1,width=WIDTH_IND)
        self.Ind_2 = Entry(self.frame_left,bg="white",fg="black",textvariable = ButtonVar1,width=WIDTH_IND)
        self.Ind_3 = Entry(self.frame_left,bg="white",fg="black",textvariable = ButtonVar1,width=WIDTH_IND)
        self.Ind_4 = Entry(self.frame_left,bg="white",fg="black",textvariable = ButtonVar1,width=WIDTH_IND)
        self.Ind_5 = Entry(self.frame_left,bg="white",fg="black",textvariable = ButtonVar1,width=WIDTH_IND)
        self.Ind_6 = Entry(self.frame_left,bg="white",fg="black",textvariable = ButtonVar1,width=WIDTH_IND)
        self.Ind_7 = Entry(self.frame_left,bg="white",fg="black",textvariable = ButtonVar1,width=WIDTH_IND)
        self.Ind_8 = Entry(self.frame_left,bg="white",fg="black",textvariable = ButtonVar1,width=WIDTH_IND)
        self.Ind_9 = Entry(self.frame_left,bg="white",fg="black",textvariable = ButtonVar1,width=WIDTH_IND)
        self.Ind_10 = Entry(self.frame_left,bg="white",fg="black",textvariable = ButtonVar1,width=WIDTH_IND)
        self.Ind_11 = Entry(self.frame_left,bg="white",fg="black",textvariable = ButtonVar1,width=WIDTH_IND)

        self.IND_LAB_0 = Label(self.frame_left,text="IO0",padx=10,pady=10,bg="white",fg="black",font=self.frame2_font,width=WIDTH_IND)
        self.IND_LAB_1 = Label(self.frame_left,text="IO1",padx=10,pady=10,bg="white",fg="black",font=self.frame2_font,width=WIDTH_IND)
        self.IND_LAB_2 = Label(self.frame_left,text="IO2",padx=10,pady=10,bg="white",fg="black",font=self.frame2_font,width=WIDTH_IND)
        self.IND_LAB_3 = Label(self.frame_left,text="IO3",padx=10,pady=10,bg="white",fg="black",font=self.frame2_font,width=WIDTH_IND)
        self.IND_LAB_4 = Label(self.frame_left,text="IO4",padx=10,pady=10,bg="white",fg="black",font=self.frame2_font,width=WIDTH_IND)
        self.IND_LAB_5 = Label(self.frame_left,text="IO5",padx=10,pady=10,bg="white",fg="black",font=self.frame2_font,width=WIDTH_IND)
        self.IND_LAB_6 = Label(self.frame_left,text="IO6",padx=10,pady=10,bg="white",fg="black",font=self.frame2_font,width=WIDTH_IND)
        self.IND_LAB_7 = Label(self.frame_left,text="IO7",padx=10,pady=10,bg="white",fg="black",font=self.frame2_font,width=WIDTH_IND)
        self.IND_LAB_8 = Label(self.frame_left,text="IO8",padx=10,pady=10,bg="white",fg="black",font=self.frame2_font,width=WIDTH_IND)
        self.IND_LAB_9 = Label(self.frame_left,text="IO9",padx=10,pady=10,bg="white",fg="black",font=self.frame2_font,width=WIDTH_IND)
        self.IND_LAB_10 = Label(self.frame_left,text="IO10",padx=10,pady=10,bg="white",fg="black",font=self.frame2_font,width=WIDTH_IND)
        self.IND_LAB_11 = Label(self.frame_left,text="IO11",padx=10,pady=10,bg="white",fg="black",font=self.frame2_font,width=WIDTH_IND)
       
        self.IND_BTN_0 = Button(self.frame_left,text="T",height = 1, width = WIDTH_LABEL,bg="#d1d1d1",fg="black",command=lambda:toggle_pin(0))
        self.IND_BTN_1 = Button(self.frame_left,text="T",height = 1, width = WIDTH_LABEL,bg="#d1d1d1",fg="black",command=lambda:toggle_pin(1))
        self.IND_BTN_2 = Button(self.frame_left,text="T",height = 1, width = WIDTH_LABEL,bg="#d1d1d1",fg="black",command=lambda:toggle_pin(2))
        self.IND_BTN_3 = Button(self.frame_left,text="T",height = 1, width = WIDTH_LABEL,bg="#d1d1d1",fg="black",command=lambda:toggle_pin(3))
        self.IND_BTN_4 = Button(self.frame_left,text="T",height = 1, width = WIDTH_LABEL,bg="#d1d1d1",fg="black",command=lambda:toggle_pin(4))
        self.IND_BTN_5 = Button(self.frame_left,text="T",height = 1, width = WIDTH_LABEL,bg="#d1d1d1",fg="black",command=lambda:toggle_pin(5))
        self.IND_BTN_6 = Button(self.frame_left,text="T",height = 1, width = WIDTH_LABEL,bg="#d1d1d1",fg="black",command=lambda:toggle_pin(6))
        self.IND_BTN_7 = Button(self.frame_left,text="T",height = 1, width = WIDTH_LABEL,bg="#d1d1d1",fg="black",command=lambda:toggle_pin(7))
        self.IND_BTN_8 = Button(self.frame_left,text="T",height = 1, width = WIDTH_LABEL,bg="#d1d1d1",fg="black",command=lambda:toggle_pin(8))
        self.IND_BTN_9 = Button(self.frame_left,text="T",height = 1, width = WIDTH_LABEL,bg="#d1d1d1",fg="black",command=lambda:toggle_pin(9))
        self.IND_BTN_10 = Button(self.frame_left,text="T",height = 1, width = WIDTH_LABEL,bg="#d1d1d1",fg="black",command=lambda:toggle_pin(10))
        self.IND_BTN_11 = Button(self.frame_left,text="T",height = 1, width = WIDTH_LABEL,bg="#d1d1d1",fg="black",command=lambda:toggle_pin(11))

        #componants grid for frame 1
        self.Ind_0.grid(row=1,column=0,sticky="w",padx=10,pady=10)
        self.Ind_1.grid(row=1,column=1,sticky="w",padx=10,pady=10)
        self.Ind_2.grid(row=1,column=2,sticky="w",padx=10,pady=10)
        self.Ind_3.grid(row=1,column=3,sticky="w",padx=10,pady=10)
        self.Ind_4.grid(row=1,column=4,sticky="w",padx=10,pady=10)
        self.Ind_5.grid(row=1,column=5,sticky="w",padx=10,pady=10)
        self.Ind_6.grid(row=1,column=6,sticky="w",padx=10,pady=10)
        self.Ind_7.grid(row=1,column=7,sticky="w",padx=10,pady=10)
        self.Ind_8.grid(row=1,column=8,sticky="w",padx=10,pady=10)
        self.Ind_9.grid(row=1,column=9,sticky="w",padx=10,pady=10)
        self.Ind_10.grid(row=1,column=10,sticky="w",padx=10,pady=10)
        self.Ind_11.grid(row=1,column=11,sticky="w",padx=10,pady=10)
        
        self.IND_LAB_0.grid(row=0,column=0,sticky="w")
        self.IND_LAB_1.grid(row=0,column=1,sticky="w")
        self.IND_LAB_2.grid(row=0,column=2,sticky="w")
        self.IND_LAB_3.grid(row=0,column=3,sticky="w")
        self.IND_LAB_4.grid(row=0,column=4,sticky="w")
        self.IND_LAB_5.grid(row=0,column=5,sticky="w")
        self.IND_LAB_6.grid(row=0,column=6,sticky="w")
        self.IND_LAB_7.grid(row=0,column=7,sticky="w")
        self.IND_LAB_8.grid(row=0,column=8,sticky="w")
        self.IND_LAB_9.grid(row=0,column=9,sticky="w")
        self.IND_LAB_10.grid(row=0,column=10,sticky="w")
        self.IND_LAB_11.grid(row=0,column=11,sticky="w")
        
        self.IND_BTN_0.grid(row=2,column=0,sticky="w")
        self.IND_BTN_1.grid(row=2,column=1)
        self.IND_BTN_2.grid(row=2,column=2)
        self.IND_BTN_3.grid(row=2,column=3)
        self.IND_BTN_4.grid(row=2,column=4)
        self.IND_BTN_5.grid(row=2,column=5)
        self.IND_BTN_6.grid(row=2,column=6)
        self.IND_BTN_7.grid(row=2,column=7)
        self.IND_BTN_8.grid(row=2,column=8)
        self.IND_BTN_9.grid(row=2,column=9)
        self.IND_BTN_10.grid(row=2,column=10)
        self.IND_BTN_11.grid(row=2,column=11)


        # -----------------------   define functions here    ----------------------- #

        def set_color():
            global C0
            self.Ind_0.config({"background": C0})

        def get_set_io(PINNO):
            pass
            
        def toggle_pin(PINNO):
            global C0
            C0 ="yellow"
            get_set_io(PINNO)
            set_color()
            
        
       
root = Tk()
hack_gui = Convert(root)
root.mainloop()
