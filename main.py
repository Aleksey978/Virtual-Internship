from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
from database import SessionLocal
from validation import PerevalBase

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


