from jinja2 import Environment, PackageLoader, select_autoescape
import os, webbrowser
env = Environment(
    loader=PackageLoader("html_gen"),
    autoescape=select_autoescape()
    )

template = env.get_template("output.html")

def html_gen(data):
    
    with open("output.html", "wb") as f:
        content = template.render(array=data)
        f.write(content.encode("utf-8"))
    new = 2
    path = os.getcwd()
    url = f"file://{path}\output.html"
    webbrowser.open(url,new=new)