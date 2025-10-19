from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .db import Base, engine, get_db
from . import models, schemas, crud

app = FastAPI(title="Journal API", version="1.0.0")

# ---- CORS (for local dev) ----
# For a local file `index.html` or any localhost port, this is simplest.
# Note: allow_credentials=False is recommended when using "*" origins.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # allow all origins for dev
    allow_credentials=False,    # keep False when using "*"
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables in Postgres on startup (dev convenience)
Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/entries", response_model=schemas.EntryOut, status_code=201)
def create_entry(data: schemas.EntryCreate, db: Session = Depends(get_db)):
    return crud.create_entry(db, data)

@app.get("/entries", response_model=list[schemas.EntryOut])
def list_all(db: Session = Depends(get_db)):
    return crud.list_entries(db)

@app.get("/entries/{entry_id}", response_model=schemas.EntryOut)
def read_one(entry_id: int, db: Session = Depends(get_db)):
    entry = crud.get_entry(db, entry_id)
    if not entry:
        raise HTTPException(404, "Entry not found")
    return entry

@app.patch("/entries/{entry_id}", response_model=schemas.EntryOut)
def update_entry(entry_id: int, data: schemas.EntryUpdate, db: Session = Depends(get_db)):
    entry = crud.update_entry(db, entry_id, data)
    if not entry:
        raise HTTPException(404, "Entry not found")
    return entry

@app.delete("/entries/{entry_id}", status_code=204)
def delete_entry(entry_id: int, db: Session = Depends(get_db)):
    ok = crud.delete_entry(db, entry_id)
    if not ok:
        raise HTTPException(404, "Entry not found")
    return
