import customtkinter as CTk
import os
from appdirs import user_data_dir
import tkinter.font as tkFont
import tkinter as tk

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

textbox = CTk.CTkTextbox(window, wrap='word', fg_color='#171717')
textbox.pack(fill='both', expand=True)

textbox.insert("0.0", "Hello")
text = textbox.get("0.0", "end")
textbox.delete("0.0", "end") 

app_name = "JoltminiNotes"
app_author = "Mineman130"
data_dir = user_data_dir(app_name, app_author)
os.makedirs(data_dir, exist_ok=True)
filepath = os.path.join(data_dir, "notes.txt")

save_timer = None
debounce_delay = 1000  # milliseconds

def save_note_debounced(event=None):
    global save_timer
    if save_timer:
        window.after_cancel(save_timer)
    save_timer = window.after(debounce_delay, save_note)

def save_note():
    text_to_save = textbox.get("0.0", "end")
    try:
        with open(filepath, 'w') as file:
            file.write(text_to_save)
        print(f"Notes saved to: {filepath}")
    except Exception as e:
        print(f"Error saving note: {e}")

def load_note():
    try:
        with open(filepath, "r") as file:
            loaded_text = file.read()
            textbox.delete('0.0', 'end')
            textbox.insert('0.0', loaded_text)
        print(f'Note Loaded from: {filepath}')
    except FileNotFoundError:
        print('No Files Found.')
    except Exception as e:
        print(f'Error Loading Note: {e}')

def delete_line(event=None):
    try:
        current_position = textbox.index(tk.INSERT)
        current_line = current_position.split('.')[0]
        line_start = f"{current_line}.0"
        if textbox.compare(f"{current_line}.end", "<", "end"):
            line_end = f"{str(int(current_line)+1)}.0"
        else:
            line_end = f"{current_line}.end"
        textbox.delete(line_start, line_end)
        print("Line Deleted")
    except Exception as e:
        print(f"Error deleting line: {e}")

textbox.bind("<KeyRelease>", save_note_debounced)

load_note()

window.mainloop()