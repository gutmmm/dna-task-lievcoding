import uvicorn

if __name__ == "__main__":
    print("Starting server...")
    uvicorn.run("app.api.main:app", host="0.0.0.0", port=8000, reload=True)
