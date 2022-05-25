from werkzeug.wrappers import response
from movies import *



@app.route('/movies/<int:id>', methods=['GET'])
def get_movie_by_id(id):
    return_value = Movie.get_movie(id)
    return jsonify(return_value)

@app.route("/movies", methods = ['POST'])    
def add_movie():
    request_data = request.get_json()
    Movie.add_movie(request_data["title"],request_data['year'],request_data['genre'])
    response = Response("Movie add ",201 ,mimetype='application/json')
    return response

@app.route('/movies/<int:id>', methods=['PUT'])
def update_movie(id):
    '''Function to edit movie in our database using movie id'''
    request_data = request.get_json()
    Movie.update_movie(id, request_data['title'], request_data['year'], request_data['genre'])
    response = Response("Movie Updated", status=200, mimetype='application/json')
    return response

@app.route('/movies/<int:id>', methods=['DELETE'])
def remove_movie(id):
    '''Function to delete movie from our database'''
    Movie.delete_movie(id)
    response = Response("Movie Deleted", status=200, mimetype='application/json')
    return response

if __name__ == "__main__":
    app.run(debug=True)    