import pyscreenshot as ImageGrab
import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk
root.title("SSAP")
root.geometry("300x150")

# take ss function
def takeScreenShot():
    root.withdraw
    screenshot = ImageGrab.grab()
    
    root.deiconify()
    
    # configure file path and format
    file_path = filedialog.asksaveasfile(defaultextension=".png",
                                         filetypes=[("PNG files","*.png"),("All files","*.*")])
    
    if file_path:
        screenshot.save(file_path)
        messagebox.showinfo("Screenshot saved", f"Screenshot saved to {file_path}")
        

screenshot_button = tk.Button(root,text="take ss", command=takeScreenShot)
screenshot_button.pack(expand=True)

root.mainloop()
    
