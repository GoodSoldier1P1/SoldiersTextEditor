import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

import sv_ttk


def textEditor():
    def openFile():
        filepath = askopenfilename(
            filetypes=[('Text Files', '*.text'), ('All Files', '*.*')]
        )

        if not filepath:
            return
        
        txt_edit.delete(1.0, tk.END)
        with open(filepath, 'r') as input_file:
            text = input_file.read()
            txt_edit.insert(tk.END, text)
        window.title(f"SoldiersTextEditor - {filepath}")
    
    def saveFile():
        filepath = asksaveasfilename(
            defaultextension='txt',
            filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')],
        )

        if not filepath:
            return
        
        with open(filepath, 'w') as output_file:
            text = txt_edit.get(1.0, tk.END)
            output_file.write(text)
        window.title(f"Soldier's Text Editor - {filepath}")
    
    window = tk.Tk()
    window.title('Soldier\'s Text Editor')
    window.rowconfigure(0, minsize=800, weight=1)
    window.columnconfigure(1, minsize=800, weight=1)

    menubar = tk.Menu(window)

    fileMenu = tk.Menu(menubar, tearoff=0)
    fileMenu.add_command(label='Open', command=openFile)
    fileMenu.add_command(label='Save As...', command=saveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label='Exit', command=window.quit)
    menubar.add_cascade(label='File', menu=fileMenu)

    editMenu = tk.Menu(menubar, tearoff=0)
    editMenu.add_command(label='Undo')
    editMenu.add_command(label='Redo')
    menubar.add_cascade(label='Edit', menu=editMenu)

    viewMenu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='View', menu=viewMenu)

    window.config(menu=menubar)

    txt_edit = tk.Text(window, undo=True, autoseparators=True)
    scrollbar = tk.Scrollbar(window, command=txt_edit.yview)
    txt_edit.config(yscrollcommand=scrollbar.set)
    scrollbar.grid(row=0, column=2, sticky='ns')

    txt_edit.grid(row=0, column=1, sticky='nsew')

    sv_ttk.set_theme("dark")

    # KEYBINDS
    
    window.bind("<Control-s>", saveFile) # save file

    # END KEYBINDS

    window.mainloop()


if __name__ == '__main__':
    textEditor()