import tkinter as tk

def create_main_window():
    root = tk.Tk()
    root.title("Rajzolóprogram (SzN)")
    root.geometry("600x500")
    return root

def create_canvas(root, draw_callback):
    canvas = tk.Canvas(root, bg="white", width=580, height=400)
    canvas.pack(pady=10)
    canvas.bind("<B1-Motion>", draw_callback)
    return canvas

def create_clear_button(root, callback):
    btn = tk.Button(root, text="Törlés", command=callback)
    btn.pack(pady=5)
