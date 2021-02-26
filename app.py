import os
import traceback

from flask import Flask, request, send_from_directory

from deaths import Deaths

app = Flask(__name__)


@app.route("/")
def root():
    return app.send_static_file("index.html")


@app.route("/jquery")
def jquery():
    return app.send_static_file("jquery.js")


@app.route("/api/0/deaths")
def deaths():
    try:
        days = int(request.args.get("days", None))
        assert 0 < days < 1000
    except:
        traceback.print_exc()
        return {"error": True}

    return D.last(days)


if __name__ == "__main__":
    D = Deaths()
    app.run("0.0.0.0", port=int(os.getenv("PORT", "80")))
