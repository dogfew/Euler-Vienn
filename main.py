from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from Euler_Vienn import *

# create root
root = Tk()
root.title('Euler-Vienn')
root.geometry('900x680')
root.config(bg='#FFFFFF')

# create notebook
notebook = ttk.Notebook(root)
notebook.pack(expand=True)

# create frame
frame = ttk.Frame(notebook)
frame.pack(fill='both', expand=True)
notebook.add(frame, text='Base')
# create hint frame
hint_frame = ttk.Frame(notebook)
hint_frame.pack(fill='both', expand=True)
notebook.add(hint_frame, text='Hint')

# Create styles
style = ttk.Style()
style.configure("TButton", font=("Noto Sans", 12), borderwidth=1)
style.configure("TLabel", font=("Noto Sans", 12), borderwidth=0)
style.configure("TEntry", borderwidth=0)
style.map("TButton", foreground=[("active", "disabled", "green")],
          background=[("active", "#75a86d")])


def callback(event):
    """Чтобы Ctrl+A выделяло весь текст"""
    event.widget.select_range(0, 'end')
    event.widget.icursor('end')


def safe_eval(string):
    allowed = 'abcABC^&|-+)( '
    res = ''
    for i in string:
        res += i.replace('+', '|').upper() if i in allowed else ''
    return eval(res)


def show_func(url='user_img.png'):
    w = operation.get()
    try:
        euler(safe_eval(w), t=w)
    except Exception:
        url = 'default.png'
    image = Image.open(url)
    img = ImageTk.PhotoImage(image)
    disp_img.config(image=img)
    disp_img.image = img


# Main Label
ttk.Label(
    frame,
    text='  Введите операцию  \n  с множествами:  ',
    relief='flat'
).pack(side=LEFT, ipadx=10)

# Hint Label
ttk.Label(
    hint_frame,
    text=
    ''' & пересечение               | объединение
 - разность                         ^ симметрическая разность''',
    relief='flat'
).pack(side=LEFT, ipadx=10)

# Entry
operation = ttk.Entry(frame,
                      width=20,
                      font=("Sans", 12),
                      justify='center')
operation.insert(END, 'A ^ B')
operation.bind('<Control-KeyRelease-a>', callback)
operation.pack(side=LEFT)

# Button
ttk.Button(
    frame,
    text='Оперировать',
    command=show_func,
).pack(side=LEFT, padx=10, ipadx=10)

disp_img = Label()
disp_img.pack()
show_func('default.png')
root.bind('<Return>', lambda event: show_func())

root.mainloop()
