__author__ = 'sargdsra'

from flask import Flask, render_template, request

from src.DATABASE import sign_in, sign_up, followers, followings, posting, get_post_all, get_comment_all, like_post, \
    dislike_post, commenting, get_users, get_photo_profile, get_reply_all, like_comment, dislike_comment, like_reply, \
    dislike_reply, replying, edit_post_text, delete_post

import MySQLdb

from mailing_welcom import mailing_welcome

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
    user = MySQLdb.escape_string(request.form['Username'])
    password = MySQLdb.escape_string(request.form['Password'])
    rep = MySQLdb.escape_string(request.form['Re-password'])
    email = MySQLdb.escape_string(request.form['Email'])
    if rep == password and email.count("@") == 1:
        if sign_up(user, password, email):
            mailing_welcome(email, user)
            return render_template("profile.html", Username=user, followers=0, following=0,
                                   pic="http://cdn.persiangig.com/preview/APb8Wef9r4/profile-img.jpg")
    return render_template("main-page.html")


@app.route('/signin', methods=['POST'])
def signin():
    user = MySQLdb.escape_string(request.form['Username'])
    password = MySQLdb.escape_string(request.form['Password'])
    if sign_in(user, password):
        posts = fget_post_all(user)
        return render_template("home.html", posts=posts, Username=user)
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
        p = get_photo_profile(user)
        if p == "__empty__":
            p = "http://cdn.persiangig.com/preview/APb8Wef9r4/profile-img.jpg"
        return render_template("profile.html", Username=user, followers=follow, following=followi, posts=posts, pic=p)
    return render_template("main-page.html")


@app.route('/like/<string:user>/<int:pi>', methods=["POST", "GET"])
def flike(user, pi):
    user = MySQLdb.escape_string(user)
    if like_post(pi, user) or get_photo_profile(user):
        posts = fget_post_all(user)
        return render_template("home.html", posts=posts, Username=user)
    return render_template("main-page.html")


@app.route('/dlike/<string:user>/<int:pi>', methods=["POST", "GET"])
def fdlike(user, pi):
    user = MySQLdb.escape_string(user)
    if dislike_post(pi, user) or get_photo_profile(user):
        posts = fget_post_all(user)
        return render_template("home.html", posts=posts, Username=user)
    return render_template("main-page.html")


@app.route('/cm/<int:pi>/<string:user>', methods=['POST'])
def fcm(pi, user):
    com = MySQLdb.escape_string(request.form['comment'])
    user = MySQLdb.escape_string(user)
    if commenting(pi, user, com):
        posts = fget_post_all(user)
        return render_template("home.html", posts=posts, Username=user)
    return render_template("main-page.html")


@app.route('/h/<string:user>', methods=['POST', 'GET'])
def fhome(user):
    user = MySQLdb.escape_string(user)
    if get_photo_profile(user):
        posts = fget_post_all(user)
        return render_template("home.html", posts=posts, Username=user)
    return render_template("main-page.html")


@app.route('/p/<string:user>', methods=['POST', 'GET'])
def fpro(user):
    user = MySQLdb.escape_string(user)
    if get_photo_profile(user):
        follow = len(followers(user))
        followi = len(followings(user))
        posts = fget_post_all(user)
        p = get_photo_profile(user)
        if p == "__empty__":
            p = "http://cdn.persiangig.com/preview/APb8Wef9r4/profile-img.jpg"
        return render_template("profile.html", Username=user, followers=follow, following=followi, posts=posts, pic=p)
    return render_template("main-page.html")


@app.route('/clike/<string:user>/<int:ci>', methods=['POST', 'GET'])
def fclike(user, ci):
    user = MySQLdb.escape_string(user)
    if like_comment(ci, user) or get_photo_profile(user):
        posts = fget_post_all(user)
        return render_template("home.html", posts=posts, Username=user)
    return render_template("main-page.html")


@app.route('/cdlike/<string:user>/<int:ci>', methods=['POST', 'GET'])
def fcdlike(user, ci):
    user = MySQLdb.escape_string(user)
    if dislike_comment(ci, user) or get_photo_profile(user):
        posts = fget_post_all(user)
        return render_template("home.html", posts=posts, Username=user)
    return render_template("main-page.html")


@app.route('/rlike/<string:user>/<int:ri>', methods=['POST', 'GET'])
def frlike(user, ri):
    user = MySQLdb.escape_string(user)
    if like_reply(ri, user) or get_photo_profile(user):
        posts = fget_post_all(user)
        return render_template("home.html", posts=posts, Username=user)
    return render_template("main-page.html")


@app.route('/rdlike/<string:user>/<int:ri>', methods=['POST', 'GET'])
def frdlike(user, ri):
    user = MySQLdb.escape_string(user)
    if dislike_reply(ri, user) or get_photo_profile(user):
        posts = fget_post_all(user)
        return render_template("home.html", posts=posts, Username=user)
    return render_template("main-page.html")


@app.route('/rep/<int:ci>/<string:user>/<int:pi>', methods=['POST'])
def frep(ci, user, pi):
    rep = MySQLdb.escape_string(request.form['reply'])
    user = MySQLdb.escape_string(user)
    if replying(ci, user, pi, rep):
        posts = fget_post_all(user)
        return render_template("home.html", posts=posts, Username=user)
    return render_template("main-page.html")


@app.route('/ep/<int:pi>/<string:user>', methods=['POST'])
def fedit_p(pi, user):
    np = MySQLdb.escape_string(request.form['new_p'])
    user = MySQLdb.escape_string(user)
    if edit_post_text(pi, np, user):
        posts = fget_post_all(user)
        return render_template("home.html", posts=posts, Username=user)
    return render_template("main-page.html")


@app.route('/dp/<int:pi>/<string:user>', methods=['POST', 'GET'])
def fdel_p(pi, user):
    user = MySQLdb.escape_string(user)
    if delete_post(pi, user):
        posts = fget_post_all(user)
        return render_template("home.html", posts=posts, Username=user)
    return render_template("main-page.html")

def fget_post_all(user):
    user = MySQLdb.escape_string(user)
    posts = get_post_all(user)
    followi = followings(user)
    if len(followi) > 0:
        for uf in followi:
            posts += get_post_all(uf)
    posts = fdate_sort(posts)
    for post in posts:
        comments1 = list(get_comment_all(post[0]))
        comments = [list(i) for i in comments1]
        for comment in comments:
            l = get_photo_profile(comment[2])
            if l == "__empty__":
                l = "http://cdn.persiangig.com/preview/APb8Wef9r4/profile-img.jpg"
            comment.append(l)
            reply1 = list(get_reply_all(comment[0]))
            reply = [list(i) for i in reply1]
            for rep in reply:
                lr = get_photo_profile(rep[2])
                if lr == "__empty__":
                    lr = "http://cdn.persiangig.com/preview/APb8Wef9r4/profile-img.jpg"
                rep.append(lr)
            comment.append(reply)
        post.append(len(comments))
        post.append(comments)
        if post[5] == "__empty__":
            post[5] = "http://cdn.persiangig.com/preview/APb8Wef9r4/profile-img.jpg"
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
