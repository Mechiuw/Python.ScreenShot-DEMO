import pyscreenshot as ImageGrab
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

root = tk.Tk()
root.title("SSAP")
root.geometry("300x150")

# take ss function
def takeScreenShot():
    try:
        root.withdraw
        
        # ss field dimesnsions range  
        bbox = None
        screenshot = ImageGrab.grab(bbox=bbox)
        
        root.deiconify()
        
        # configure file path and format
        file_path = filedialog.asksaveasfile(defaultextension=".png",
                                            filetypes=[("PNG files","*.png"),
                                                        ("JPEG files","*.jpeg"),
                                                        ("All files","*.*")])
        
        if file_path:
            file_format = file_path.split('.')[-1].upper()
            screenshot.save(file_path, format=file_format)
            messagebox.showinfo("Screenshot saved", f"Screenshot saved to {file_path}")
        else :
            retry = messagebox.askyesnocancel("Retry", "take another screenshot?")
            if retry :
                takeScreenShot()
    except Exception as e:
        if messagebox.askretrycancel("Error",f"An error occurred: {e}\nWould you like to try again?"):
            takeScreenShot()
        

screenshot_button = tk.Button(root,text="screenshot", command=takeScreenShot)
screenshot_button.pack(expand=True)

root.mainloop()
    
