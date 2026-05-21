from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():

    message = ""

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "1234":
            message = """
            <div class="success">
                ✅ Login Successful
            </div>
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
        <title>Colorful Flask Login</title>

        <style>

            body {{
                margin: 0;
                padding: 0;
                font-family: Arial, sans-serif;
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
                margin-bottom: 20px;
            }}

            input[type="text"],
            input[type="password"] {{
                width: 90%;
                padding: 12px;
                margin: 10px 0;
                border: 2px solid #4facfe;
                border-radius: 8px;
                font-size: 16px;
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
                transition: 0.3s;
            }}

            input[type="submit"]:hover {{
                background: #007bff;
                transform: scale(1.05);
            }}

            .success {{
                background: #28a745;
                color: white;
                padding: 10px;
                border-radius: 8px;
                margin-bottom: 15px;
            }}

            .error {{
                background: #dc3545;
                color: white;
                padding: 10px;
                border-radius: 8px;
                margin-bottom: 15px;
            }}

            .footer {{
                margin-top: 15px;
                color: gray;
                font-size: 14px;
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

            <div class="footer">
                Made with Flask ❤️
            </div>

        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
