# -*- coding: utf-8 -*-
__author__ = 'sargdsra'

from flask import Flask, render_template, request, redirect, url_for, session, json

from werkzeug import secure_filename

from src.DATABASE import sign_in, sign_up, followers, followings, posting, get_post_all, get_comment_all, like_post, \
    dislike_post, commenting, get_users, get_photo_profile, get_reply_all, like_comment, dislike_comment, like_reply, \
    dislike_reply, replying, edit_post_text, delete_post, update_password, forget_pass_user, follow, photo_profile, \
    unfollow, photo_post, un_subscribe, get_link, put_link

import MySQLdb

from mailing_welcom import mailing_welcome
from forget_password import forget_pass
from django.utils.encoding import smart_str

import os

app = Flask(__name__)
app.secret_key = 'amir'
app.config['UPLOAD_FOLDER'] = 'static/pics/'


@app.route('/')
def hello():
    session.clear()
    return render_template("main-page.html")


@app.route('/auth/signin')
def login():
    return render_template("signin.html")


@app.route('/signup', methods=['POST'])
def signup():
    user = MySQLdb.escape_string(smart_str(request.form['Username']))
    password = MySQLdb.escape_string(smart_str(request.form['Password']))
    rep = MySQLdb.escape_string(smart_str(request.form['Re-password']))
    email = MySQLdb.escape_string(smart_str(request.form['Email']))
    if rep == password and email.count("@") == 1:
        if sign_up(user, password, email):
            mailing_welcome(email, user)
            return render_template("home.html", posts=[], Username=user)
    return render_template("main-page.html")


@app.route('/signin', methods=['POST'])
def signin():
    user = MySQLdb.escape_string(smart_str(request.form['Username']))
    password = MySQLdb.escape_string(smart_str(request.form['Password']))
    if sign_in(user, password):
        posts = fget_post_all(user)
        return render_template("home.html", posts=posts, Username=user)
    return render_template("main-page.html")


@app.route('/auth/signup')
def asign_up():
    return render_template("main-page.html")


@app.route('/unfollow', methods=['POST'])
def fun():
    user = MySQLdb.escape_string(smart_str(request.form['user']))
    unf = MySQLdb.escape_string(smart_str(request.form['unf']))
    if unfollow(user, unf):
        posts = fget_post_all(user)
        return render_template("home.html", posts=posts, Username=user)
    return render_template("main-page.html")


@app.route('/post', methods=['POST'])
def fpost():
    post = MySQLdb.escape_string(smart_str(request.form['post_text']))
    user = MySQLdb.escape_string(smart_str(request.form['user']))
    lv = MySQLdb.escape_string(smart_str(request.form['lvalue']))
    la = MySQLdb.escape_string(smart_str(request.form['ladr']))
    pic = request.files['file']
    if pic:
        ur = secure_filename(pic.filename)
        if '.' not in ur:
            ur = "." + ur
        if len(get_post_all(user)) > 0:
            ur = str(get_post_all(user)[-1][0] + 1) + ur
        else:
            ur = "1" + ur
        pic.save(os.path.join(app.config['UPLOAD_FOLDER'], ur))
        ur = "pics/" + ur
    else:
        ur = "__empty__"
    if posting(user, MySQLdb.escape_string(post), ur):
        if la:
            if la[:7] != "http://":
                la = "http://" + la
            pi = int(get_post_all(user)[-1][0])
            if lv:
                put_link(pi, la, lv)
            else:
                put_link(pi, la)
        session['user'] = user
        return redirect(url_for("hom"))


@app.route('/ep', methods=['POST'])
def fedit_p():
    np = MySQLdb.escape_string(smart_str(request.form['new_p']))
    user = MySQLdb.escape_string(smart_str(request.form['user']))
    pi = int(request.form['post'])
    pic = request.files['file']
    if pic:
        ur = secure_filename(pic.filename)
        if '.' not in ur:
            ur = "." + ur
        ur = str(pi + 1) + ur
        pic.save(os.path.join(app.config['UPLOAD_FOLDER'], ur))
        ur = "pics/" + ur
        if photo_post(pi, ur, user):
            if edit_post_text(pi, np, user):
                session['user'] = user
                return redirect(url_for("hom"))
    else:
        if edit_post_text(pi, np, user):
            session['user'] = user
            return redirect(url_for("hom"))


@app.route('/change_piic', methods=['POST'])
def chiip():
    user = MySQLdb.escape_string(smart_str(request.form['user']))
    pic = request.files['file']
    if pic:
        ur = secure_filename(pic.filename)
        if '.' not in ur:
            ur = "." + ur
        ur = str(user) + ur
        pic.save(os.path.join(app.config['UPLOAD_FOLDER'], ur))
        ur = "pics/" + ur
    if photo_profile(user, ur):
        session['user'] = user
        return redirect(url_for("hom"))


@app.route('/hp')
def hom():
    try:
        user = session['user']
    except:
        return render_template("main-page.html")
    posts = fget_post_all(user)
    return render_template("home.html", posts=posts, Username=user)


@app.route('/li', methods=["POST", "GET"])
def send_i():
    if request.method == 'POST':
        inf = MySQLdb.escape_string(smart_str(request.form['inf']))
        session['inf'] = inf
        return '1'
    return render_template("main-page.html")


@app.route('/gpu')
def fgpu():
    try:
        inf = session['inf']
    except:
        return render_template("main-page.html")
    inf1 = inf.split('/')
    user = inf1[0]
    ouser = (inf1[1])
    follow = len(followers(ouser))
    followi = len(followings(ouser))
    posts = foget_post_all(ouser)
    p = get_photo_profile(ouser)
    if p == "__empty__":
        p = "pictures/profile-img.jpg"
    friends = fsearch("", user)
    return render_template("other-profile.html", Username=user, OUsername=ouser, Ofollowers=follow, Ofollowing=followi,
                           posts=posts, pic=p, friends=friends)


@app.route('/like')
def flike():
    try:
        inf = session['inf']
    except:
        return render_template("main-page.html")
    inf1 = inf.split('/')
    user = inf1[0]
    pi = int(inf1[1])
    if like_post(pi, user) or get_photo_profile(user):
        posts = fget_post_all(user)
        return render_template("home.html", posts=posts, Username=user)
    return render_template("main-page.html")


@app.route('/dlike')
def fdlike():
    try:
        inf = session['inf']
    except:
        return render_template("main-page.html")
    inf1 = inf.split('/')
    user = inf1[0]
    pi = int(inf1[1])
    if dislike_post(pi, user) or get_photo_profile(user):
        posts = fget_post_all(user)
        return render_template("home.html", posts=posts, Username=user)
    return render_template("main-page.html")


@app.route('/clike')
def fclike():
    try:
        inf = session['inf']
    except:
        return render_template("main-page.html")
    inf1 = inf.split('/')
    user = inf1[0]
    ci = int(inf1[1])
    if like_comment(ci, user) or get_photo_profile(user):
        posts = fget_post_all(user)
        return render_template("home.html", posts=posts, Username=user)
    return render_template("main-page.html")


@app.route('/cdlike')
def fcdlike():
    try:
        inf = session['inf']
    except:
        return render_template("main-page.html")
    inf1 = inf.split('/')
    user = inf1[0]
    ci = int(inf1[1])
    if dislike_comment(ci, user) or get_photo_profile(user):
        posts = fget_post_all(user)
        return render_template("home.html", posts=posts, Username=user)
    return render_template("main-page.html")


@app.route('/rlike')
def frlike():
    try:
        inf = session['inf']
    except:
        return render_template("main-page.html")
    inf1 = inf.split('/')
    user = inf1[0]
    ri = int(inf1[1])
    if like_reply(ri, user) or get_photo_profile(user):
        posts = fget_post_all(user)
        return render_template("home.html", posts=posts, Username=user)
    return render_template("main-page.html")


@app.route('/rdlike')
def frdlike():
    try:
        inf = session['inf']
    except:
        return render_template("main-page.html")
    inf1 = inf.split('/')
    user = inf1[0]
    ri = int(inf1[1])
    if dislike_reply(ri, user) or get_photo_profile(user):
        posts = fget_post_all(user)
        return render_template("home.html", posts=posts, Username=user)
    return render_template("main-page.html")


@app.route('/h', methods=['POST', 'GET'])
@app.route('/p', methods=['POST', 'GET'])
@app.route('/change_p', methods=['POST', 'GET'])
@app.route('/change_pic', methods=['POST', 'GET'])
@app.route('/re', methods=['POST', 'GET'])
@app.route('/dea', methods=['POST', 'GET'])
def send_user():
    if request.method == 'POST':
        user = MySQLdb.escape_string(smart_str(request.form['username']))
        session['user'] = user
        return '1'
    return render_template("main-page.html")


@app.route('/cm', methods=['POST'])
def fcm():
    com = MySQLdb.escape_string(smart_str(request.form['comment']))
    user = MySQLdb.escape_string(smart_str(request.form['user']))
    pi = int(request.form['post'])
    if commenting(pi, user, com):
        posts = fget_post_all(user)
        return render_template("home.html", posts=posts, Username=user)
    return render_template("main-page.html")


@app.route('/home')
def ffhome():
    try:
        user = session['user']
    except:
        return render_template("main-page.html")
    posts = fget_post_all(user)
    return render_template("home.html", posts=posts, Username=user)


@app.route('/pro')
def ffpro():
    try:
        user = session['user']
    except:
        return render_template("main-page.html")
    if get_photo_profile(user):
        follow = len(followers(user))
        followi = len(followings(user))
        posts = foget_post_all(user)
        p = get_photo_profile(user)
        if p == "__empty__":
            p = "pictures/profile-img.jpg"
        friends = fsearch("", user)
        return render_template("profile.html", Username=user, followers=follow, following=followi, posts=posts, pic=p,
                               friends=friends)
    return render_template("main-page.html")


@app.route('/chp')
def cp():
    try:
        user = session['user']
    except:
        return render_template("main-page.html")
    return render_template("reset-password.html", Username=user)


@app.route('/fdea')
def ffdea():
    try:
        user = session['user']
    except:
        return render_template("main-page.html")
    return render_template("unsubscribe.html", Username=user)


@app.errorhandler(500)
def erh():
    return render_template("main-page.html")


@app.route('/chpi')
def cpi():
    try:
        user = session['user']
    except:
        return render_template("main-page.html")
    l = get_photo_profile(user)
    if l == "__empty__":
        l = "pictures/profile-img.jpg"
    return render_template("change_pic.html", Username=user, pic=l)


@app.route('/rel')
def frel():
    try:
        user = session['user']
    except:
        return render_template("main-page.html")
    followerss1 = followers(user)
    followerss = []
    if followerss1:
        for i in range(len(followerss1)):
            followerss.append([followerss1[i]])
        for item in followerss:
            l = get_photo_profile(item[0])
            if l == "__empty__":
                l = "pictures/profile-img.jpg"
            item.append(l)
    else:
        followerss = followerss1
    followingss1 = followings(user)
    followingss = []
    if followingss1:
        for i in range(len(followingss1)):
            followingss.append([followingss1[i]])
        for item in followingss:
            l = get_photo_profile(item[0])
            if l == "__empty__":
                l = "pictures/profile-img.jpg"
            item.append(l)
    else:
        followingss = followingss1
    return render_template("follow.html", Username=user, fer=followerss, fing=followingss)


@app.route('/rep', methods=['POST'])
def frep():
    rep = MySQLdb.escape_string(smart_str(request.form['reply']))
    user = MySQLdb.escape_string(smart_str(request.form['user']))
    pi = int(request.form['post'])
    ci = int(request.form['comment'])
    if replying(ci, user, pi, rep):
        posts = fget_post_all(user)
        return render_template("home.html", posts=posts, Username=user)
    return render_template("main-page.html")


@app.route('/dp', methods=['GET'])
def fdel_p():
    user = MySQLdb.escape_string(smart_str(request.args.get('user')))
    pi = int(request.args.get('post'))
    if delete_post(pi, user):
        posts = fget_post_all(user)
        return render_template("home.html", posts=posts, Username=user)
    return render_template("main-page.html")


@app.route('/change_pass', methods=['POST'])
def ch_pass():
    user = MySQLdb.escape_string(smart_str(request.form['Username']))
    b_pass = MySQLdb.escape_string(smart_str(request.form['opass']))
    n_pass = MySQLdb.escape_string(smart_str(request.form['npass']))
    cn_pass = MySQLdb.escape_string(smart_str(request.form['cnpass']))
    if cn_pass == n_pass:
        if update_password(user, b_pass, n_pass):
            posts = fget_post_all(user)
            return render_template("home.html", posts=posts, Username=user)
    return render_template("main-page.html")


@app.route('/fp')
def ffp():
    return render_template("forget-pass.html")


@app.route('/mail_p', methods=['POST'])
def mail_pass():
    user = MySQLdb.escape_string(smart_str(request.form['Username']))
    inf = forget_pass_user(smart_str(user))
    if inf:
        forget_pass(inf[2], inf[0], inf[1])
    return render_template("main-page.html")


@app.route('/end', methods=['POST'])
def uned():
    user = MySQLdb.escape_string(smart_str(request.form['user']))
    passw = MySQLdb.escape_string(smart_str(request.form['pass']))
    un_subscribe(user, passw)
    return render_template("main-page.html")


@app.route("/follow", methods=['POST'])
def ffolo():
    user = MySQLdb.escape_string(smart_str(request.form['user']))
    fo = MySQLdb.escape_string(smart_str(request.form['friend']))
    follow(user, fo)
    posts = fget_post_all(user)
    return render_template("home.html", posts=posts, Username=user)


@app.route("/search", methods=['POST'])
def ffs():
    s = MySQLdb.escape_string(smart_str(request.form['search']))
    user = MySQLdb.escape_string(smart_str(request.form['user']))
    follow = len(followers(user))
    followi = len(followings(user))
    posts = foget_post_all(user)
    p = get_photo_profile(user)
    if p == "__empty__":
        p = "pictures/profile-img.jpg"
    friends = fsearch(s, user)
    return render_template("profile.html", Username=user, followers=follow, following=followi, posts=posts, pic=p,
                           friends=friends)


def fget_post_all(user):
    user = MySQLdb.escape_string(smart_str(user))
    posts = get_post_all(user)
    followi = followings(user)
    if len(followi) > 0:
        for uf in followi:
            posts += get_post_all(uf)
    posts = fdate_sort(posts)
    for post in posts:
        pi = int(post[0])
        lin = get_link(pi)
        il = get_photo_profile(post[1])
        comments1 = list(get_comment_all(post[0]))
        comments = [list(i) for i in comments1]
        for comment in comments:
            l = get_photo_profile(comment[2])
            if l == "__empty__":
                l = "pictures/profile-img.jpg"
            comment.append(l)
            reply1 = list(get_reply_all(comment[0]))
            reply = [list(i) for i in reply1]
            for rep in reply:
                lr = get_photo_profile(rep[2])
                if lr == "__empty__":
                    lr = "pictures/profile-img.jpg"
                rep.append(lr)
            comment.append(reply)
        post.append(len(comments))
        post.append(comments)
        if il == "__empty__":
            il = "pictures/profile-img.jpg"
        post.append(il)
        if lin:
            post.append(str(lin[0][1]))
            post.append(str(lin[0][2]))
        if post[5] == "__empty__":
            post[5] = ""
    return posts


def foget_post_all(user):
    user = MySQLdb.escape_string(smart_str(user))
    posts = get_post_all(user)
    posts = fdate_sort(posts)
    for post in posts:
        pi = int(post[0])
        lin = get_link(pi)
        il = get_photo_profile(post[1])
        comments1 = list(get_comment_all(post[0]))
        comments = [list(i) for i in comments1]
        for comment in comments:
            l = get_photo_profile(comment[2])
            if l == "__empty__":
                l = "pictures/profile-img.jpg"
            comment.append(l)
            reply1 = list(get_reply_all(comment[0]))
            reply = [list(i) for i in reply1]
            for rep in reply:
                lr = get_photo_profile(rep[2])
                if lr == "__empty__":
                    lr = "pictures/profile-img.jpg"
                rep.append(lr)
            comment.append(reply)
        post.append(len(comments))
        post.append(comments)
        if il == "__empty__":
            il = "pictures/profile-img.jpg"
        post.append(il)
        if lin:
            post.append(str(lin[0][1]))
            post.append(str(lin[0][2]))
        if post[5] == "__empty__":
            post[5] = ""
    return posts


def fdate_sort(p):
    pl = [list(i) for i in p]
    for i in range(len(pl)):
        for j in range(0, len(pl) - i - 1):
            if pl[j][6] < pl[j + 1][6]:
                pl[j], pl[j + 1] = pl[j + 1], pl[j]
    return pl


def fsearch(st, user):
    search_res = get_users(st)
    search_re = [list(i) for i in search_res]
    folo = followings(user)
    i = 0
    sea = []
    while i < len(search_re):
        if not search_re[i][0] in folo and not search_re[i][0] == user:
            sea.append(search_re[i])
        i = i + 1
    for item in sea:
        if item[1] == '__empty__':
            item[1] = "pictures/profile-img.jpg"
    return sea


if __name__ == '__main__':
    app.run(debug=True, port=4958)
