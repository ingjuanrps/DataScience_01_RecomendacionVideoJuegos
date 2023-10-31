from fastapi import FastAPI
from route.user import user

app = FastAPI() #Aplicación

app.include_router(user)