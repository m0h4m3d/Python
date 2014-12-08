from wsgiref.simple_server import make_server
import sqlite3



conn = sqlite3.connect("zooData.sqlite")
cursor = conn.cursor()
cursor.execute("create table if not exists animal_count (animalName text, animalCount integer)")
def get_form_vals(post_str):
    form_vals = {item.split("=")[0]: item.split("=")[1] for item in post_str.decode().split("&")}
    return form_vals

def animal_data(environ, start_response):
    #print("ENVIRON:", environ)
    message=""
    status = '200 OK'
    headers = [('Content-type', 'html; charset=utf-8')]
    start_response(status, headers)
    if(environ['REQUEST_METHOD'] == 'POST'):
            message += "<br>Your data has been recorded:"
            request_body_size = int(environ['CONTENT_LENGTH'])
            request_body = environ['wsgi.input'].read(request_body_size)
            form_vals = get_form_vals(request_body)
            animal = form_vals['animalName']
            count = form_vals['count']
            cursor.execute("insert into animal_count(animalName, animalCountcount) values(?, ?)", (animal, count))
            conn.commit()
    message += "<h1>Welcome to the Zoo</h1>"
    message += "<form method='POST'><br>Animal:<input type=text name='animalName'>"
    message += "<br><br>Count:<input type=text name='count'>"
    message += "<br><br><input type='submit' name='Submit' ></form>"
    return[bytes(message,'utf-8')]


httpd = make_server('', 8000, animal_data)
print("Serving on port 8000...")
httpd.serve_forever()
conn.close()
