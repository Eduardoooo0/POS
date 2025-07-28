from fastapi import APIRouter, Query
from typing import List, Optional
from models import University
from services import fetch_universities_by_country, fetch_universities_by_name,fetch_universities_in_brazil

router = APIRouter()

@router.get("/universidades/pais", response_model=List[University])
def get_universities_by_country(country: str = Query(..., example="Brazil")):
    return fetch_universities_by_country(country)

@router.get("/universidades/nome", response_model=List[University])
def get_universities_by_name(name: str = Query(..., example="Federal")):
    return fetch_universities_by_name(name)

@router.get("/universidades/brasil", response_model=List[University])
def get_universities_by_name():
    return fetch_universities_in_brazil()
