import store

#SERVIDOR WEB
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app= FastAPI()

@app.get('/')  #RUTAS
def get_list():
    return [1,2,3]

@app.get('/contact')
def get_list():
    return {"name": 'Platzi'}

@app.get('/prueba', response_class=HTMLResponse)
def get_list():
    return """
        <h1>Hola soy Karen</h1>
        <p>Es un párrafo de prueba que funciona el servidor web con html y no solo arroja datos</p>
    """

def run():
    store.get_categories()

if __name__=='__main__':
    run()