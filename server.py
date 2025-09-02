import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Shruti ChatBot is alive on Render!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

