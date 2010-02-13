
def parse(content):
    rows = []
    for line in content.split('\n'):
        if not line.strip():
            continue
        row = [i.strip() for i in line.split(',')]
        if rows:
            assert len(row) == len(rows[-1]), \
                "This doesn't look like a valid bitmap; the rows aren't all the same length."
        rows.append(row)
    return rows

def lib_js():
    fp = open('/tmp/hyperbmp/hyperbmp/lib.js')
    data = fp.read()
    fp.close()
    return data

def draw(req, content, props):
    data = parse(content)

    html = """<table style='border: 1px solid black;
              border-collapse: collapse;'>""" 

    for row in data:
        html += "<tr>"
        for item in row:
            item = item.split('>')

            if len(item) == 2:
                item, link = item
            elif len(item) == 1:
                item = item[0]
                link = None

            if not link:
                html += """
<td class='%s' height='%s' width='%s' 
    style='padding: 0; border: 1px solid black; background-color: %s'>
""" % (
                    item,
                    props.pixelheight(req),
                    props.pixelwidth(req),
                    item)
            else:
                html += """
<td href='%s' class='%s' height='%s' width='%s' 
    style='padding: 0; border: 1px solid black; background-color: %s'>
""" % (
                    link,
                    item,
                    props.pixelheight(req),
                    props.pixelwidth(req),
                    item)
                html += "<center><a href='%s'>&nbsp;</a></center>" % link

            html += "&nbsp;</td>"

        html += "</tr>"
    html += "</table>"
    return html

def render_controls(colors):
    form = '\n'.join(["""
<span style='padding:0.25em; background-color: %s'>&nbsp;
  <input type='radio' name='brush' value='%s' />
</span>""" % (value, value)
                      for value in colors])
    
    form += """
<input type='radio' name='brush' value='link' />
<input type='text' id='hyperlink' />"""

    return """
<div id="form" style="padding:1em;">
%s
</div>""" % form

some_colors = ('red','blue','green','white',
               'black','orange','purple','yellow','lightgreen')
