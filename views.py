from flask import Blueprint, render_template, redirect

views = Blueprint('views', __name__)

@views.route("/")
def index():
  return redirect("digart")
	
@views.route('/login/')
def login():
  return render_template("login.html", title="Login")

@views.route('/about/')
def about():
  return render_template("about.html", title="About")
  
@views.route('/logo/')
def logo():
  from fetch import logos
  sharelink="https://site.sunderbanspod.repl.co/logo/"
  sharetext=f"Check out the Sunderbans Logo Competition @ {sharelink}"
  return render_template("logo.html", logos=logos(), title="Logo Contest", sharetext=sharetext, sharelink=sharelink)
    
@views.route('/photocon/')
def photocon():
  from fetch import photocon
  sharelink="https://site.sunderbanspod.repl.co/photocon/"
  sharetext=f"Check out the Sunderbans Photography Competition @ {sharelink}"
  return render_template("photocon.html", photos=photocon(), title="Photography Contest", sharetext=sharetext, sharelink=sharelink)
    
@views.route('/digart/')
def digart():
  from fetch import digart
  sharelink="https://site.sunderbanspod.repl.co/digart/"
  sharetext=f"Check out the Sunderbans Digital Art Competition @ {sharelink}"
  return render_template("digart.html", photos=digart(), title="Digital Art Contest", sharetext=sharetext, sharelink=sharelink)
    
@views.route('/events/')
def events():
  from fetch import events
  return render_template("events.html", events=events() ,title="Events")
  