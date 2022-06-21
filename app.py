from urllib.request import urlopen

import yaml
from flask import Flask, render_template, request, redirect

app = Flask(
    __name__,
    template_folder='static'
)

with open("conf.yml", "r") as global_conf_file:
    global_conf = yaml.load(global_conf_file, Loader=yaml.UnsafeLoader)


@app.errorhandler(Exception)
def basic_error(e):
    return render_template(
        'error.html',
        error=
        e,
        url=
        request.url,
        conf=
        global_conf,
        color_bg=
        global_conf['colors']['background'],
        color_fg=
        global_conf['colors']['foreground'],
        color_h=
        global_conf['colors']['heading'],
        color_err=
        global_conf['colors']['text']
    )


@app.route("/robots.txt")
def robots():
    return "User-Agent: * Disallow: /"


@app.route("/")
def git():
    return redirect("https://github.com/ihatethefrench/pronounce")


@app.route("/<username>")
def root(username):
    with urlopen(f"{global_conf['user-url']}".replace("{username}", f"{username}")) as data:
        yml = data.read().decode('utf-8')
        conf = yaml.load(yml, Loader=yaml.FullLoader)
        print(conf)
    if conf['colors']['background'].startswith("http"):
        bg = "url(" + conf['colors']['background'] + ") center center/cover no-repeat"
    else:
        bg = conf['colors']['background']
    return render_template(
        'index.html',
        color_bg=
        bg,
        color_fg=
        conf.get("colors", {}).get("foreground", global_conf['colors']['foreground']),
        color_name=
        conf.get("colors", {}).get("name", global_conf['colors']['heading']),
        color_info=
        conf.get("colors", {}).get("info", global_conf['colors']['text']),
        color_url=
        conf.get("colors", {}).get("url", {}).get("normal", global_conf['colors']['url']['normal']),
        color_url_hover=
        conf.get("colors", {}).get("url", {}).get("hover", global_conf['colors']['url']['hover']),
        title=
        conf.get("title", global_conf['title'].replace("{username}", f"{username}")),
        icon=
        conf.get("icon", global_conf['icon']),
        name=
        conf['name'],
        age=
        conf.get("age", ""),
        pronouns=
        ", ".join(
            conf['pronouns']
        ),
        contacts=
        conf['contacts'],
        urls=
        conf['urls']
    )
