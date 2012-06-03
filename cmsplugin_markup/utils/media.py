from django.utils.html import escapejs

def content_scripts(scripts):
    output = ""
    for script in scripts:
        output += '<script type="%s" src="%s"></script>' % (script.get('type', 'text/javascript'), script['href'])
    return output

def content_stylesheets(stylesheets):
    output = ""
    for stylesheet in stylesheets:
        output += 'jQuery.loadStyleSheet("%s", "%s");\n' % (escapejs(stylesheet['href']), escapejs(stylesheet.get('type', 'text/css')))
    if output:
        output = '<script type="text/javascript">\n' + output + '</script>\n'
    return output
