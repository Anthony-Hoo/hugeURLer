from os import mkdir


def page_gen(identifier, url):
    with open("./template/template.html", "r", encoding="utf-8") as f:
        template = f.read()
    template = template.replace("[/title/]", identifier)
    template = template.replace("[/url/]", url)
    mkdir("./pages/" + identifier)
    with open("./pages/" + identifier + "/index.html", "w", encoding="utf-8") as f:
        f.write(template)
