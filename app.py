from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/index.html")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/how-we-do-it")
def how_we_do_it():
    return render_template("how-we-do-it.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/publications")
def publications():
    return render_template("publications.html")

@app.route("/news")
def news():
    return render_template("news.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/gallery-england")
def gallery_england():
    return render_template("gallery-england.html")

@app.route("/gallery-germany")
def gallery_germany():
    return render_template("gallery-germany.html")

@app.route("/gallery-norway")
def gallery_norway():
    return render_template("gallery-norway.html")

@app.route("/gallery-roi")
def gallery_roi():
    return render_template("gallery-roi.html")

@app.route("/gallery-scotland")
def gallery_scotland():
    return render_template("gallery-scotland.html")

@app.route("/gallery-wales")
def gallery_wales():
    return render_template("gallery-wales.html")

@app.route("/case-studies-england")
def case_studies_england():
    return render_template("case-studies-england.html")

@app.route("/case-studies-germany")
def case_studies_germany():
    return render_template("case-studies-germany.html")

@app.route("/case-studies-norway")
def case_studies_norway():
    return render_template("case-studies-norway.html")

@app.route("/case-studies-roi")
def case_studies_roi():
    return render_template("case-studies-roi.html")

@app.route("/case-studies-scotland")
def case_studies_scotland():
    return render_template("case-studies-scotland.html")

@app.route("/case-studies-wales")
def case_studies_wales():
    return render_template("case-studies-wales.html")

if __name__ == "__main__":
    app.run(debug=True)