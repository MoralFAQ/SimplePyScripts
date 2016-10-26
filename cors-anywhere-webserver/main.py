#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


from flask import Flask, Response, request
app = Flask(__name__)
app.debug = True

from urllib.request import urlopen


@app.route('/')
def index():
    url = request.args.get('url')
    print('URL:', url)
    if url is None:
        return "Append url, please: {}?url=&lt;your_url&gt;".format(request.host_url)

    with urlopen(url) as f:
        content = f.read()
        headers = dict(f.getheaders())

        rs = Response(content)
        rs.headers.extend(headers)
        rs.headers['Access-Control-Allow-Origin'] = '*'

        return rs


if __name__ == "__main__":
    # Localhost
    app.run()

    # # Public IP
    # app.run(host='0.0.0.0')