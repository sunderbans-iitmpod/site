import os
from flask import Blueprint, render_template, redirect, request
from models import Event

views = Blueprint('views', __name__)

@views.route("/")
def index():
  return render_template("home.html", title="Sundarbans")

@views.route("/bei/")
def bei():
  return render_template("bei.html", title="Backend Interface", msg='', typ='')

@views.route('/bei/', methods=['POST'])
def beipost():
    from post import add_event
    msg = 'Success'
    typ = 'success'

    e_dict = {'title': request.form['title'], 'desc' : request.form['desc'], 'org' : request.form['org'], 'link' : request.form['link'], 'host' : request.form['host'], 'email' : request.form['email']}
    e = Event(e_dict)

    pwd = request.form['pwd']
    beipwd = os.environ['beipwd']
    if pwd != beipwd:
      msg = 'Password is incorrect!'
      typ = 'danger'
    if not e_dict['title']:
      msg = 'Title cannot be empty!'
      typ = 'warning'
    if msg == "Success":
      add_event(e)
    return render_template("bei.html", title="Backend Interface", msg=msg, typ=typ)
    
@views.route('/events/')
def events():
  from fetch import events
  return render_template("events.html", events=events() ,title="Events")

@views.route('/events/capture/')
def capture():
  from fetch import captures
  sharelink="https://site.sunderbanspod.repl.co/capture/"
  sharetext=f"Check out these cool submissions of Photo Capture by Sunderbans House @ {sharelink}"
  return render_template("events/capture.html", captures=captures(), sharetext=sharetext, sharelink=sharelink)

@views.route('/events/photocon/')
def photocon():
  from fetch import photos
  sharelink="https://site.sunderbanspod.repl.co/photocon/"
  sharetext=f"Check out the Sunderbans Photography Competition @ {sharelink}"
  return render_template("photocon.html", photos=photos(), title="Photography Contest", sharetext=sharetext, sharelink=sharelink)

@views.route('/events/logo/')
def logo():
  from fetch import logos
  sharelink="https://site.sunderbanspod.repl.co/logo/"
  sharetext=f"Check out the Sunderbans Logo Competition @ {sharelink}"
  return render_template("logo.html", logos=logos(), title="Logo Contest", sharetext=sharetext, sharelink=sharelink)

@views.route('/about/')
def about():
  return render_template("about.html", title="About")