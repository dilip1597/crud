
import json
from flask import Flask, request , Response, jsonify


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app =Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

class Movie(db.Model):
    __tablename__ = 'movies' # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    title = db.Column(db.String(80), nullable=False)
    # nullable is false so the column can't be empty
    year = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(80), nullable=False)

    def json(self):
            return {'id': self.id, 'title': self.title,
                    'year': self.year, 'genre': self.genre}

    def add_movie(_title, _year, _genre):
            '''function to add movie to database using _title, _year, _genre
            as parameters'''
            # creating an instance of our Movie constructor
            new_movie = Movie(title=_title, year=_year, genre=_genre)
            db.session.add(new_movie)  # add new movie to database session
            db.session.commit()

    def get_all_movies():
            '''function to get all movies in our database'''
            return [Movie.json(movie) for movie in Movie.query.all()]

    def get_movie(_id):
            return [Movie.json(Movie.query.filter_by(id=_id).first())] 

    def update_movie(_id, _title, _year, _genre):
            '''function to update the details of a movie using the id, title,
            year and genre as parameters'''
            movie_to_update = Movie.query.filter_by(id=_id).first()
            movie_to_update.title = _title
            movie_to_update.year = _year
            movie_to_update.genre = _genre
            db.session.commit()

    def delete_movie(_id):
            '''function to delete a movie from our database using
            the id of the movie as a parameter'''
            Movie.query.filter_by(id=_id).delete()
            # filter movie by id and delete
            db.session.commit()        