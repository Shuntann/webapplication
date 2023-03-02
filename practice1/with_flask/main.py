from with_flask import app
from flask import render_template


@app.route("/home/")
def home():
    return render_template(
        "home.html"
    )

@app.route("/about/")
def about():
    return render_template(
        "about.html"
    )

@app.route("/menu/")
def menu():
    menus =[
        {"name":"バナナとキャラメルのタルト",
         "price":400,
         "description":"バナナとソテーをキャラメルクリームで絡めたフィリングがたっぷり"
        }
        {"name":"アプリコットのタルト",
         "price":400,
         "description":"アプリコットのコンポートとカスタードの愛称が抜群"
        }
        {
        "name":"焼リンゴのタルト",
        "price":400,
        "description":"たっぷりのはちみつとバターで焼き上げたリンゴにシナモンをきかせて",
        
        }
    ]
    
    return render_template(
        "menu.html",menus=menus
    )

@app.route("/menu2/")
def menu2():
    return render_template(
        "menu2.html"
    )

@app.route("/menu3/")
def menu3():
    return render_template(
        "menu3.html"
    )

@app.route("/access/")
def access():
    return render_template(
        "access.html"
    )


@app.route("/contact/")
def contact():
    return render_template(
        "contact.html"
    )

@app.route("/result/")
def result():
    return render_template(
        "result.html"
    )
