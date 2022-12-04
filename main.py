from flask import Flask, jsonify
from threading import Thread
import os
import shutil

app = Flask('')


@app.route('/')
def home():
  return "I'm alive"


@app.route('/api/makestore/<string:storename>/<int:tables>')
def makestore(storename, tables):
  os.mkdir(f"./DB/{storename}")
  f = open(f'./DB/{storename}/{storename}.txt', 'w')
  f.write(str(tables))
  f.close()
  d = 1
  for i in range(0, tables):
    f = open(f'./DB/{storename}/{d}.txt', 'w')
    f.close()
    d += 1
  d = 1
  for j in range(0, tables):
    f = open(f'./DB/{storename}/{d}price.txt', 'w')
    f.write(str(0))
    f.close()
    d += 1
  return jsonify({"result": "success!"})


@app.route(
  '/api/order/<string:storename>/<int:table>/<string:menuname>/<int:menuprice>'
)
def order(storename, table, menuname, menuprice):
  f = open(f'./DB/{storename}/{table}.txt', 'a')
  f.write(menuname + "\n")
  f.close()
  f = open(f'./DB/{storename}/{table}price.txt', 'r')
  lines = f.readlines()
  f.close()
  price = int(lines[0]) + menuprice
  f = open(f'./DB/{storename}/{table}price.txt', 'w')
  f.write(str(price))
  f.close()
  return jsonify({"result": "success!"})


@app.route('/api/call/<string:storename>/<int:table>')
def call(storename, table):
  f = open(f'./DB/{storename}/{table}.txt', 'a')
  f.write("직원호출\n")
  f.close()
  return jsonify({"result": "success!"})


@app.route('/api/deletestore/<string:storename>')
def deletestore(storename):
  shutil.rmtree(f'./DB/{storename}')
  return jsonify({"result": "success!"})


def run():
  app.run(host='0.0.0.0', port=7000)


t = Thread(target=run)
t.start()
