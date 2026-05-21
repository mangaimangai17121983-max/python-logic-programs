from flask import Flask, request

app = Flask(__name__)

# ---------------- LOGIN PAGE ----------------

@app.route("/", methods=["GET", "POST"])
def login():

    message = ""

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "1234":

            # QUIZ PAGE AFTER LOGIN
            return """
            <html>

            <head>

                <title>Quiz Page</title>

                <style>

                    body{
                        font-family: Arial;
                        background: linear-gradient(to right, #ff9966, #ff5e62);
                        color: white;
                        text-align: center;
                        padding: 30px;
                    }

                    .quiz-box{
                        background: white;
                        color: black;
                        width: 500px;
                        margin: auto;
                        padding: 30px;
                        border-radius: 15px;
                        box-shadow: 0px 0px 15px gray;
                    }

                    h1{
                        color: #ff5e62;
                    }

                    .question{
                        text-align: left;
                        margin-top: 20px;
                        font-size: 18px;
                    }

                    input[type="submit"]{
                        margin-top: 20px;
                        padding: 12px;
                        width: 100%;
                        background: #28a745;
                        color: white;
                        border: none;
                        border-radius: 10px;
                        font-size: 18px;
                        cursor: pointer;
                    }

                    input[type="submit"]:hover{
                        background: green;
                    }

                </style>

            </head>

            <body>

                <div class="quiz-box">

                    <h1>🎯 Simple Knowledge Quiz</h1>

                    <form action="/result" method="POST">

                        <div class="question">
                            1. Python is a ? <br><br>

                            <input type="radio" name="q1" value="correct"> Programming Language <br>
                            <input type="radio" name="q1" value="wrong"> Game <br>
                            <input type="radio" name="q1" value="wrong"> Browser
                        </div>

                        <div class="question">
                            2. HTML is used for ? <br><br>

                            <input type="radio" name="q2" value="correct"> Web Pages <br>
                            <input type="radio" name="q2" value="wrong"> Music <br>
                            <input type="radio" name="q2" value="wrong"> Hacking
                        </div>

                        <div class="question">
                            3. Flask is a ? <br><br>

                            <input type="radio" name="q3" value="correct"> Python Framework <br>
                            <input type="radio" name="q3" value="wrong"> Mobile App <br>
                            <input type="radio" name="q3" value="wrong"> Database
                        </div>

                        <input type="submit" value="Submit Quiz">

                    </form>

                </div>

            </body>

            </html>
            """

        else:
            message = """
            <div class="error">
                ❌ Invalid Username or Password
            </div>
            """

    return f"""
    <html>

    <head>

        <title>Colorful Login</title>

        <style>

            body {{
                margin: 0;
                padding: 0;
                font-family: Arial;
                background: linear-gradient(to right, #4facfe, #00f2fe);
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }}

            .login-box {{
                background: white;
                padding: 40px;
                width: 350px;
                border-radius: 15px;
                box-shadow: 0px 0px 20px rgba(0,0,0,0.3);
                text-align: center;
            }}

            h2 {{
                color: #333;
            }}

            input[type="text"],
            input[type="password"] {{
                width: 90%;
                padding: 12px;
                margin: 10px 0;
                border: 2px solid #4facfe;
                border-radius: 8px;
            }}

            input[type="submit"] {{
                width: 95%;
                padding: 12px;
                background: #4facfe;
                color: white;
                border: none;
                border-radius: 8px;
                font-size: 18px;
                cursor: pointer;
            }}

            input[type="submit"]:hover {{
                background: #007bff;
            }}

            .error {{
                background: red;
                color: white;
                padding: 10px;
                border-radius: 8px;
                margin-bottom: 10px;
            }}

        </style>

    </head>

    <body>

        <div class="login-box">

            <h2>🌟 Flask Login Page 🌟</h2>

            {message}

            <form method="POST">

                <input type="text" name="username" placeholder="Enter Username" required>

                <input type="password" name="password" placeholder="Enter Password" required>

                <input type="submit" value="Login">

            </form>

        </div>

    </body>

    </html>
    """


# ---------------- RESULT PAGE ----------------

@app.route("/result", methods=["POST"])
def result():

    score = 0

    answers = [
        request.form.get("q1"),
        request.form.get("q2"),
        request.form.get("q3")
    ]

    for answer in answers:
        if answer == "correct":
            score += 1

    # PERFORMANCE MESSAGE
    if score == 3:
        status = "🏆 Excellent! Maintain your knowledge."
        color = "green"

    elif score == 2:
        status = "👍 Good! Small improvement needed."
        color = "orange"

    else:
        status = "📚 You need more practice and knowledge improvement."
        color = "red"

    return f"""
    <html>

    <head>

        <title>Quiz Result</title>

        <style>

            body{{
                font-family: Arial;
                background: linear-gradient(to right, #36d1dc, #5b86e5);
                text-align: center;
                color: white;
                padding-top: 100px;
            }}

            .result-box{{
                background: white;
                color: black;
                width: 400px;
                margin: auto;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0px 0px 20px gray;
            }}

            h1{{
                color: {color};
            }}

            .score{{
                font-size: 28px;
                margin: 20px;
            }}

        </style>

    </head>

    <body>

        <div class="result-box">

            <h1>🎉 Quiz Completed</h1>

            <div class="score">
                Your Score: {score}/3
            </div>

            <h2>{status}</h2>

        </div>

    </body>

    </html>
    """


# ---------------- RUN APP ----------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
