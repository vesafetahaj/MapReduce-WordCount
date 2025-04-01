import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog, messagebox
from src.mapper import WordCountMapper
from src.reducer import WordCountReducer


class WordCountApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MapReduce Word Count Tool")
        self.root.geometry("700x600")

        self.file_path = None

        # Title Label
        ttk.Label(root, text="MapReduce Word Count", font=("Helvetica", 20, "bold")).pack(pady=20)

        # Upload File Button
        ttk.Button(root, text="Upload Text File", bootstyle="info-outline", command=self.upload_file).pack(pady=10)

        # Run Button
        self.run_btn = ttk.Button(root, text="Run Word Count", bootstyle="success", command=self.run_word_count, state=DISABLED)
        self.run_btn.pack(pady=10)

        # Output Box
        self.output_box = ttk.ScrolledText(root, width=80, height=25, font=("Consolas", 11))
        self.output_box.pack(padx=10, pady=20)

    def upload_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if self.file_path:
            self.run_btn.config(state=NORMAL)
            messagebox.showinfo("File Loaded", f"File loaded: {self.file_path}")

    def run_word_count(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            mapper = WordCountMapper()
            reducer = WordCountReducer()
            mapped = [pair for line in lines for pair in mapper.map(line)]
            grouped = reducer.shuffle_and_sort(mapped)
            reduced = reducer.reduce(grouped)

            # Display Results
            self.output_box.delete("1.0", "end")
            self.output_box.insert("end", f"{'WORD':<20}{'FREQUENCY'}\n")
            self.output_box.insert("end", "-"*30 + "\n")
            for word in sorted(reduced):
                self.output_box.insert("end", f"{word:<20}{reduced[word]}\n")

        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    app = ttk.Window(themename="cyborg")  # You can also try: flatly, journal, lumen, morph, minty
    WordCountApp(app)
    app.mainloop()
