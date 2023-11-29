from tkinter import *

morse_dict = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....",
    "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.",
    "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
    "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----", " ": "/", ":": "---...",
    ".": ".-.-.-", "?": "..--..", "/": "-..-.","-": "-....-", "!": "-.-.--"
}

BACKGROUND_COLOR = "#E0C097"
GREEN = "#9CA777"


class TranslatorInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Morse Translator")
        
        self.window.config(bg=BACKGROUND_COLOR)

        self.canvas = Canvas(width=800, height=200, bg=BACKGROUND_COLOR, highlightthickness=0)
        morse_img = PhotoImage(file="assets/code_morse.png")
        self.canvas.create_image(400, 100, image=morse_img)
        self.canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=2)

        self.title_label = Label(
            text="Morse Code Translator", 
            fg="Black", 
            bg=BACKGROUND_COLOR, 
            font=("Helvetica", 24, "bold")
        )
        self.title_label.grid(row=1, column=0, columnspan=2, padx=20, pady=10)

        self.text_label = Label(
            text="Message", 
            fg="Black", 
            bg=BACKGROUND_COLOR, 
            font=("Helvetica", 12, "bold")
        )
        self.text_label.grid(sticky=W, row=2, column=0, padx=20, pady=2)

        self.text_label = Label(
            text="Type your message", 
            fg="Black", 
            bg=BACKGROUND_COLOR, 
            font=("Helvetica", 10)
        )
        self.text_label.grid(sticky=W, row=3, column=0, padx=20)

        self.in_text = Text(bg=GREEN, font=("Helvetica", 10), relief=SOLID, height=5, width=50)
        self.in_text.grid(row=4, column=0, padx=20)

        self.morse_label = Label(
            text="Morse Code", 
            fg="Black", 
            bg=BACKGROUND_COLOR, 
            font=("Helvetica", 12, "bold")
        )
        self.morse_label.grid(sticky=W, row=2, column=1, padx=20, pady=5)

        self.text_label = Label(
            text="'#' indicate an unstranslatable character.", 
            fg="Black", 
            bg=BACKGROUND_COLOR, 
            font=("Helvetica", 10)
        )
        self.text_label.grid(sticky=W, row=3, column=1, padx=20)

        self.out_text = Text(bg=GREEN, font=("Helvetica", 10), relief=SOLID, height=5, width=50)
        self.out_text.grid(row=4, column=1, padx=20)

        self.convert_btn = Button(
            text="Convert", 
            fg="Black",
            bg=GREEN, 
            activebackground=GREEN, 
            font=("Helvetica", 12, "bold"),
            command=self.converted_txt
        )
        self.convert_btn.grid(sticky=E, row=5, column=1, padx=120, pady=15, ipadx=8, ipady=8)

        self.clear_btn = Button(
            text="Reset", 
            fg="Black",
            bg=GREEN, 
            activebackground=GREEN, 
            font=("Helvetica", 12, "bold"),
            command=self.reset_txt
        )
        self.clear_btn.grid(sticky=E, row=5, column=1, padx=20, pady=15, ipadx=8, ipady=8)

        self.window.mainloop()
        
    def converted_txt(self):
        txt_input = self.in_text.get("1.0", "end-1c").upper()
        code = ''
        output_list = [morse_dict[letter] if letter in morse_dict else '#' for letter in txt_input]
        for letter in output_list:
            code += letter
        self.out_text.delete("1.0", END)
        self.out_text.insert(END, code)

    def reset_txt(self):
        self.in_text.delete("0.0", END)
        self.out_text.delete("0.0", END)

if __name__ == '__main__':

    code_ui = TranslatorInterface()    

      