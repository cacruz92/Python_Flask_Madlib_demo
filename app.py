from flask import Flask, request, render_template
# from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
# app.config['SECRET_KEY'] = "oh-so-secret"

# debug = DebugToolbarExtension(app)

@app.route("/")
def story_form():
    """Returns Form with questions to fill in Madlib"""
    prompts = story.prompts
    return render_template("questions.html", prompts=prompts)

@app.route("/story")
def generate_story():
    """Returns story from information from the form"""
    text = story.generate(request.args)
    return render_template("story.html", text=text)