#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, json
from flask import Flask, render_template, abort


app = Flask(__name__)


def get_file_content():
    data = {}
    # file_list =  os.listdir(os.chdir('/home/shiyanlou/files')) # 不能写死
    file_list = os.listdir(os.chdir(os.path.abspath(os.pardir) + '/files'))
    for filename in file_list:
        with open(filename) as f:
            # data[filename.split('.')[0]] = json.loads(f.read())
            # data[filename[:-5]] = json.load(f) # 推荐
            data[filename.split('.')[0]] = json.load(f)
    return data


def get_file_name(filename):
    content = get_file_content()
    return content.get(filename)


# def get_file_content():
#     file_content = []
#     for i in get_file_list():
#         with open(i, 'r') as f:
#             content = json.loads(f.read())
#             file_content.append(content)
#     return file_content


def get_title_content():
    title_list = []
    for v in get_file_content().values():
        title_list.append(v.get('title'))
    return title_list


@app.route('/')
def index():
    title_list = get_title_content()
    return render_template('index.html', title_list=title_list)


@app.route('/files/<filename>')
def file(filename):
    filename = get_file_name(filename)
    # print(filename)
    if not filename:
        abort(404)
    else:
        return render_template('file.html', filename=filename)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(port=3000, debug=True)
    
