import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class ModernApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern GUI Application")
        self.root.geometry("600x700")
        self.root.configure(bg="#f0f0f0")
        
        # Set style
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("Title.TLabel", font=("Helvetica", 24, "bold"), background="#f0f0f0")
        self.style.configure("Header.TLabel", font=("Helvetica", 14, "bold"), background="#f0f0f0")
        
        self.setup_ui()
    
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title = ttk.Label(main_frame, text="Welcome!", style="Title.TLabel")
        title.pack(pady=10)
        
        # Subtitle
        subtitle = ttk.Label(main_frame, text="Simple GUI with Tkinter", font=("Helvetica", 12), background="#f0f0f0")
        subtitle.pack(pady=5)
        
        # Separator
        separator1 = ttk.Separator(main_frame, orient="horizontal")
        separator1.pack(fill="x", pady=15)
        
        # Todo List Section
        todo_header = ttk.Label(main_frame, text="📝 Todo List", style="Header.TLabel")
        todo_header.pack(anchor="w", pady=(10, 5))
        
        # Input frame
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill="x", pady=10)
        
        self.todo_input = ttk.Entry(input_frame, width=40)
        self.todo_input.pack(side=tk.LEFT, padx=(0, 10))
        self.todo_input.bind("<Return>", lambda e: self.add_todo())
        
        add_btn = ttk.Button(input_frame, text="Add", command=self.add_todo)
        add_btn.pack(side=tk.LEFT)
        
        # Listbox frame
        list_frame = ttk.Frame(main_frame)
        list_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        scrollbar = ttk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.todo_listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set, height=8)
        self.todo_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.todo_listbox.yview)
        
        # Button frame
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill="x", pady=10)
        
        delete_btn = ttk.Button(btn_frame, text="Delete Selected", command=self.delete_todo)
        delete_btn.pack(side=tk.LEFT, padx=5)
        
        clear_btn = ttk.Button(btn_frame, text="Clear All", command=self.clear_todos)
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Separator
        separator2 = ttk.Separator(main_frame, orient="horizontal")
        separator2.pack(fill="x", pady=15)
        
        # Info Section
        info_header = ttk.Label(main_frame, text="ℹ️ Information", style="Header.TLabel")
        info_header.pack(anchor="w", pady=(10, 5))
        
        # Time display
        time_frame = ttk.Frame(main_frame)
        time_frame.pack(fill="x", pady=5)
        
        ttk.Label(time_frame, text="Current Time:", font=("Helvetica", 10), background="#f0f0f0").pack(side=tk.LEFT)
        self.time_label = ttk.Label(time_frame, text="", font=("Helvetica", 10, "bold"), background="#f0f0f0")
        self.time_label.pack(side=tk.LEFT, padx=10)
        
        # Update time
        self.update_time()
        
        # Count display
        count_frame = ttk.Frame(main_frame)
        count_frame.pack(fill="x", pady=5)
        
        ttk.Label(count_frame, text="Tasks:", font=("Helvetica", 10), background="#f0f0f0").pack(side=tk.LEFT)
        self.count_label = ttk.Label(count_frame, text="0", font=("Helvetica", 10, "bold"), background="#f0f0f0")
        self.count_label.pack(side=tk.LEFT, padx=10)
        
        # Separator
        separator3 = ttk.Separator(main_frame, orient="horizontal")
        separator3.pack(fill="x", pady=15)
        
        # Action buttons
        action_frame = ttk.Frame(main_frame)
        action_frame.pack(fill="x", pady=10)
        
        about_btn = ttk.Button(action_frame, text="About", command=self.show_about)
        about_btn.pack(side=tk.LEFT, padx=5)
        
        exit_btn = ttk.Button(action_frame, text="Exit", command=self.root.quit)
        exit_btn.pack(side=tk.LEFT, padx=5)
    
    def add_todo(self):
        task = self.todo_input.get().strip()
        if task:
            self.todo_listbox.insert(tk.END, f"✓ {task}")
            self.todo_input.delete(0, tk.END)
            self.update_count()
        else:
            messagebox.showwarning("Empty Task", "Please enter a task!")
    
    def delete_todo(self):
        try:
            index = self.todo_listbox.curselection()[0]
            self.todo_listbox.delete(index)
            self.update_count()
        except IndexError:
            messagebox.showwarning("No Selection", "Please select a task to delete!")
    
    def clear_todos(self):
        if messagebox.askyesno("Clear All", "Are you sure you want to clear all tasks?"):
            self.todo_listbox.delete(0, tk.END)
            self.update_count()
    
    def update_count(self):
        count = self.todo_listbox.size()
        self.count_label.config(text=str(count))
    
    def update_time(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        self.time_label.config(text=current_time)
        self.root.after(1000, self.update_time)
    
    def show_about(self):
        messagebox.showinfo("About", "Modern Tkinter Application\nVersion 1.0\nA simple GUI with todo list")

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernApp(root)
    root.mainloop()