from fastapi import APIRouter, Query, HTTPException, status, Depends
from typing import List
from sqlmodel import Session, select
from fastapi import Path

from models import University, Favorite, User
from services import (
    fetch_universities_by_country,
    fetch_universities_by_name,
    fetch_universities_in_brazil,
)
from db import engine

router = APIRouter()

def get_session():
    with Session(engine) as session:
        yield session



@router.get("/universidades/pais", response_model=List[University])
def get_universities_by_country(country: str = Query(..., example="Brazil")):
    return fetch_universities_by_country(country)

@router.get("/universidades/nome", response_model=List[University])
def get_universities_by_name(name: str = Query(..., example="Federal")):
    return fetch_universities_by_name(name)

@router.get("/universidades/brasil", response_model=List[University])
def get_universities_in_brazil():
    return fetch_universities_in_brazil()

@router.post("/favoritos", status_code=status.HTTP_201_CREATED, response_model=Favorite)
def add_favorite(favorite: Favorite, session: Session = Depends(get_session)):
    session.add(favorite)
    session.commit()
    session.refresh(favorite)
    return favorite

@router.get("/favoritos", response_model=List[Favorite])
def list_favorites(session: Session = Depends(get_session)):
    favoritos = session.exec(select(Favorite)).all()
    return favoritos

@router.delete("/favoritos/{id}", status_code=204)
def delete_favorite(id: int = Path(...), session: Session = Depends(get_session)):
    favorito = session.get(Favorite, id)
    if not favorito:
        raise HTTPException(status_code=404, detail="Favorito não encontrado")
    session.delete(favorito)
    session.commit()
    return

@router.put("/favoritos/{id}", response_model=Favorite)
def update_favorite(id: int, updated: Favorite, session: Session = Depends(get_session)):
    favorito = session.get(Favorite, id)
    if not favorito:
        raise HTTPException(status_code=404, detail="Favorito não encontrado")

    favorito.name = updated.name
    favorito.country = updated.country
    favorito.domains = updated.domains
    favorito.web_pages = updated.web_pages

    session.commit()
    session.refresh(favorito)
    return favorito


@router.post("/register")
def register_user(user: User, session: Session = Depends(get_session)):
    session.add(user)
    session.commit()
    return {"msg": "Usuário registrado com sucesso"}

@router.post("/login")
def login(user: User, session: Session = Depends(get_session)):
    db_user = session.exec(select(User).where(User.username == user.username)).first()
    if not db_user or db_user.password != user.password:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    # Aqui deveria retornar um token JWT
    return {"msg": "Login bem-sucedido (JWT simulado)"}
