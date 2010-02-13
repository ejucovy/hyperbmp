from svenweb.edit import BaseEditor
from webob import Response

from hyperbmp.props import RequestProperties
from hyperbmp.lib import parse, lib_js, draw, render_controls, some_colors, render_addform

import mimetypes
mimetypes.add_type('text/csv+hbmp', '.hbmp')

class HbmpEditor(BaseEditor):

    @property
    def props(self):
        return RequestProperties()

    def new(self, request):
        if 'raw' in request.GET:
            return BaseEditor.new(self, request)

        if request.GET.has_key('hbmp'):
            return self.hbmp_new(request)

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

    def match_edit(self, request, content, mimetype):
        if 'raw' in request.GET:
            return BaseEditor.match_edit(self, request, content, mimetype)

        if mimetype == 'text/csv+hbmp':
            return self.hbmp_form
        return BaseEditor.match_edit(self, request, content, mimetype)

    def hbmp_form(self, request, content, mimetype):
        return self.render(request, content)

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
