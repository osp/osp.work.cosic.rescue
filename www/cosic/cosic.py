import subprocess
import tempfile

from bottle import (run, template, get, post, request, response)


@get('/')
def form():
    return template("templates/form")

@get('/logo.<filetype:re:(png|eps)>')
def preview(filetype):
    download = request.query.get('download')
    thickness = request.query.get('thickness', 0.7)
    period = request.query.get('period', 2.1)
    color = request.query.get('color')

    if color:
        red = float(int(color[1:3], 16)) / 255
        green = float(int(color[3:5], 16)) / 255
        blue = float(int(color[5:7], 16)) / 255
    else:
        red = 0
        green = 0
        blue = 0

    context = dict(red=red, green=green, blue=blue, period=period, thickness=thickness)

    if filetype == "png":
        f = tempfile.NamedTemporaryFile(delete=True, suffix=".eps")
        f.write(template("templates/logo", **context))
        f.seek(0)

        args = [
            "gs",
            "-q",
            "-dNOPAUSE", "-dBATCH", "-dSAFER",
            "-dEPSCrop",
            "-sDEVICE=png16m",
            "-dGraphicsAlphaBits=4",
            "-dTextAlphaBits=4",
            "-sOutputFile=-",
            "-"
            ]

        output = subprocess.check_output(args, stdin=f)
        f.close()

        if download:
            response.headers["Content-Disposition"] = "attachment; filename=\"logo.png\""
        response.content_type = 'image/png'
    else:
        output = template("templates/logo", **context)

        if download:
            response.headers["Content-Disposition"] = "attachment; filename=\"logo.eps\""
        response.content_type = 'image/x-eps'

    return output


if __name__ = "__main__":
    run(host='localhost', port=8080, reloader=False)
