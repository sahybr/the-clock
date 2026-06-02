import tkinter as tk
from tkinter import *
import os
from time import strftime
import ctypes

def carregar_fonte_google(caminho_arquivo):
    # Essa linha diz ao Windows para registrar temporariamente a fonte para o seu app
    ctypes.windll.gdi32.AddFontResourceW(caminho_arquivo)

carregar_fonte_google("./assets/fonts/Changa_One/ChangaOne-Regular.ttf") 

light_color = "white"
dark_color = "#1d1d1d"
purple_color = "#8e27ea"

font_style = "Changa One"

root = tk.Tk()
root.title("Python Clock")
root.geometry("600x320")
root.maxsize(600, 320)
root.minsize(600, 320)
root.configure(background=light_color)

light_icon = PhotoImage(file="./assets/icons/brightness.png")
dark_icon = PhotoImage(file="./assets/icons/dark.png")

def toggle_dark_mode():
    if root["bg"] == dark_color:
        root["bg"] = light_color
        tela["bg"] = light_color
        saudacao["bg"] = light_color
        data["bg"] = light_color
        horas["bg"] = light_color
        mode_button["image"] = light_icon
        mode_button["bg"] = light_color
    else:
        root["bg"] = dark_color
        tela["bg"] = dark_color
        saudacao["bg"] = dark_color
        data["bg"] = dark_color
        horas["bg"] = dark_color
        mode_button["image"] = dark_icon
        mode_button["bg"] = dark_color

def get_saudacao():
    nome_usuario = os.getlogin()
    hora_atual = int(strftime("%H"))

    if hora_atual >=5 and hora_atual < 12:
        saudacao.config(text="Bom dia, "+nome_usuario+"!")
    elif hora_atual >=12 and hora_atual < 18:
        saudacao.config(text="Boa tarde "+nome_usuario+"!")
    else:
        saudacao.config(text="Boa noite "+nome_usuario+"!")

def get_data():
    data_atual = strftime(" %a, %d %b %Y")
    data.config(text=data_atual)

def get_horas():
    hora_atual = strftime("%H:%M:%S")
    horas.config(text=hora_atual)
    horas.after(1000, get_horas)

mode_button = Button(root, command=toggle_dark_mode)
mode_button.config(image=light_icon, bd=0, bg=light_color)
mode_button.pack(pady=10)

tela = tk.Canvas(root, width=600, height=20, bg=light_color,
                 bd=0, highlightthickness=0, relief="ridge")
tela.pack()

saudacao = Label(root, bg=light_color, fg=purple_color, font=(font_style, 16))
saudacao.pack()

data = Label(root, bg=light_color, fg=purple_color, font=(font_style, 14))
data.pack(pady=2)

horas = Label(root, bg=light_color, fg=purple_color, font=(font_style, 64, "bold"))
horas.pack(pady=2)

get_saudacao()
get_data()
get_horas()
root.mainloop()