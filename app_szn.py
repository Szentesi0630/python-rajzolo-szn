import tkinter as tk
from gui_module import create_main_window, create_canvas, create_clear_button
from utils_module import save_canvas_image, generate_filename

def szn_save_drawing(canvas):
    filename = generate_filename()
    save_canvas_image(canvas, filename)
    print(f"Rajz mentve: {filename}.ps")

class DrawAppSzN:
    def __init__(self):
        self.root = create_main_window()
        self.last_x, self.last_y = None, None

        self.canvas = create_canvas(self.root, self.draw)
        create_clear_button(self.root, self.clear_canvas)

        save_btn = tk.Button(self.root, text="Rajz mentése", command=lambda: szn_save_drawing(self.canvas))
        save_btn.pack(pady=5)

    def draw(self, event):
        x, y = event.x, event.y
        if self.last_x and self.last_y:
            self.canvas.create_line(self.last_x, self.last_y, x, y, fill="black", width=3)
        self.last_x, self.last_y = x, y

    def clear_canvas(self):
        self.canvas.delete("all")
        self.last_x, self.last_y = None, None

    def run(self):
        self.root.mainloop()
