def filter_factory(global_conf, **app_conf):
    return Foo

from webob import Request
from hyperbmp.read import HbmpView

class Foo(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        req = Request(environ)
        res = req.get_response(self.app)
        content = res.body
        mimetype = res.content_type

        thingie = HbmpView()
        if thingie.match_view(req, content, mimetype):
            return thingie.render(req, content)(environ, start_response)
        return res(environ, start_response)

from svenweb.factory import factory as base_factory
from hyperbmp.edit import HbmpEditor

def app_factory(global_conf, **app_conf):
    return base_factory(global_conf, 
                        editor=HbmpEditor, viewer=HbmpView, 
                        **app_conf)

def single_file_app_factory(global_conf, file=None, **app_conf):
    renderer = HbmpView()

    def call(environ, start_response):
        req = Request(environ)
        content = open(file).read()
        return renderer.render(req, content)(environ, start_response)

    return call
