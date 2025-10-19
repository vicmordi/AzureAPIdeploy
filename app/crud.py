from sqlalchemy.orm import Session
from . import models, schemas

def create_entry(db: Session, data: schemas.EntryCreate):
    entry = models.JournalEntry(title=data.title, content=data.content)
    db.add(entry); db.commit(); db.refresh(entry)
    return entry

def list_entries(db: Session):
    return db.query(models.JournalEntry).order_by(models.JournalEntry.id.desc()).all()

def get_entry(db: Session, entry_id: int):
    return db.query(models.JournalEntry).filter(models.JournalEntry.id == entry_id).first()

def update_entry(db: Session, entry_id: int, data: schemas.EntryUpdate):
    entry = get_entry(db, entry_id)
    if not entry: return None
    if data.title is not None: entry.title = data.title
    if data.content is not None: entry.content = data.content
    db.commit(); db.refresh(entry)
    return entry

def delete_entry(db: Session, entry_id: int) -> bool:
    entry = get_entry(db, entry_id)
    if not entry: return False
    db.delete(entry); db.commit()
    return True
