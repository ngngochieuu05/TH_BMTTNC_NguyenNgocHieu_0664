import customtkinter as ctk
from Caesar import encrypt as caesar_encrypt, decrypt as caesar_decrypt
from Vigenere import encrypt as vigenere_encrypt, decrypt as vigenere_decrypt

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class CipherApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Mã Hóa Cùng Hiếu Biển")
        self.geometry("800x700")
        
        # Main frame
        main_frame = ctk.CTkFrame(self, corner_radius=10)
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Title
        title_label = ctk.CTkLabel(
            main_frame,
            text="Cipher Encryption & Decryption",
            font=("Arial", 24, "bold")
        )
        title_label.pack(pady=15)
        
        # Cipher type selection
        cipher_frame = ctk.CTkFrame(main_frame, corner_radius=8)
        cipher_frame.pack(pady=10, padx=10, fill="x")
        
        cipher_label = ctk.CTkLabel(
            cipher_frame,
            text="Select Cipher Type:",
            font=("Arial", 14, "bold")
        )
        cipher_label.pack(side="left", padx=10, pady=10)
        
        self.cipher_var = ctk.StringVar(value="caesar")
        
        caesar_radio = ctk.CTkRadioButton(
            cipher_frame,
            text="Caesar",
            variable=self.cipher_var,
            value="caesar",
            command=self.update_key_label
        )
        caesar_radio.pack(side="left", padx=5)
        
        vigenere_radio = ctk.CTkRadioButton(
            cipher_frame,
            text="Vigenere",
            variable=self.cipher_var,
            value="vigenere",
            command=self.update_key_label
        )
        vigenere_radio.pack(side="left", padx=5)
        
        # Input section
        input_frame = ctk.CTkFrame(main_frame, corner_radius=8)
        input_frame.pack(pady=10, padx=10, fill="x")
        
        input_label = ctk.CTkLabel(
            input_frame,
            text="Input Text:",
            font=("Arial", 12, "bold")
        )
        input_label.pack(anchor="w", padx=10, pady=(10, 5))
        
        self.input_text = ctk.CTkTextbox(input_frame, height=100)
        self.input_text.pack(padx=10, pady=(0, 10), fill="both", expand=True)
        
        # Key section
        key_frame = ctk.CTkFrame(main_frame, corner_radius=8)
        key_frame.pack(pady=10, padx=10, fill="x")
        
        self.key_label = ctk.CTkLabel(
            key_frame,
            text="Shift Key (Number):",
            font=("Arial", 12, "bold")
        )
        self.key_label.pack(anchor="w", padx=10, pady=(10, 5))
        
        self.key_entry = ctk.CTkEntry(
            key_frame,
            placeholder_text="Enter shift value (0-25) or keyword",
            height=40
        )
        self.key_entry.pack(padx=10, pady=(0, 10), fill="x")
        
        # Buttons frame
        button_frame = ctk.CTkFrame(main_frame, corner_radius=8)
        button_frame.pack(pady=10, padx=10, fill="x")
        
        encrypt_button = ctk.CTkButton(
            button_frame,
            text="Encrypt",
            command=self.encrypt_text,
            height=40,
            font=("Arial", 12, "bold")
        )
        encrypt_button.pack(side="left", padx=5, pady=10, expand=True, fill="x")
        
        decrypt_button = ctk.CTkButton(
            button_frame,
            text="Decrypt",
            command=self.decrypt_text,
            height=40,
            font=("Arial", 12, "bold")
        )
        decrypt_button.pack(side="left", padx=5, pady=10, expand=True, fill="x")
        
        clear_button = ctk.CTkButton(
            button_frame,
            text="Clear",
            command=self.clear_all,
            height=40,
            font=("Arial", 12, "bold"),
            fg_color="gray"
        )
        clear_button.pack(side="left", padx=5, pady=10, expand=True, fill="x")
        
        # Output section
        output_frame = ctk.CTkFrame(main_frame, corner_radius=8)
        output_frame.pack(pady=10, padx=10, fill="both", expand=True)
        
        output_label = ctk.CTkLabel(
            output_frame,
            text="Output:",
            font=("Arial", 12, "bold")
        )
        output_label.pack(anchor="w", padx=10, pady=(10, 5))
        
        self.output_text = ctk.CTkTextbox(output_frame, state="disabled")
        self.output_text.pack(padx=10, pady=(0, 10), fill="both", expand=True)
        
        # Status bar
        self.status_label = ctk.CTkLabel(
            main_frame,
            text="Ready",
            font=("Arial", 10),
            text_color="gray"
        )
        self.status_label.pack(pady=5)
    
    def update_key_label(self):
        cipher_type = self.cipher_var.get()
        if cipher_type == "caesar":
            self.key_label.configure(text="Shift Key (Number 0-25):")
            self.key_entry.configure(placeholder_text="Enter shift value (0-25)")
        else:
            self.key_label.configure(text="Keyword:")
            self.key_entry.configure(placeholder_text="Enter keyword")
    
    def encrypt_text(self):
        try:
            input_text = self.input_text.get("1.0", "end-1c")
            key_str = self.key_entry.get()
            cipher_type = self.cipher_var.get()
            
            if not input_text:
                self.show_output("Error: Please enter text to encrypt")
                return
            
            if not key_str:
                self.show_output("Error: Please enter a key")
                return
            
            if cipher_type == "caesar":
                try:
                    key = int(key_str)
                    if key < 0 or key > 25:
                        self.show_output("Error: Shift key must be between 0 and 25")
                        return
                    result = caesar_encrypt(input_text, key)
                    self.show_output(result)
                except ValueError:
                    self.show_output("Error: Shift key must be a number")
            else:
                result = vigenere_encrypt(input_text, key_str)
                self.show_output(result)
            
            self.status_label.configure(text=f"✓ Encrypted using {cipher_type.upper()}")
            
        except Exception as e:
            self.show_output(f"Error: {str(e)}")
    
    def decrypt_text(self):
        try:
            input_text = self.input_text.get("1.0", "end-1c")
            key_str = self.key_entry.get()
            cipher_type = self.cipher_var.get()
            
            if not input_text:
                self.show_output("Error: Please enter text to decrypt")
                return
            
            if not key_str:
                self.show_output("Error: Please enter a key")
                return
            
            if cipher_type == "caesar":
                try:
                    key = int(key_str)
                    if key < 0 or key > 25:
                        self.show_output("Error: Shift key must be between 0 and 25")
                        return
                    result = caesar_decrypt(input_text, key)
                    self.show_output(result)
                except ValueError:
                    self.show_output("Error: Shift key must be a number")
            else:
                result = vigenere_decrypt(input_text, key_str)
                self.show_output(result)
            
            self.status_label.configure(text=f"✓ Decrypted using {cipher_type.upper()}")
            
        except Exception as e:
            self.show_output(f"Error: {str(e)}")
    
    def show_output(self, message):
        self.output_text.configure(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", message)
        self.output_text.configure(state="disabled")
    
    def clear_all(self):
        self.input_text.delete("1.0", "end")
        self.output_text.configure(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.configure(state="disabled")
        self.key_entry.delete(0, "end")
        self.status_label.configure(text="Cleared")


if __name__ == "__main__":
    app = CipherApp()
    app.mainloop()
