__author__ = 'sargdsra'

from flask import Flask, render_template, request

from src.DATABASE import sign_in, sign_up, followers, followings, posting, get_post_all, get_comment_all, like_post, \
    get_users, dislike_post, commenting

app = Flask(__name__)
app.secret_key = 'amir'


@app.route('/')
def hello():
    return render_template("main-page.html")


@app.route('/auth/signin')
def login():
    return render_template("signin.html")


@app.route('/signup', methods=['POST'])
def signup():
    user = str(request.form['Username'])
    password = str(request.form['Password'])
    rep = str(request.form['Re-password'])
    email = str(request.form['Email'])
    if rep == password and email.count("@") == 1:
        if sign_up(user, password, email):
            return render_template("profile.html", Username=user, followers=0, following=0)
    return render_template("main-page.html")


@app.route('/signin', methods=['POST'])
def signin():
    user = str(request.form['Username'])
    password = str(request.form['Password'])
    if sign_in(user, password):
        follow = len(followers(user))
        followi = len(followings(user))
        posts = fget_post_all(user)
        return render_template("profile.html", Username=user, followers=follow, following=followi, posts=posts)
    return render_template("main-page.html")


@app.route('/auth/signup')
def asign_up():
    return render_template("main-page.html")


@app.route('/post/<string:user>', methods=['POST'])
def fpost(user):
    if posting(user, str(request.form['post_text'])):
        follow = len(followers(user))
        followi = len(followings(user))
        posts = fget_post_all(user)
        return render_template("profile.html", Username=user, followers=follow, following=followi, posts=posts)
    return render_template("main-page.html")


@app.route('/like/<string:user>/<int:pi>', methods=["POST", "GET"])
def flike(user, pi):
    if like_post(pi, user) or get_users(user):
        follow = len(followers(user))
        followi = len(followings(user))
        posts = fget_post_all(user)
        return render_template("profile.html", Username=user, followers=follow, following=followi, posts=posts)
    return render_template("main-page.html")


@app.route('/dlike/<string:user>/<int:pi>', methods=["POST", "GET"])
def fdlike(user, pi):
    if dislike_post(pi, user) or get_users(user):
        follow = len(followers(user))
        followi = len(followings(user))
        posts = fget_post_all(user)
        return render_template("profile.html", Username=user, followers=follow, following=followi, posts=posts)
    return render_template("main-page.html")


@app.route('/cm/<int:pi>/<string:user>', methods=['POST'])
def fcm(pi, user):
    com = str(request.form['comment'])
    if commenting(pi, user, com):
        follow = len(followers(user))
        followi = len(followings(user))
        posts = fget_post_all(user)
        return render_template("profile.html", Username=user, followers=follow, following=followi, posts=posts)
    return render_template("main-page.html")


def fget_post_all(user):
    posts = get_post_all(user)
    followi = followings(user)
    if len(followi) > 0:
        for uf in followi:
            posts += get_post_all(uf)
    posts = fdate_sort(posts)
    for post in posts:
        comments = list(get_comment_all(post[0]))[::-1]
        post.append(len(comments))
        post.append(comments)
        if post[5] == "__empty__":
            post[5] = "../static/pictures/profile-img.jpg"
    print posts
    return posts


def fdate_sort(p):
    pl = [list(i) for i in p]
    for i in range(len(pl)):
        for j in range(0, len(pl) - i - 1):
            if pl[j][6] < pl[j + 1][6]:
                pl[j], pl[j + 1] = pl[j + 1], pl[j]
    return pl


if __name__ == '__main__':
    app.run(debug=True)
