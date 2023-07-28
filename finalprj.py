"""
Creator: Jacob Ray
Date: 7/27/2023
Description:
This application allows the user to add songs to a list that they might want
to listen to later. The user can also remove the songs. The user
has the ability to add songs with description to a future database.
"""
import tkinter as tk
from tkinter import ttk
from tkinter import *



class Window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('450x400')
        self.title('Add A Song')



        # allows user to enter song info for library
        song_info_frame = tk.LabelFrame(self, text="Add Song")
        song_info_frame.grid(row=0, column=0, padx=20, pady=10)

        song_name_label = tk.Label(song_info_frame, text="Song Name")
        song_name_label.grid(row=0, column=0)
        artist_name_label = tk.Label(song_info_frame, text="Artist Name")
        artist_name_label.grid(row=0, column=1)

        song_name_entry = tk.Entry(song_info_frame)
        artist_name_entry = tk.Entry(song_info_frame)
        song_name_entry.grid(row=1, column=0)
        artist_name_entry.grid(row=1, column=1)

        title_label = tk.Label(song_info_frame, text="Genre")
        title_combobox = ttk.Combobox(song_info_frame,
                                      values=["", "Rock.", "Country", "Pop", "Indie", "Rap", "Instrumental"])
        title_label.grid(row=0, column=2)
        title_combobox.grid(row=1, column=2)

        rating_label = tk.Label(song_info_frame, text="Rating")
        rating_spinbox = tk.Spinbox(song_info_frame, from_=1, to=10)
        rating_label.grid(row=2, column=0)
        rating_spinbox.grid(row=3, column=0)

        exit_button = tk.Button(self, text="Exit", command=self.destroy)
        exit_button.grid(row=2, column=3)
        exit_button.pack(pady=20)
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('800x800')
        self.title('Tier Tunes')
        # place a button on the root window
        ttk.Button(self,
                   text='Add to Song Library',
                   command=self.open_window).pack(expand=True)
        # Listbox
        my_listbox = Listbox(self)
        my_listbox.pack(pady=15)



        label1 = tk.Label(self, text="Songs To Listen To")
        label1.place(relx = .5, rely = .5, anchor= 'center')
        self.configure(background='gray')
        # Delete items
        def delete():
            my_listbox.delete(ANCHOR)
        def insertSong():
            if len(entry.get()) != 0:
                my_listbox.insert(END, entry.get())
# allows user to delete songs added to listening list
        delete_button = Button(self, text="Remove Song", command=delete)
        delete_button.pack(pady=10)

        entry = Entry(self)
        entry.pack()
# allows user to add song to list
        button = Button(self,text= "Add a Song to Listen To", command=insertSong)
        button.pack()
# allows user to close application
        exit_button = Button(self, text="Exit Application", command=self.destroy)
        exit_button.pack(pady=20)

    def open_window(self):
        window = Window(self)
        window.grab_set()

# starts the application
if __name__ == "__main__":
    app = App()
    app.mainloop()
