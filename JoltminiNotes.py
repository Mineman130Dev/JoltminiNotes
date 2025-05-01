import customtkinter as CTk
import os

window = CTk.CTk()
window.title("JoltminiNotes")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_width = 200
window_height = 200

x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)

window.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")

window.attributes('-topmost', True)

texbox = CTk.CTkTextbox(window, width=200, height=200)
texbox.pack(fill="both", expand=True)


window.mainloop()
