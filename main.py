import tkinter as tk
import random
from tkinter import messagebox
from random import randint
from pygame import mixer

def quit():
    window.destroy()

def generate():
    code = ''
    for i in range(4):
        number = randint(0,9)
        alphabet = [chr(i).upper() for i in range(97, 123)]
        letters = [alphabet[randint(0, len(alphabet) - 1)] for i in range(3)]
        letters.insert(randint(0,4), str(number))
        code += (''.join(letters))
        code += '-'
    word_label.config(text = code[0:-1])

def on_off_music():
    global MUSIC
    if MUSIC == 1:
        mixer.music.stop()
        MUSIC = 0
    else:
        mixer.music.play()
        MUSIC = 1

MUSIC = 0

window = tk.Tk()
window.title('My app')
window.geometry('300x300')
window.resizable(0, 0)
bg_img = tk.PhotoImage(file=r'C:\Users\Mi\Documents\ITMO\Python\lab_3\tanki_online.png')
mixer.init()
mixer.music.load(r'C:\Users\Mi\Documents\ITMO\Python\lab_3\music_8_bit.mp3')


bg_label = tk.Label(window, image=bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

word_label = tk.Label(window, 
                      text="XXXX-XXXX-XXXX-XXXX",
                      font=('Cansolas', 15),
                      bg='red',
                      fg='white')
word_label.place(x=0, y=0, relwidth=1)


btn_guess = tk.Button(window, 
                      text="Сгенерировать ключ",
                      width=17,
                      command=generate)
btn_guess.place(relx=0.08, rely=0.55)

btn_exit = tk.Button(window, 
                      text="Cancel",
                      width=15,
                      command=quit)
btn_exit.place(relx=0.55, rely=0.55)

btn_guess = tk.Button(window, 
                      text="Вкл/выкл музыку",
                      width=17,
                      command=on_off_music)
btn_guess.place(relx=0.3, rely=0.9)


window.mainloop()
