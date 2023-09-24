from flask import Flask, render_template
from post import Post

post_class = Post()

app = Flask(__name__)

@app.route('/URL/post/<int:id>')
def blog_post(id):
    return render_template("post.html",post = post_class.all_posts[id-1])

@app.route('/')
def home():
    return render_template("index.html",posts = post_class.all_posts)

    

if __name__ == "__main__":
    app.run(debug=True)
