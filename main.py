@app.get("/api/hello")
def hello():
    return {"message": "Hallo, die API läuft!"}

