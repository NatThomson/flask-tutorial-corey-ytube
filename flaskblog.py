from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'nobody mcnobody',
        'title': 'I couldnt think of a title',
        'content': 'dummy content post',
        'date_posted': 'March 1, 2022'
    },
    {
        'author': 'who what who',
        'title': 'still no title',
        'content': 'another dummy content post',
        'date_posted': 'May 5, 2022'
    }
]

@app.route("/")
def hello():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html')



if __name__ == '__main__':
    app.run(debug=True)