from webob import Response

from hyperbmp.props import RequestProperties
from hyperbmp.lib import parse, lib_js, draw

class HbmpView(object):
    
    @property
    def props(self):
        return RequestProperties()

    def match_view(self, request, content, mimetype):
        """
        returns a callable that takes (request, content)
        and returns a Response
        """
        if mimetype == 'text/csv+imgplot':
            return imageplot_render

        if mimetype == 'text/csv+hbmp':
            return self.render

    def render(self, req, content):
        html = """
<html>
<head>
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.3/jquery.min.js"></script>
<script type="text/javascript">
  $(document).ready(function () {
    $("td").click(go);
  });

  %s

</script></head><body>""" % lib_js()

        html += draw(req, content, self.props)

        html += "</body></html>"
        return Response(html)

image_tmpl = """
<img src="%s" style="position: absolute;
                     top: %s; left: %s;
                     z-index: %s;" />
"""

def imageplot_render(req, content):
    images = []
    for line in content.splitlines():
        data = line.split(',')
        img_src, coords = data[0], data[1:]
        z_index = "auto"
        if len(coords) == 3:
            z_index = coords[2]
        image = image_tmpl % (img_src, coords[0], coords[1], z_index)
        images.append(image)
    images = '\n'.join(images)
    html = "<html><body>\n%s\n</body></html>" % images
    return Response(html)
