def pageGen(identifier, url):
    template = ""
    with open("./template/template.html", "r", encoding="utf-8") as f:
        template = f.read()
    template = template.replace("[/title/]", identifier)
    template = template.replace("[/url/]", url)
    with open("./pages/" + identifier + ".html", "w", encoding="utf-8") as f:
        f.write(template)
