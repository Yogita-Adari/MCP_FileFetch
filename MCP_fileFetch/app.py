from fastapi import FastAPI, Query
import uvicorn

app = FastAPI()

@app.get("/search")
def search_keyword(keyword: str = Query(..., min_length=1)):
    try:
        with open("sample.txt", "r") as file:
            lines = file.readlines()
        matches = [line.strip() for line in lines if keyword.lower() in line.lower()]
        return {"keyword": keyword, "matches": matches}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
