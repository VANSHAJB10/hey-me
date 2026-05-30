import tkinter as tk
import itertools

greetings = [
    "Hey Vanshaj",                    # English
    "नमस्ते वंशज",                     # Hindi
    "ਸਤ ਸ੍ਰੀ ਅਕਾਲ ਵੰਸ਼ਜ",             # Punjabi
    "હાય વંશજ",                       # Gujarati
    "হ্যালো বংশজ",                    # Bengali
    "హాయ్ వంశజ్",                     # Telugu
    "வணக்கம் வன்ஷாஜ்",                # Tamil
    "ഹായ് വൻഷാജ്",                    # Malayalam
    "ಹಾಯ್ ವಂಶಜ್",                     # Kannada
    "नमस्कार वंशज",                   # Marathi
    "Hello Vanshaj",                  # English Variant
    "Hola Vanshaj",                   # Spanish
    "Bonjour Vanshaj",                # French
    "Hallo Vanshaj",                  # German
    "Ciao Vanshaj",                   # Italian
    "Olá Vanshaj",                    # Portuguese
    "Привет Ваншадж",                 # Russian
    "你好 Vanshaj",                    # Chinese
    "こんにちは ヴァンシャジ",         # Japanese
    "안녕 반샤즈",                     # Korean
    "Merhaba Vanshaj",                # Turkish
    "Γεια σου Vanshaj",               # Greek
    "Hej Vanshaj",                    # Swedish
    "Hei Vanshaj",                    # Norwegian
    "Hej Vanshaj",                    # Danish
    "Moi Vanshaj",                    # Finnish
    "Cześć Vanshaj",                  # Polish
    "Ahoj Vanshaj",                   # Czech
    "Szia Vanshaj",                   # Hungarian
    "Salut Vanshaj",                  # Romanian
    "Здраво Vanshaj",                 # Serbian
    "Привіт Vanshaj",                 # Ukrainian
    "Halo Vanshaj",                   # Indonesian
    "Kamusta Vanshaj",                # Filipino
    "Xin chào Vanshaj",               # Vietnamese
    "Sawubona Vanshaj",               # Zulu
    "Jambo Vanshaj",                  # Swahili
    "Salam Vanshaj",                  # Persian
    "مرحبا فانشاج",                   # Arabic
    "שלום ואנשאג",                    # Hebrew
    "Habari Vanshaj",                 # Swahili Variant
    "Mingalaba Vanshaj",              # Burmese
    "Sabaidee Vanshaj",               # Lao
    "Suostei Vanshaj",                # Khmer
    "Selamat Vanshaj",                # Malay
    "Yassas Vanshaj",                 # Greek Variant
    "Tere Vanshaj",                   # Estonian
    "Sveiki Vanshaj",                 # Latvian
    "Labas Vanshaj",                  # Lithuanian
    "Buna Vanshaj",                   # Azerbaijani
    "Salom Vanshaj",                  # Uzbek
    "Салам Vanshaj",                  # Kyrgyz
    "Сайн уу Vanshaj",                # Mongolian
    "Aloha Vanshaj",                  # Hawaiian
    "Kia Ora Vanshaj",                # Maori
    "Dia dhuit Vanshaj",              # Irish
    "Shwmae Vanshaj",                 # Welsh
    "Halló Vanshaj",                  # Icelandic
    "Moien Vanshaj",                  # Luxembourgish
    "Hejsan Vanshaj"                  # Swedish Variant
]

colors = [
    "#ff0055", "#00d4ff", "#ffd700", "#7fff00",
    "#ff4500", "#ff00ff", "#00ff7f", "#1e90ff"
]

root = tk.Tk()
root.title("Hey Vanshaj")
root.configure(bg="black")
root.attributes("-fullscreen", True)

label = tk.Label(
    root,
    text="",
    font=("Arial", 60, "bold"),
    fg="white",
    bg="black"
)
label.pack(expand=True)

greeting_cycle = itertools.cycle(greetings)
color_cycle = itertools.cycle(colors)

def animate():
    label.config(
        text=next(greeting_cycle),
        fg=next(color_cycle)
    )
    root.after(80, animate)  # 80ms transition

animate()

root.bind("<Escape>", lambda e: root.destroy())

root.mainloop()
