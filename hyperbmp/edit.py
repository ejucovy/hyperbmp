from svenweb.edit import BaseEditor
from webob import Response
from webob import exc

from hyperbmp.props import RequestProperties
from hyperbmp.lib import parse, lib_js, draw, render_controls, some_colors, render_addform

import mimetypes
mimetypes.add_type('text/csv+hbmp', '.hbmp')

def uploader_form():
    form = """<html><body><form name="upload_form" method="post" enctype="multipart/form-data">
<label for="file">Upload a file</label><input type="file" name="file"/>
<br/>
<label for="svenweb.commit_message">Change note</label>
<input type="text" name="svenweb.commit_message" />
<br/>
<input type="submit" value="upload"/></form></body></html>"""

    return Response(form)

from mimetypes import guess_type
from svenweb.lib import location
def uploader_post(req):
    loc = location(req)
    fin = req.POST['file']
    mimetype = guess_type(fin.filename)[0]
    contents = fin.file.read()
    message = req.POST.get('svenweb.commit_message')
    return (contents, message, mimetype, 
            exc.HTTPSeeOther(location=loc))

class HbmpEditor(BaseEditor):

    @property
    def props(self):
        return RequestProperties()

    def post(self, request):
        if request.POST.has_key('file'):
            return uploader_post(request)
        return BaseEditor.post(self, request)

    def new(self, request):
        if 'raw' in request.GET:
            return BaseEditor.new(self, request)

        if request.GET.has_key('hbmp'):
            return self.hbmp_new(request)

        if request.GET.has_key('file'):
            return uploader_form()

        if self.new_default_mimetype(request) == 'text/csv+hbmp':
            return self.hbmp_new(request)

        return BaseEditor.new(self, request)

    def hbmp_new(self, request):
        height = self.props.height(request)
        width = self.props.width(request)

        content = []
        for j in range(height):
            content.append(','.join(["white" for i in range(width)]))
        content = '\n'.join(content)
        return self.render(request, content, new=True)

    def editform(self, request, content, mimetype):
        if 'raw' in request.GET:
            return BaseEditor.editform(self, request, content, mimetype)

        if request.GET.has_key('file'):
            return uploader_form()

        if mimetype == 'text/csv+hbmp':
            return self.render(request, content)

        return BaseEditor.match_edit(self, request, content, mimetype)

    def render(self, req, content, new=False):
        html = """
<html>
<head>
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.3/jquery.min.js"></script>
<script type="text/javascript">
  $(document).ready(function () {
    $("td").click(paint_square);
    $("input[name=brush]")[0].checked = true;
});

%s

</script></head><body>""" % lib_js()

        if new is True:
            html += render_addform(req.GET.get('h'), req.GET.get('w'))

        html += draw(req, content, self.props)
        html += render_controls(some_colors)
        
        html += """
<form method="POST" onsubmit="serialize();">
<input type="hidden" id="resource_body" name="svenweb.resource_body" value="%s"></textarea>
<label for="svenweb.commit_message">Commit message</label>
<input name="svenweb.commit_message"></input>
<input name="svenweb.mimetype" type="hidden" value="text/csv+hbmp" />
<input type="submit" />
</form>
</body></html>""" % (content)

        return Response(html)
