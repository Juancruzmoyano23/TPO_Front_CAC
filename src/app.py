from flask import Flask, jsonify, request, send_file
from psycopg2 import connect, extras


app = Flask(__name__)


def get_connection():
    return connect(
        host="localhost",
        port=15432,
        database="tpo13_backend",
        user="postgres",
        password="password",
    )

@app.get("/api/recetas")
def get_recetas():

    # conectar a la database
    conn = get_connection()
    # crear un cursor -- se encarga de ejecutar las queries (selects)
    cursor = conn.cursor(cursor_factory=extras.RealDictCursor)

    # ejecutar la query para obtener registros
    cursor.execute("select * from recetas")
    recetas = cursor.fetchall()

    # cerrar el cursor y la conexión
    cursor.close()
    conn.close()

    # retornar los resultados
    return (recetas)


@app.post("/api/recetas")
def create_receta():

    receta_data = request.get_json()

    # conectar a la bbdd
    conn = get_connection()
    # crear un cursor -- se encarga de ejecutar las queries
    cursor = conn.cursor(cursor_factory=extras.RealDictCursor)

    # ejecutar la query para obtener registros
    query = """
    insert into recetas (name, description, ingredient, rating, receta_id)
    VALUES (%s, %s, %s, %s, %s)
    RETURNING *
    """
    cursor.execute(
        query=query,
        vars=(
            receta_data["name"],
            receta_data["description"],
            receta_data["ingredient"],
            receta_data["rating"],
            receta_data["receta_id"],
        ),
    )
    receta = cursor.fetchone()
    conn.commit()
    
    # cerrar el cursor y la conexión
    cursor.close()
    conn.close()

    if receta is None:
        return jsonify({"message": "receta not created"}), 400

    # retornar los resultados
    return jsonify(receta), 201


@app.get("/api/recetas/<receta_id>")
def get_receta(receta_id):
    # conectar a la bbdd
    conn = get_connection()
    # crear un cursor -- se encarga de ejecutar las queries
    cursor = conn.cursor(cursor_factory=extras.RealDictCursor)

    # ejecutar la query para obtener registros
    cursor.execute(
        query="SELECT * FROM recetas WHERE receta_id = %s", 
        vars=(receta_id, )
    )   
    receta = cursor.fetchone()
    # cerrar el cursor y la conexión
    cursor.close()
    conn.close()

    return jsonify(receta)
    
    if receta is None:
        return jsonify({"message": "Receta not found"}), 404

    # retornar los resultados
    return jsonify(receta)


@app.delete("/api/recetas/<receta_id>")
def delete_receta(receta_id):
    conn = get_connection()
    # crear un cursor -- se encarga de ejecutar las queries
    cursor = conn.cursor(cursor_factory=extras.RealDictCursor)

    # ejecutar la query para obtener registros
    cursor.execute(
        query="DELETE FROM recetas WHERE receta_id = %s RETURNING *", vars=(receta_id,)
    )   
    receta = cursor.fetchone()
    conn.commit()
    # cerrar el cursor y la conexión
    cursor.close()
    conn.close()
    
    if receta is None:
        return jsonify({"message": "Receta not found"}), 404

    # retornar los resultados
    return jsonify(receta)


# PUT / PATCH
@app.patch("/api/movies/<movie_id>")
def update_movie(movie_id):
    return {"title": "Spiderman 2", "year": 2002, "id": movie_id}


@app.put("/api/movies/<movie_id>")
def update_movie_put(movie_id):
    return {"title": "Spiderman 2", "year": 2002, "id": movie_id}

@app.get("/")
def home():
    return send_file("static/index.html")

@app.get("/soporte")
def soporte():
    return send_file("static/pages/soporte.html")

@app.get("/register")
def register():
    return send_file("static/pages/register.html")

@app.get("/chefs")
def chefs():
    return send_file("static/pages/chefs.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
