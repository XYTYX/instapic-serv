from manage import app

@app.route("/health")
def health():
    return 200