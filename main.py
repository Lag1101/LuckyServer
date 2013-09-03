__author__ = 'vasiliy.lomanov'

from flask import Flask
app = Flask(__name__)

f = open("index.html")
s = f.readlines()
index = ''
for i in s:
    index += i+"\n"
f.close()


@app.route("/<param>")
def listen(param):
    return param


if __name__ == "__main__":
    app.run(host='0.0.0.0')