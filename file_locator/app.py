import os
import sys
import requests
import json 
import time
import pdb
import collections
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session,g,redirect,url_for, \
abort, render_template,flash
import flask
import urllib2
import requests
from contextlib import closing
app=Flask(__name__)

app.config.update(dict(
SECRET_KEY='development key'
))

listof_files = []
location_list = []
big_list = collections.defaultdict(list)

@app.route('/', methods=['GET', 'POST'])

def search():
    error = None
    if request.method == 'POST':
        file_name=flask.request.form['filename']
        text = json_log (file_name) 
    	return render_template('search.html', error=error, text=text)
    return render_template('search.html', error=error)


def json_log (file_str):
   if file_str in big_list:
      n = big_list[file_str]
      l=0
      p = ""
      for v in n:
         l=location_list[v]
         l = l[1:]
         p = p+ fullpath +  l +"<br/>"
      return p
   else:
      return "No such file exists"           
         


if __name__ == "__main__":
   pathname = os.path.dirname(sys.argv[0])
   fullpath = os.path.abspath(pathname)
   start_time = time.time()
   i=0
   fout = open("test.json",'w')
   for dirname, dirnames, filenames in os.walk('.'):
      for subdirname in dirnames:
         os.path.join(dirname,subdirname)
      for filename in filenames:
         location = os.path.join(dirname,filename)
         location_list.append (location)
         file_name = filename
         s = tuple(file_name)
         r = []
         for size in range(1, len(s)+1):
            for index in range(len(s)+1-size):
               x= file_name[index:index+size]
               big_list[x].append(i)
         i=i+1
   
   app.run(debug=True)
     
     

