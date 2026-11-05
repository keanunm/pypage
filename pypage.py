import json
import os
import sys

os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

class RepositioryNotInitiated(Exception):
    pass
RepositioryError_text = "Repository is not initialised. Add 'pypage.init('my project')' to fix it."

class TagError(Exception):
    pass

repository = ""
text_types = ["p", "h1", "h2", "h3", "h4", "h5", "h6"]

def init(name):
    global repository
    repository = name
    data = {}

    data["name"] = name
    data["elements"] = []

    try:
        os.makedirs(f"{repository}")
    except:
        print()
    with open(f"{repository}/main.json", "w") as file:
        json.dump(data, file, indent=4)
    
def set_title(title):
    with open(f"{repository}/main.json", "r") as file:
        data = json.load(file)

    data["name"] = title
    
    with open(f"{repository}/main.json", "w") as file:
        json.dump(data, file, indent=4)


def addtext(text, tag):
    if repository == "":
        raise RepositioryNotInitiated(RepositioryError_text)
    
    if tag not in text_types:
        raise TagError(f"{tag} is not a type of text in HTML.")
    else:
        type_of_text = tag

    with open(f"{repository}/main.json", "r") as file:
        data = json.load(file)

    data["elements"].append({"tag": tag, "text": text})

    with open(f"{repository}/main.json", "w") as file:
        json.dump(data, file, indent=4)

def addimg(link):
    if repository == "":
        raise RepositioryNotInitiated(RepositioryError_text)
    
    with open(f"{repository}/main.json", "r") as file:
        data = json.load(file)
    
    data["elements"].append({"tag": "img", "link": link})
    
    with open(f"{repository}/main.json", "w") as file:
        json.dump(data, file, indent=4)

def addlink(text, link):
    if repository == "":
        raise RepositioryNotInitiated(RepositioryError_text)
        
    with open(f"{repository}/main.json", "r") as file:
        data = json.load(file)
        
    data["elements"].append({"tag": "a", "text": text, "link": link})
        
    with open(f"{repository}/main.json", "w") as file:
        json.dump(data, file, indent=4)




def compile():
    if repository == "":
        raise RepositioryNotInitiated(RepositioryError_text)
    with open(f"{repository}/main.json", "r") as file:
        data = json.load(file)

    body = ""
    for item in data["elements"]:
        tag = item["tag"]
        if tag in text_types:
            text = item["text"]
            body += f"  <{tag}>{text}</{tag}>\n"

        elif tag == "img":
            link = item["link"]
            body += f"  <{tag} src={link}>\n"

        elif tag == "a":
            text = item["text"]
            link = item["link"]
            body += f"  <{tag} href={link}>{text}</{tag}>\n"

    html = f"""<!DOCTYPE html>
<html>
    <head>
        <title>{data["name"]}</title>
    </head>
    <body>
{body}    </body>
</html>"""

    with open(f"{repository}/{repository}.html", "w") as file:
        file.write(html)