# BLOCK Requirements #
#   customtkinter
# ENDBLOCK Requirements #

import tkinter as tk
import customtkinter as ctk

class GradientFrame(tk.Canvas):
    """
        A gradient frame which uses a canvas to draw the background
    """

    def __init__(self, parent, color1="red", color2="black", **kwargs):
        super().__init__(master=parent, **kwargs)
        self._color1 = color1
        self._color2 = color2
        self.bind("<Configure>", self._draw_gradient)

    def _draw_gradient(self, event=None):
        """
            Draw the gradient
        """

        self.update_idletasks()
        self.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()
        limit = width
        (r1,g1,b1) = self.winfo_rgb(self._color1)
        (r2,g2,b2) = self.winfo_rgb(self._color2)
        r_ratio = float(r2-r1) / limit
        g_ratio = float(g2-g1) / limit
        b_ratio = float(b2-b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = "#%4.4x%4.4x%4.4x" % (nr,ng,nb)
            self.create_line(i,0,i,height, tags=("gradient",), fill=color)
        self.lower("gradient")



class App(ctk.CTk):
    def __init__(self):
        """
            Load all the application
        """
        super().__init__(fg_color="#ffffff")

        self.center_window(win=self, wth=600, hht=500)

        main: tk.Canvas = GradientFrame(parent=self, color1="#0004ff", color2="#ff7300")
        main.pack(fill="both", expand=True)
    
    def center_window(self, win: ctk.CTk | ctk.CTkToplevel,
        wth: int, hht: int):
        """
            Center the window horizontally and vertically
        """

        self.update_idletasks()

        scrn_w: int = self.winfo_screenwidth()
        scrn_h: int = self.winfo_screenheight()

        ww: int = win.winfo_width()
        wh: int = win.winfo_height()

        x: int = (scrn_w // 3) - (ww // 2)
        y: int = (scrn_h // 3) - (wh // 2)

        win.geometry(f"{wth}x{hht}+{x}+{y}")

if __name__ == "__main__":
    app: App = App()
    app.mainloop()