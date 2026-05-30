from flask import Flask

app = Flask(__name__)

greetings = [
    "Hey Vanshaj",
    "नमस्ते वंशज",
    "ਸਤ ਸ੍ਰੀ ਅਕਾਲ ਵੰਸ਼ਜ",
    "હાય વંશજ",
    "হ্যালো বংশজ",
    "హాయ్ వంశజ్",
    "வணக்கம் வன்ஷாஜ்",
    "ഹായ് വൻഷാജ്",
    "ಹಾಯ್ ವಂಶಜ್",
    "नमस्कार वंशज",
    "Hello Vanshaj",
    "Hola Vanshaj",
    "Bonjour Vanshaj",
    "Hallo Vanshaj",
    "Ciao Vanshaj",
    "Olá Vanshaj",
    "Привет Ваншадж",
    "你好 Vanshaj",
    "こんにちは ヴァンシャジ",
    "안녕 반샤즈",
    "Merhaba Vanshaj",
    "Γεια σου Vanshaj",
    "Hej Vanshaj",
    "Hei Vanshaj",
    "Kamusta Vanshaj",
    "Xin chào Vanshaj",
    "Jambo Vanshaj",
    "مرحبا فانشاج",
    "שלום ואנשאג",
    "Aloha Vanshaj",
    "Kia Ora Vanshaj"
]

@app.route("/")
def home():
    greetings_js = str(greetings)

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hey Vanshaj</title>
        <style>
            body {{
                margin: 0;
                background: black;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                overflow: hidden;
                font-family: Arial, sans-serif;
            }}

            #greeting {{
                font-size: 4rem;
                font-weight: bold;
                text-align: center;
                transition: all 0.08s linear;
            }}
        </style>
    </head>
    <body>
        <div id="greeting"></div>

        <script>
            const greetings = {greetings_js};

            const colors = [
                "#ff0055",
                "#00d4ff",
                "#ffd700",
                "#7fff00",
                "#ff4500",
                "#ff00ff",
                "#00ff7f",
                "#1e90ff"
            ];

            let i = 0;
            let j = 0;

            const greetingDiv = document.getElementById("greeting");

            function animate() {{
                greetingDiv.innerText = greetings[i];
                greetingDiv.style.color = colors[j];

                i = (i + 1) % greetings.length;
                j = (j + 1) % colors.length;
            }}

            setInterval(animate, 80);
            animate();
        </script>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
