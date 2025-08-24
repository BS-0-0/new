import tkinter as tk
import webbrowser

# Dictionary of shortcuts
shortcuts = {
    'YouTube': "https://www.youtube.com",
    'Spotify': "https://www.spotify.com",
    'CDKeys': "https://www.cdkeys.com",
    'College': "https://btc.eassessorpro.co.uk",
    'MovieBoxPro': "https://www.movieboxpro.app"
}

# Function to open a website
def open_website(url):
    webbrowser.open(url)

# Create main window
root = tk.Tk()
root.title("Quick Launcher")
root.geometry("370x450")  # Width x Height
root.configure(bg="#1E1E1E")  # Set background color
root.resizable(False, False)
# Create buttons for each shortcut

button_bg = "#3A3A3A"  # Button background  color
button_fg = "#FFFFFF"  # Button text color
button_font = ("Segoe", 14)  # Button font

title = tk.Label(root, text="🚀Quick Launcher" , font=(" Segoe", 14, "bold"),
                     bg="#1E1E1E", fg="#FFFFFF")
title.pack(pady=10) 

rocket_frame = tk.Frame (root, bg="#1E1E1E")
rocket_frame.pack(side="right", fill="y" , padx=10)

rocket_art = """

        *
       / \ 
      / _ \ 
     |.o '.|
     |'._.'|
     |     |
     | ./  |   |
     |     |
     |  |  |
   ,'|  |  |`.
  /  |  |  |  \ 
  |,-'--|--'-.| 420
"""
rocket_label = tk.Label(rocket_frame, text=rocket_art, font=("Courier", 12),  justify= 'left' , bg="#1E1E1E", fg="#FFFFFF")
rocket_label.pack(pady=10)



for name, url in shortcuts.items():
    button = tk.Button(
        root,
        text=name,
        font=("Segoe", 14),
        width=20,
        height=2,
        command=lambda url=url: open_website(url)
    )
    button.pack(pady=5)


# Run the GUI loop
root.mainloop()