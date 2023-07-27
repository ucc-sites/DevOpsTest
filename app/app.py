from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route('/')
def hello_world():
    html = ('<h2 style="font-family: Consolas, monaco, monospace">' +
            '    Hello from Flask, {name}! (Python)' +
            '</h2>' +
            '<h3 style="font-family: Consolas, monaco, monospace">' +
            '    Hostname:' +
            '</h3>' +
            '<h3 style="font-family: Consolas, monaco, monospace">' +
            '    {hostname}' +
            '</h3>')
    return html.format(name=os.getenv("NAME", "World"), hostname=socket.gethostname())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)