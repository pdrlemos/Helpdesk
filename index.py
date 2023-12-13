#importar bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser
#Criar janela
jan = Tk()
jan.title('HELPDESK - LOGIN PANEL')
jan.geometry("650x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes('-alpha', 0.9)


#Carregar Imagem
logo = PhotoImage(file="Icons/apple.png")

#Widgets
LeftFrame = Frame(jan, width=250, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=0, y=0)

UserLabel = Label(RightFrame, text="Username:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
UserLabel.place(x=5, y=75)

UserEntry = ttk.Entry(RightFrame, width=20)
UserEntry.place(x=150, y=75)

PassLabel = Label(RightFrame, text="Password:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
PassLabel.place(x=5, y=150)

PassEntry = ttk.Entry(RightFrame, width=20, show="*")
PassEntry.place(x=150, y=150)


def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()
    
    DataBaser.cursor.execute("""
    SELECT * FROM Users
    WHERE User = ? AND Password = ?
    """, (User, Pass))
    print("Selecionou")
    VerifyLogin = DataBaser.cursor.fetchone()
    try:
        if (User in VerifyLogin and Pass in VerifyLogin):
            messagebox.showinfo(title="Login Info", message="Acesso Confirmado. Bem Vindo!")
    except:
        messagebox.showinfo(title="Login Info", message="Acesso Negado. Verifique se esta cadastrado!")

#Botoes
LoginButton = ttk.Button(RightFrame, text="Login", width=20, command=Login)
LoginButton.place(x=90, y=210)

def Register():
    #Removendo Widget de Login
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)
    #Inserindo widgets de cadatro
    NomeLabel = Label(RightFrame, text="Nome:", font=("Century Ghothic", 20), bg="MIDNIGHTBLUE", fg="white")
    NomeLabel.place(x=5, y=5)
    
    NomeEntry = ttk.Entry(RightFrame, width=20)
    NomeEntry.place(x=150, y=5)
    
    EmailLabel = Label(RightFrame, text="Email:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    EmailLabel.place(x=5, y=210)
    
    EmailEntry = ttk.Entry(RightFrame, width=20)
    EmailEntry.place(x=150, y=210)
    
    def RegisterToDatabase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()
        
        if (Name == "" and Email == "" and User == "" and Pass == ""):
            messagebox.showerror(title="Register Error", message="Nao Deixe Nenhum Campo Vazio. Preencha Todos os Campos")
        else:
            DataBaser.cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES(?, ?, ?, ?)
            """, (Name, Email, User, Pass))
            DataBaser.conn.commit()
            messagebox.showinfo(title="Register Info", message="Conta Criada Com Sucesso")
    
    Register = ttk.Button(RightFrame, text="Register", width=10, command=RegisterToDatabase)
    Register.place(x=10, y=255)
    
    def BackToLogin():
        #removendo widget de cadastro
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)
        #trazendo de volta os botoes de widget
        LoginButton.place(x=90, y=210)
        RegisterButton.place(x=90, y=255)
    
    Back = ttk.Button(RightFrame, text="Back", width=10, command=BackToLogin)
    Back.place(x=200, y=255)

RegisterButton = ttk.Button(RightFrame, text="Register", width=20, command=Register)
RegisterButton.place(x=90, y=255)

jan.mainloop()
    