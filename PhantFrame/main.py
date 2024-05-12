from app import PyFrameApp
from middleware import Middleware
import json

app = PyFrameApp()


@app.route("/home", allowed_methods=["get"])
def home(request, response):
   response.text = "Hello from the Home page"
@app.route("/about", allowed_methods="put")
def about(request, response):
    response.text = "Hello from the About page"

@app.route("/hello/{name}")
def greeting(requset, response, name):
    response.text = f"Hello {name}"
@app.route("/books")
class Books:
    def get(self, request, response):
        response.text= "Books Page"

    def post(self, request, response):
        response.text = "Endpoint to create a book"

def new_handler(req, resp):
    resp.text = "From new handler"

app.add_route("/new-handler", new_handler)

@app.route("/template")
def template_handler(req, resp):
    resp.html = app.template(
        "home.html",
        context={"new_title": "New Title", "new_body": "Best Body"}
    )
@app.route("/json")    
def json_handler(req, resp):
    response_data = {"name": "some name", "type": "json"}
    resp_body = json.dumps(response_data).encode()
    resp.json = response_data

def on_exception(req, resp, exc):
    resp.text = str(exc)

app.add_exception_handler(on_exception)

@app.route("/exception")
def exception_throwing_handler(req, resp):
    raise AttributeError("some exception")

class LoggingMiddleware(Middleware):
    def __init__(self, app):
        super().__init__(app)
    def process_request(self, req):
        print("request is being called")
    def process_response(self, req, rasp):
        print("responce has been generated")
app.add_middleware(LoggingMiddleware)


