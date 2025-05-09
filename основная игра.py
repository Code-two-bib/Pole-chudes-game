import random
import filtr
from tkinter import*

letters = []
word, a = str(), ''
title, n = 0, 0
txt = 'Areal 20'
flag = 1

def oper():
    global flag, letters, word, a, title, n
    if flag == 0:
        bt['text'] = 'Проверить'
        game()
    else:
        letters = []
        word, a = str(), ''
        title,  n = 0, 0
        start()
        bt['text'] = 'Нажми ещё раз'
    print(flag)

def game():
    global word,  n, title, flag
    if n > 0:
        letter = en.get
        if letter in letters:
            lb_a['text'] = "Эта буква уже была"
        else:
            lb_a['text'] = a
            letters.append(letter)
            if letter in word:
                for i in range(len(word)):
                    if word[i] == letter:
                        title = title[:i] + letter + title[i+1:]
            lb_t['text'] =  title
            if title == word:
                lb_a['text'] = "Вы угадали слово!"
                n = 0
                bt['text'] = "Продолжить играть"
                flag = 1
            n -= 1
            if n == 0:
                lb_a["text"] = 'Вы проиграли'
                lb_t['text'] = word
                bt['text'] = "Продолжить играть"
                flag = 1
    en.delete(0, END)

def start():
    global n, title, word, a, flag
    flag = 0
    words = filtr.filt()
    word = words[random.randint(0, len(words) - 1)]
    a = 'Угадайте слово из ' + str(len(word)) + ' букв'
    y, n = u'\u2733', len(word)*2
    title = y * len(word)
    print(word)

start()
root = Tk()
root.geometry("500x200")
lb_a = Label(root, text=a, font=txt)
lb_a.pack()
lb_t = Label(root, text=title, font=txt)
lb_t.pack()
en = Entry(root, width=1, font=txt)
en.pack()
bt = Button(root, text='Проверить', font=txt, command=oper)
bt.pack()
