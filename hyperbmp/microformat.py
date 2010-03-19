from hyperbmp.lib import draw
from hyperbmp.props import RequestProperties

from pyquery import PyQuery as pq
from webob import Request, Response

class Filter(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        req = Request(environ)
        res = req.get_response(self.app)
        if res.status_int != 200:
            return res(environ, start_response)
        if res.content_type != 'text/html':
            return res(environ, start_response)
        d = pq(res.body)
        match = d("pre.hbmp")
        if not len(match):
            return res(environ, start_response)
        props = RequestProperties()
        for i in range(len(match)):
            el = match.eq(i)
            content = el.html()
            rendered = draw(req, content, props)
            el.html(rendered)
        res.body = str(d)
        return res(environ, start_response)

def filter_factory(*args, **kw):
    def filter(app):
        return Filter(app)
    return filter
