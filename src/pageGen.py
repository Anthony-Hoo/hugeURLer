def pageGen(identifier, url):
    template = ""
    with open('./template/template.html', 'r') as f:
        template = f.read()
    template = template.replace("[/title/]", identifier)
    template = template.replace("[/url/]", url)
    with open('./pages/'+identifier+'.html', 'w') as f:
        f.write(template)
