import requests
from backend.main import *
from backend.database import *
from fastapi import Depends, FastAPI, Body


def get_vacancies(db, keyword, graphic, experience, emp, field, page):
    url = "https://api.hh.ru/vacancies"
    params = {
        "text": keyword,
        "schedule": graphic,
        "experience": experience,
        "employment": emp,
        "vacancy_search_fields": field,
        "per_page": page,
        "area": 1620,

    }
    headers = {
        "User-Agent": "Your User Agent",
    }

    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        vacancies = data.get("items", [])
        for vacancy in vacancies:
            vacancy_id = vacancy.get("id")
            vacancy_title = vacancy.get("name")
            vacancy_graphic = vacancy.get("schedule", {}).get("name")
            vacancy_experience = vacancy.get("experience", {}).get("name")
            vacancy_emp = vacancy.get("employment", {}).get("name")
            vacancy_url = vacancy.get("alternate_url")
            company_name = vacancy.get("employer", {}).get("name")
            vac = Vac(id = vacancy_id,title=vacancy_title,graphic=vacancy_graphic,experience=vacancy_experience,emp=vacancy_emp,company=vacancy_url,URL=company_name)
            db.add(vac)
            db.commit()
            db.refresh(vac)





    else:
        print(f"Request failed with status code: {response.status_code}")

