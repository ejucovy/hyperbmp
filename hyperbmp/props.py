
class RequestProperties(object):

    default = {'height': 16, 'width': 16, 
               'pixelheight': '50px', 'pixelwidth': '50px',}    

    def height(self, req):
        if req.GET.has_key('h'):
            return int(req.GET['h'])

        return self.default['height']

    def width(self, req):
        if req.GET.has_key('w'):
            return int(req.GET['w'])

        return self.default['width']

    def pixelheight(self, req):
        if req.GET.has_key('ph'):
            return req.GET['ph']

        return self.default['pixelheight']

    def pixelwidth(self, req):
        if req.GET.has_key('pw'):
            return req.GET['pw']

        return self.default['pixelwidth']

