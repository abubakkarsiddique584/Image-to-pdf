from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image
import tkinter.font as font

def upload_image():
    global img_path
    img_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )
    if img_path:
        messagebox.showinfo("Image Selected", f"Image loaded: {img_path}")

def convert_to_pdf():
    if not img_path:
        messagebox.showerror("Error", "No image selected.")
        return

    pdf_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
    if pdf_path:
        try:
            image = Image.open(img_path)
            if image.mode in ("RGBA", "P"):
                image = image.convert("RGB")
            image.save(pdf_path, "PDF", resolution=100.0)
            messagebox.showinfo("Success", f"Image converted to PDF: {pdf_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to convert image to PDF: {str(e)}")

# Initialize the main window
window = Tk()
window.title("Image to PDF Converter")
window.geometry("400x300")
window.config(bg="#F0F0F0")

# Define font
title_font = font.Font(family='Helvetica', size=18, weight='bold')
button_font = font.Font(family='Helvetica', size=12)

# Title label
title_label = Label(window, text="Image to PDF Converter", bg="#F0F0F0", fg="#333333", font=title_font)
title_label.pack(pady=20)

# Upload button
upload_button = Button(window, text="Upload Image", command=upload_image, font=button_font, bg="#4CAF50", fg="white", padx=10, pady=5)
upload_button.pack(pady=10)

# Convert button
convert_button = Button(window, text="Convert to PDF", command=convert_to_pdf, font=button_font, bg="#2196F3", fg="white", padx=10, pady=5)
convert_button.pack(pady=10)

# Run the main loop
window.mainloop()
