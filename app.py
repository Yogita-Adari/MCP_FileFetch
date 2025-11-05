from fastapi import FastAPI, UploadFile, File, Query
import uvicorn
import os

app = FastAPI()
UPLOAD_DIR = "uploaded_files"

# Ensure upload directory exists
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """Uploads a text file and saves it locally."""
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_location, "wb") as f:
        f.write(await file.read())
    return {"message": f"File '{file.filename}' uploaded successfully."}


@app.get("/search")
def search_keyword(keyword: str = Query(..., min_length=1), filename: str = Query(...)):
    """Searches for a keyword in the specified uploaded file."""
    try:
        file_path = os.path.join(UPLOAD_DIR, filename)
        if not os.path.exists(file_path):
            return {"error": f"File '{filename}' not found."}

        with open(file_path, "r") as file:
            lines = file.readlines()

        matches = [line.strip() for line in lines if keyword.lower() in line.lower()]
        return {"filename": filename, "keyword": keyword, "matches": matches}

    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
