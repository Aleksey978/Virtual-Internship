from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
from database import SessionLocal
from validation import PerevalBase, UpdateResponse

app = FastAPI()

# Зависимости
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Метод POST для создания перевала
@app.post("/perevals/", response_model=PerevalBase)
def create_pereval(pereval: PerevalBase, db: Session = Depends(get_db)):
    # Создание пользователя
    user = models.User(**pereval.user.dict())
    db.add(user)
    db.commit()
    db.refresh(user)

    # Создание координат
    coords = models.Coords(**pereval.coords.dict())
    db.add(coords)
    db.commit()
    db.refresh(coords)

    # Создание уровня сложности
    level = models.Level(**pereval.level.dict())
    db.add(level)
    db.commit()
    db.refresh(level)

    # Создание перевала
    pereval_data = pereval.dict()
    pereval_data.pop("user")
    pereval_data.pop("coords")
    pereval_data.pop("level")
    pereval_data.pop("images")
    pereval_data["user_id"] = user.id
    pereval_data["coords_id"] = coords.id
    pereval_data["level_id"] = level.id
    db_pereval = models.Pereval(**pereval_data)
    db.add(db_pereval)
    db.commit()
    db.refresh(db_pereval)

    for image in pereval.images:
        db_image = models.Image(data=image.data, title=image.title, pereval_id=db_pereval.id)
        db.add(db_image)
        db.commit()

    return db_pereval


@app.get("/perevals/{pereval_id}", response_model=PerevalBase)
def get_pereval(pereval_id: int, db: Session = Depends(get_db)):
    db_pereval = db.query(models.Pereval).filter(models.Pereval.id == pereval_id).first()
    if db_pereval is None:
        raise HTTPException(status_code=404, detail="Pereval not found")
    return db_pereval

@app.patch("/perevals/{pereval_id}", response_model=UpdateResponse)
def update_pereval(pereval_id: int, pereval: PerevalBase, db: Session = Depends(get_db)):
    db_pereval = db.query(models.Pereval).filter(models.Pereval.id == pereval_id).first()
    if db_pereval is None:
        return UpdateResponse(state=0, message="Pereval not found")

    if db_pereval.status != models.PerevalStatus.new:
        return UpdateResponse(state=0, message="Pereval is not in 'new' status")
    update_data = pereval.dict(exclude={"user", "coords", "level", "images"})


    for item in pereval.images:
        db.query(models.Image).filter(models.Image.pereval_id == pereval_id).update(item.dict())


    db.query(models.Level).filter(models.Level.id == db_pereval.level_id).update(pereval.level.dict())
    db.query(models.Coords).filter(models.Coords.id == db_pereval.coords_id).update(pereval.coords.dict())
    db.query(models.Pereval).filter(models.Pereval.id == pereval_id).update(update_data)

    db.commit()
    db.refresh(db_pereval)

    return UpdateResponse(state=1, message="Pereval updated successfully")

@app.get("/perevalData/", response_model=list[PerevalBase])
def get_perevals_by_email(user__email: str, db: Session = Depends(get_db)):
    perevals = db.query(models.Pereval).join(models.User).filter(models.User.email == user__email).all()
    if not perevals:
        raise HTTPException(status_code=404, detail="No perevals found for this email")
    return perevals