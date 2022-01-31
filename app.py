from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def index():
    """Returns page with form for madlibs"""
    prompts = story.prompts
    return render_template("main.html",prompts=prompts)

@app.route("/story")
def renderstory():
    """Renders a story with the answers from the form rendered"""
    complete_story = story.generate(request.args)
    return render_template("story.html", complete_story =complete_story)