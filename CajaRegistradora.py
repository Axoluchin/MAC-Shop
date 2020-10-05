from tkinter.simpledialog import askstring
from tkinter.messagebox import *
from tkinter import *
import datetime
import os

def Agregar():
    producto = askstring('Producto', '¿Cuál es el nombre del producto?')
    precio = askstring('Precio', '¿Cuál es su precio?')
    
    file = open(f"Productos/{producto}","w")
    file.write(precio)
    file.close()

    lbProductos.delete(0 , END)
    llenar()

    showinfo('Agregado', f'El producto {producto} fue agregado a la lista de productos')

def Historial():
    VentasDias = 0
    ComprasHechas = 0

    lista = os.listdir('Compras')
    for x in lista:
        VentasDias +=1
        lista2 = os.listdir(f'Compras/{x}')
        ComprasHechas +=len(lista2)

    showinfo(f'Historial', 'Dias Vendiendo: {VentasDias}\nTotal de Compras: {ComprasHechas}')
    
def llenar():
    lista = os.listdir('Productos')

    for  producto in lista:
        file = open (f"Productos/{producto}","r")
        Articulo = file.read()
        Articulo = (f"${Articulo}   {producto}")
        lbProductos.insert(END, Articulo)
        file.close()
    
def MenosUnoProducto(): 
    tfListaCompra.config(state=NORMAL)
    tfListaCompra.insert(END, "")
    maximo = tfListaCompra.index(END)
    maximo = float(maximo)
    maximo -=2
    tfListaCompra.delete(maximo,END)
    tfListaCompra.insert(INSERT, "\n")
    tfListaCompra.config(state=DISABLED)
    maximoProducDinero  = (int(maximo)-1)
    restaMax = lbProducDinero.get(maximoProducDinero)
    restaMax = float(restaMax)
    maximoNuevo = lbDineroTotal.get(0)
    maximoNuevo = float(maximoNuevo)
    maximoNuevo -= restaMax

    lbProducDinero.delete(maximoProducDinero)
    lbDineroTotal.insert(END, 0)
    lbDineroTotal.insert(0,maximoNuevo)

def ReiniciarCompra():
    tfListaCompra.config(state=NORMAL)
    tfListaCompra.delete('0.0',END)
    tfListaCompra.config(state=DISABLED)
    lbProducDinero.delete(0 , END)
    lbDineroTotal.delete(0 , END)
    lbDineroTotal.insert(END, 0)

def lista():
    tfListaCompra.config(state=NORMAL) 
    objetos = lbProductos.curselection()
    tienda = os.listdir('Productos')
    esp = "."
    Producto = tienda[objetos[0]]
    fraceEsp = len(Producto)
    while fraceEsp < 50:
        esp = esp + "."
        fraceEsp += 1
    file = open (f"Productos/{Producto}","r")
    precio = file.read()
    file.close() 
    precio = float(precio)
    Producto = (f"{Producto}{esp}${precio}")
    lbProducDinero.insert(END, precio)
    
    tfListaCompra.insert(END, Producto)
    tfListaCompra.insert(END, "\n")
    
    DineroTotal = lbDineroTotal.get(0)
    DineroTotal = float(DineroTotal)
    DineroTotal += precio
    lbDineroTotal.insert(0,DineroTotal)
    tfListaCompra.config(state=DISABLED)

def MoverMenuCompra():
    bComprar.place(y=800)
    bAgregar.grid(pady = 300)
    instituto.grid(pady = 300)
    b20Peso.place(y= 634)
    b50Peso.place(y= 634)
    b100Peso.place(y= 634)
    b200Peso.place(y= 634)
    b500Peso.place(y= 634)
    bregreso.place(y=750)
    lMoney.place(y=515)
    lCantidadExacta.place(y=490)
    eCantidadExacta.place(y= 520)
    bPagar.place(y=565)
    
def Regresar():
    bComprar.place(y=500)
    bAgregar.grid(pady = 0)
    instituto.grid(pady = 0)
    b20Peso.place(y= 800)
    b50Peso.place(y= 800)
    b100Peso.place(y= 800)
    b200Peso.place(y= 800)
    b500Peso.place(y= 800)
    bregreso.place(y=800)
    lMoney.place(y=800)
    lCantidadExacta.place(y=800)
    eCantidadExacta.place(y= 800)
    bPagar.place(y=800)

def CompraProceso():
    Total = lbDineroTotal.get(0)
    DineroUsuario =  float(eCantidadExacta.get())

    if Total <= DineroUsuario:
        Numero = 0
        Compra = tfListaCompra.get(0.0,END)
        Cambio = DineroUsuario - Total
        FechaDeCompra = datetime.date.today()
        Tiempo = datetime.datetime.now()
        Tiempo = str(Tiempo)
        
        try:
            NCompras = os.listdir(f'Compras/{FechaDeCompra}')
        except:
            os.mkdir(f'Compras/{FechaDeCompra}')
            NCompras = os.listdir(f'Compras/{FechaDeCompra}')
        
        try:
            Numero = len (NCompras)
            Numero +=1

        except:
            Numero = 1

        nombre = f"Compra {Numero}.txt"
        file = open(f"Compras/{FechaDeCompra}/{nombre}","w")
        file.write(f"\t\tMAC Shop\n\t{Tiempo}\n\nProductos:\n")
        file.write(Compra)
        file.write(f"Total: ${Total}\nCantidad Pagada: ${DineroUsuario}\nCambio: ${Cambio}")
        file.close()

        eCantidadExacta.delete(first=0,last=22)
        ReiniciarCompra()
        showinfo("Pagado con exito", "Se realizo la compra y se genero su ticket de pago")
        Regresar()
    else:
        showwarning("Insuficiente", "Dinero insuficiente para pagar los productos")
        eCantidadExacta.delete(first=0,last=22)

def Compra20():
    eCantidadExacta.delete(first=0,last=22)
    eCantidadExacta.insert ( 0, "20" )
    CompraProceso()

def Compra50():
    eCantidadExacta.delete(first=0,last=22)
    eCantidadExacta.insert ( 0, "50" )
    CompraProceso()

def Compra100():
    eCantidadExacta.delete(first=0,last=22)
    eCantidadExacta.insert ( 0, "100" )
    CompraProceso()

def Compra200():
    eCantidadExacta.delete(first=0,last=22)
    eCantidadExacta.insert ( 0, "200" )
    CompraProceso()

def Compra500():
    eCantidadExacta.delete(first=0,last=22)
    eCantidadExacta.insert ( 0, "500" )
    CompraProceso()

if __name__ == "__main__":
    ventana = Tk()
    ventana.geometry('1200x820+150+10')
    ventana.resizable(0,0)
    ventana.title('MAC Shop')
    ventana.configure(bg = '#1b3d70')
    ventana.iconbitmap(r'Imagenes/IconoV.ico')

    stListaCompra = Scrollbar(ventana,troughcolor ='#bd8c00' )
    stListaCompra.place(x=680 ,y=10,height=608,bordermode = INSIDE )

    scrollbary = Scrollbar(ventana,troughcolor ='#bd8c00' )
    scrollbary.place(x=1180 ,y=10,height=604,bordermode = INSIDE )

    scrollbary2 = Scrollbar(ventana,troughcolor ='#bd8c00' )
    scrollbary2.place(x=915 ,y=10,height=353,bordermode = INSIDE )

    menu=Menu(ventana,fg = '#f6d5af')
    menu.add_command(label="Crear Producto",command= Agregar)
    menu.add_command(label="Historial",command = Historial)
    ventana.config(m=menu)

    tfListaCompra = Text(ventana, height=26,width=60,foreground="black",font=("ARLRDBD",15),bg= '#F4F6FD', bd=4,insertborderwidth = 5,highlightcolor="#bd8c00",yscrollcommand = stListaCompra.set)
    tfListaCompra.grid(row=0,column=0, sticky=W,padx=15,pady=10)
    stListaCompra.config(command=tfListaCompra.yview)
    tfListaCompra.config(state=DISABLED)

    lbProductos=Listbox(ventana, height=30,width=25, background="#1b3d70",font=("ARLRDBD",13), fg="white",selectbackground="#285292", cursor = "circle",yscrollcommand = scrollbary.set)
    lbProductos.place(x=950 ,y=10)
    scrollbary.config(command=lbProductos.yview)

    lbProducDinero=Listbox(ventana, height=13,width=18, background="#1b3d70",font=("ARLRDBD",15), fg="white",selectbackground="#285292",highlightcolor="#bd8c00",selectmode = "MULTIPLE" ,cursor = "circle",yscrollcommand = scrollbary2.set)
    lbProducDinero.place(x=710,y=10)
    scrollbary2.config(command=lbProducDinero.yview)

    lTotal = Label(ventana, text =" Total: $", bg ='#1b3d70', fg ='#bd8c00')
    lTotal.config(font=("arial",20,"bold"))
    lTotal.place(x=708,y=330)

    lbDineroTotal=Listbox(ventana, height=1,width=8, background="#1b3d70",font=("ARLRDBD",15), fg="white",selectbackground="#285292",highlightcolor="#bd8c00",selectmode = "MULTIPLE" ,cursor = "circle")
    lbDineroTotal.place(x=820,y=335)
    lbDineroTotal.insert(0,0)

    iQuitar = PhotoImage(file="Imagenes/Quitar.png")
    bQuitar = Button(ventana,image=iQuitar,width=100, height=100,bg='#1b3d70',bd=0,activebackground="#285292",command = MenosUnoProducto)
    bQuitar.place(x=710,y=380)

    iReiniciar = PhotoImage(file="Imagenes/Reiniciar.png")
    bReiniciar = Button(ventana,image=iReiniciar,width=100, height=100,bg='#1b3d70',bd=0,activebackground="#285292", command = ReiniciarCompra)
    bReiniciar.place(x=830,y=380)

    iComprar = PhotoImage(file="Imagenes/Comprar.png")
    bComprar = Button(ventana,image=iComprar,width=221, height=101,bg='#1b3d70',bd=0,activebackground="#285292",command = MoverMenuCompra)
    bComprar.place(x=710,y=500)

    iInfo = PhotoImage(file="Imagenes/Manual.png")
    lInfo = Label(ventana, image=iInfo,bg= '#1b3d70')
    lInfo.grid(row=1,column=0, sticky=W,padx=10)

    img = PhotoImage(file="Imagenes/MAC.png")
    instituto = Label(ventana, image=img,bg= '#1b3d70')
    instituto.grid(row=1,column=0, sticky=W,padx=750)

    iAgregar = PhotoImage(file = "Imagenes/Agregar.png")
    bAgregar = Button(ventana,image=iAgregar,width=200, height=150,bg='#1b3d70',bd=0,activebackground="#285292",command=lista)
    bAgregar.grid(row=1, column=0,sticky=W,padx=975)

    #Billetes
    
    i20Peso = PhotoImage(file="Imagenes/20.png")
    b20Peso = Button(ventana,image=i20Peso,width=200, height=150,bg='#1b3d70',bd=0,activebackground="#285292", command= Compra20)
    b20Peso.place(x= 10,y= 800)

    i50Peso = PhotoImage(file="Imagenes/50Pesos.png")
    b50Peso = Button(ventana,image=i50Peso,width=200, height=150,bg='#1b3d70',bd=0,activebackground="#285292", command=Compra50)
    b50Peso.place(x= 240,y= 800)

    i100Peso = PhotoImage(file="Imagenes/100Pesos.png")
    b100Peso = Button(ventana,image=i100Peso,width=200, height=150,bg='#1b3d70',bd=0,activebackground="#285292", command=Compra100)
    b100Peso.place(x= 480,y= 800)
    
    i200Peso = PhotoImage(file="Imagenes/200Pesos.png")
    b200Peso = Button(ventana,image=i200Peso,width=200, height=150,bg='#1b3d70',bd=0,activebackground="#285292", command=Compra200)
    b200Peso.place(x= 720,y= 800)

    i500Peso = PhotoImage(file="Imagenes/500Pesos.png")
    b500Peso = Button(ventana,image=i500Peso,width=200, height=150,bg='#1b3d70',bd=0,activebackground="#285292", command=Compra500)
    b500Peso.place(x= 960,y= 800)

    iregreso = PhotoImage(file="Imagenes/return.png")
    bregreso = Button(ventana,image=iregreso,width=50, height=50,bg='#1b3d70',bd=0,activebackground="#285292",command = Regresar)
    bregreso.place(x= 1150,y= 800)

    lMoney = Label(ventana, text =" $", bg ='#1b3d70', fg ='#bd8c00')
    lMoney.config(font=("arial",26,"bold"))
    lMoney.place(x=715,y=800)

    lCantidadExacta = Label(ventana, text ="Cantidad Exacta:", bg ='#1b3d70', fg ='#bd8c00')
    lCantidadExacta.config(font=("arial",14,"bold"))
    lCantidadExacta.place(x= 745,y= 800)

    eCantidadExacta = Entry(ventana,width="10",font=("ARLRDBD",20))
    eCantidadExacta.place(x= 750,y= 800)

    iPagar = PhotoImage(file="Imagenes/Pagar.png")
    bPagar = Button(ventana,image=iPagar,width=170, height=50,bg='#1b3d70',bd=0,activebackground="#285292", command= CompraProceso)
    bPagar.place(x= 740,y= 800)

    llenar()
    ventana.mainloop()