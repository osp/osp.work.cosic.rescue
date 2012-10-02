import base64
import ghostscript
from bottle import route, run, template, get, post, request, static_file, response
import subprocess



from cStringIO import StringIO
import sys


@route('/')
def index():
    args = [
        "gs",
        "-q",
        "-dNOPAUSE", "-dBATCH", "-dSAFER",
        "-sDEVICE=png16m",
        "-dGraphicsAlphaBits=4",
        "-sOutputFile=/tmp/out.png",
        "../logo/squaresWeb.eps" 
        ]

    subprocess.call(args)
    return static_file('out.png', root='/tmp/')


@get('/foo/') # or @route('/login')
def login_form():
    return '''<form method="POST" action="/login">
                <input name="name"     type="text" />
                <input name="password" type="password" />
                <input type="submit" />
              </form>'''

@post('/foo/:name') # or @route('/login', method='POST')
def logo_submit(name="World"):
    return template('<b>Hello {{name}}</b>!', name=name)


run(host='localhost', port=8080, reloader=True)
