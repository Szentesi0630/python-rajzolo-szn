from datetime import datetime

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def save_canvas_image(canvas, filename):
    canvas.postscript(file=filename + ".ps", colormode='color')
    return filename + ".ps"

def generate_filename(prefix="rajz_szn"):
    return f"{prefix}_{get_timestamp()}"
