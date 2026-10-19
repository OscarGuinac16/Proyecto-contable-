from fastapi import FastAPI, Depends, HTTPException
from database import get_db

app = FastAPI(title="API CRUD Oracle")

@app.get("/test-db")
def probar_bd(db = Depends(get_db)):
    try:
        cursor = db.cursor()
        cursor.execute("SELECT '¡Conectado a Oracle!' FROM DUAL")
        return {"mensaje": cursor.fetchone()[0], "version": db.version}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))