from fastapi import FastAPI, HTTPException, Depends
from typing import List
import database
import schemas
import models

app = FastAPI()

#GET http://127.0.0.1:8000/movies
@app.get("/movies", response_model=List[schemas.Movie])
def get_movies():
    return list(models.Movie.select())

#GET http://127.0.0.1:8000/movies/2
@app.get("/movies/{movie_id}", response_model=schemas.Movie)
def get_movie(movie_id: int):
    db_movie = models.Movie.filter(models.Movie.id == movie_id).first()
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie


#POST http://127.0.0.1:8000/movies
@app.post("/movies", response_model=schemas.Movie)
def add_movies(movie: schemas.MovieBase):
    db_movie = models.Movie.create(**movie.dict())
    return db_movie

#DELETE http://127.0.0.1:8000/movies/2
@app.delete("/movies/{movie_id}", response_model=schemas.Movie)
def delete_movie(movie_id: int):
    db_movie = models.Movie.filter(models.Movie.id == movie_id).first()
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    db_movie.delete()
    return db_movie

#GET http://127.0.0.1:8000/actors
@app.get("/actors", response_model=List[schemas.Actor])
def get_actors():
    return list(models.Actor.select())

#GET http://127.0.0.1:8000/actors/2
@app.get("/actors/{actor_id}", response_model=schemas.Actor)
def get_actors(actor_id: int):
    db_actor = models.Actor.filter(models.Actor.id == actor_id).first()
    if db_actor is None:
        raise HTTPException(status_code=404, detail="Actor not found")
    return db_actor


#POST http://127.0.0.1:8000/actors
@app.post("/actors", response_model=schemas.Actor)
def add_actor(actor: schemas.ActorBase):
    db_actor = models.Actor.create(**actor.dict())
    return db_actor

#DELETE http://127.0.0.1:8000/actors/2
@app.delete("/actors/{actor_id}", response_model=schemas.Actor)
def delete_actor(actor_id: int):
    db_actor = models.Actor.filter(models.Actor.id == actor_id).first()
    if db_actor is None:
        raise HTTPException(status_code=404, detail="Actor not found")
    db_actor.delete()
    return db_actor

#POST http://127.0.0.1:8000/movies/2/actors
@app.post("/movies/{movie_id}/actors", response_model=schemas.Movie)
def assign_actor(movie_id: int, request: schemas.ActorAssign):
    db_movie = models.Movie.filter(models.Movie.id == movie_id).first()
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")

    db_movie.actors.add(models.Actor(id=request.actor_id))
    return db_movie







