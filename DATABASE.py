# -*- coding: utf-8 -*-
#############
#DB         #
#IRSN       #
#############


"""
sign_up(username, password, email, photo="__empty__")                     for sign up

sign_in(username, password)                                               for sign in

photo_profile(username, photo)                                            inserting photo for profile

get_photo_profile(username)                                               accessing profile's photo

un_subscribe(username, password)                                          to delete account

update_password(username, password, new_pass)                             for changing password

posting(username_post, post, photo="__empty__")                           for inserting post

get_post(post_id)                                                         for accessing post

check_like_post(likepost, like_user)                                      for checking if liked or not in posts

like_inserter_post(likepost, like_user)                                   for inserting relation of like of posts in table

like_post(post_id, like_user)                                             adding point to like for post

dislike_post(post_id, like_user)                                          adding point to dislike for post

get_like_post(post_id)                                                    to get number of likes for post

get_dislike_post(post_id)                                                 to get number of dislikes for post

photo_post(post_id, photo, username_post)                                 inserting photo for post

edit_post_text(post_id, new_post, username_post)                          editing post

delete_post(post_id, username_post)                                       to delete a post

like_post_calculator(post_id)                                             sum of likes and dislikes

commenting(comment_post, comment_username, comment)                       to insert comment

get_comment(comment_id)                                                   accessing comment

check_like_comment(like_com, like_user)                                   for checking if liked or not in comments

like_inserter_comment(like_com, like_user)                                for inserting relation of like of comments in table

like_comment(comment_id, like_user)                                       adding point to like for comments

dislike_comment(comment_id, like_user)                                    adding point to dislike for comments

get_like_comment(comment_id)                                              to get number of likes for comment

get_dislike_comment(comment_id)                                           to get number of dislikes for comment

like_cm_calculator(comment_id)                                            sum of likes and dislikes

replying(reply_comment, reply_username, reply_post, reply)                to insert comment

get_reply(reply_id)                                                       accessing comment

check_like_reply(like_re, like_user)                                      for checking if liked or not in comments

like_inserter_reply(like_re, like_user)                                   for inserting relation of like of comments in table

like_reply(reply_id, like_user)                                           adding point to like for comments

dislike_reply(reply_id, like_user)                                        adding point to dislike for comments

get_like_reply(reply_id)                                                  to get number of likes for post

get_dislike_reply(reply_id)                                               to get number of dislikes for post

like_re_calculator(reply_id)                                              sum of likes and dislikes

follow(follower, followed)                                                for following a user

unfollow(follower, followed)                                              to un_follow

followers(followed)                                                       to get followers

followings(follower)                                                      to get followings

get_post_all(username_post)                                               return all posts with specific user

get_comment_all(comment_post)                                             return all comments with specific post

get_reply_all(reply_comment)                                              return all replys with specific comment

get_users(pattern)                                                        return all users with specific pattern

forget_pass_user(username)                                                return username password and email in case of forget_pass

IMPORTANT NOTE:
    likepost
    comment_post
    reply_comment
    like_re
    reply_post
    like_com
    and arguments which have _id
    are INT
    others are STRING
"""


import MySQLdb
from django.utils.encoding import smart_str

def sign_up(username, password, email, photo="__empty__"):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql = "INSERT INTO users VALUES ('%s' , '%s', '%s', '%s')" % (username, password, email, photo)
    flag = False
    try:
        cursor.execute(sql)
        db.commit()
        flag = True
    except:
        db.rollback()
        print "invalid user or pass"
        flag = False
    db.close()
    if flag == True:
        return True
    else:
        return False


def sign_in(username, password):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql = "SELECT username,password FROM users WHERE username = '%s' AND password = '%s'" % (username, password)
    try:
        cursor.execute(sql)
        data = cursor.fetchone()
        db.commit()
    except:
        db.rollback()
        print "invalid user or pass"
    db.close()
    try:
        if data[0] == username and data[1] == password:
            return True
        else:
            return False
    except:
        return False


def photo_profile(username, photo):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql = "UPDATE users SET photo = '%s' WHERE username = '%s'" % (photo, username)
    flag = False
    try:
        cursor.execute(sql)
        db.commit()
        flag = True
    except:
        db.rollback()
        print "invalid user"
        flag = False
    db.close()
    if flag == True:
        return True
    else:
        return False


def get_photo_profile(username):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql = "SELECT photo FROM users WHERE username = '%s'" % username
    try:
        cursor.execute(sql)
        data = cursor.fetchone()
        db.commit()
    except:
        db.rollback()
        print "invalid id"
        return False
    db.close()
    try:
        return data[0]
    except:
        return False


def un_subscribe(username, password):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql = "DELETE FROM users WHERE username = '%s' AND password = '%s'" % (username, password)
    flag = False
    try:
        cursor.execute(sql)
        db.commit()
        flag = True
    except:
        db.rollback()
        print "invalid id"
        flag = False
    db.close()
    if flag == True:
        return True
    else:
        return False


def update_password(username, password, new_pass):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql = "SELECT password FROM users WHERE username = '%s'" % username
    flag = False
    try:
        cursor.execute(sql)
        data = cursor.fetchone()
        db.commit()
        flag = True
    except:
        db.rollback()
        print "invalid user or pass"
        flag = False
        db.close()
        return False
    if data[0] != password:
        return False
    sql = "UPDATE users SET password = '%s' WHERE username = '%s'" % (new_pass, username)
    try:
        cursor.execute(sql)
        db.commit()
        flag = True
    except:
        db.rollback()
        print "invalid user"
        flag = False
    db.close()
    if flag == True:
        return True
    else:
        return False


def posting(username_post, post, photo="__empty__"):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql = "INSERT INTO posts (username_post,post,date_mod,photo_post) VALUES ('%s' , '%s', NOW(), '%s')" % (username_post, post.decode('utf-8'), photo)
    flag = False
    try:
        cursor.execute(sql)
        db.commit()
        flag = True
    except:
        db.rollback()
        print "invalid user or pass"
        flag = False
    db.close()
    if flag == True:
        return True
    else:
        return False


def get_post(post_id):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql = "SELECT post FROM posts WHERE post_id = '%d'" % post_id
    try:
        cursor.execute(sql)
        data = cursor.fetchone()
        db.commit()
    except:
        db.rollback()
        print "invalid id"
    db.close()
    try:
        return data[0]
    except:
        return False


def get_post_all(username_post):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql = "SELECT * FROM posts WHERE username_post = '%s'" % username_post
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        db.commit()
    except:
        db.rollback()
        print "invalid id"
    db.close()
    try:
        return data
    except:
        return False


def check_like_post(likepost, like_user):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql = "SELECT * FROM likepost WHERE like_post = '%d' AND like_user = '%s' " % (likepost, like_user)
    try:
        cursor.execute(sql)
        data = cursor.fetchone()
        db.commit()
    except:
        db.rollback()
        print "invalid id"
    db.close()
    if data == None:
        return True
    else:
        return False


def like_inserter_post(likepost, like_user):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    flag = False
    if check_like_post(likepost, like_user):
        sql = "INSERT INTO likepost VALUES ('%d', '%s')" % (likepost, like_user)
        flag = False
        try:
            cursor.execute(sql)
            db.commit()
            flag = True
        except:
            db.rollback()
            print "invalid user or id"
            flag = False
        db.close()
    if flag == True:
        return True
    else:
        return False


def like_post(post_id, like_user):
    if check_like_post(post_id, like_user) == False:
        return False
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql = "SELECT likes FROM posts WHERE post_id = '%d'" % post_id
    try:
        cursor.execute(sql)
        data = cursor.fetchone()
        db.commit()
    except:
        db.rollback()
        print "invalid id"
        db.close()
        return False
    sql = "UPDATE posts SET likes = '%d' WHERE post_id = '%d'" % (data[0]+1, post_id)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print "cannot like"
        return False
    db.close()
    like_inserter_post(post_id, like_user)
    return data[0] + 1


def dislike_post(post_id, like_user):
    if check_like_post(post_id, like_user) == False:
        return False
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql = "SELECT dislikes FROM posts WHERE post_id = '%d'" % post_id
    try:
        cursor.execute(sql)
        data = cursor.fetchone()
        db.commit()
    except:
        db.rollback()
        print "invalid id"
        db.close()
        return False
    sql = "UPDATE posts SET dislikes = '%d' WHERE post_id = '%d'" % (data[0]+1, post_id)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print "cannot dislike"
        return False
    db.close()
    like_inserter_post(post_id, like_user)
    return data[0] + 1


def get_like_post(post_id):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql = "SELECT likes FROM posts WHERE post_id = '%d'" % post_id
    try:
        cursor.execute(sql)
        data = cursor.fetchone()
        db.commit()
    except:
        db.rollback()
        print "invalid id"
        return False
    db.close()
    return data[0]


def get_dislike_post(post_id):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql = "SELECT dislikes FROM posts WHERE post_id = '%d'" % post_id
    try:
        cursor.execute(sql)
        data = cursor.fetchone()
        db.commit()
    except:
        db.rollback()
        print "invalid id"
        return False
    db.close()
    return data[0]


def photo_post(post_id, photo, username_post):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql = "UPDATE posts SET photo_post = '%s',date_mod = NOW() WHERE post_id = '%d' AND username_post = '%s'" % (photo, post_id, username_post)
    flag = False
    try:
        cursor.execute(sql)
        db.commit()
        flag = True
    except:
        db.rollback()
        print "invalid id"
        flag = False
    db.close()
    if flag == True:
        return True
    else:
        return False


def edit_post_text(post_id, new_post, username_post):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql = "UPDATE posts SET post = '%s',date_mod = NOW() WHERE post_id = '%d' AND username_post = '%s'" % (new_post, post_id, username_post)
    flag = False
    try:
        cursor.execute(sql)
        db.commit()
        flag = True
    except:
        db.rollback()
        print "invalid id"
        flag = False
    db.close()
    if flag == True:
        return True
    else:
        return False


def delete_post(post_id, username_post):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql = "DELETE FROM posts WHERE post_id = '%d' AND username_post = '%s'" % (post_id, username_post)
    flag = False
    try:
        cursor.execute(sql)
        db.commit()
        flag = True
    except:
        db.rollback()
        print "invalid id"
        flag = False
    db.close()
    if flag == True:
        return True
    else:
        return False


def like_post_calculator(post_id):
    return get_like_post(post_id) - get_dislike_post(post_id)


def commenting(comment_post, comment_username, comment):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql = "INSERT INTO comments (comment_post,comment_username,comment,comment_date) VALUES ('%d' , '%s', '%s', NOW())" % (comment_post, comment_username, comment.decode('utf-8'))
    flag = False
    try:
        cursor.execute(sql)
        db.commit()
        flag = True
    except:
        db.rollback()
        print "invalid user or pass"
        flag = False
    db.close()
    if flag == True:
        return True
    else:
        return False


def get_comment(comment_id):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql = "SELECT comment FROM comments WHERE comment_id = '%d'" % comment_id
    try:
        cursor.execute(sql)
        data = cursor.fetchone()
        db.commit()
    except:
        db.rollback()
        print "invalid id"
    db.close()
    try:
        return data[0]
    except:
        return False


def get_comment_all(comment_post):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql = "SELECT * FROM comments WHERE comment_post = '%d'" % comment_post
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        db.commit()
    except:
        db.rollback()
        print "invalid id"
    db.close()
    try:
        return data
    except:
        return False


def check_like_comment(like_com, like_user):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql = "SELECT * FROM like_cm WHERE like_com = '%d' AND like_user = '%s' " % (like_com, like_user)
    try:
        cursor.execute(sql)
        data = cursor.fetchone()
        db.commit()
    except:
        db.rollback()
        print "invalid id"
    db.close()
    if data == None:
        return True
    else:
        return False


def like_inserter_comment(like_com, like_user):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    flag = False
    if check_like_comment(like_com, like_user):
        sql = "INSERT INTO like_cm VALUES ('%d', '%s')" % (like_com, like_user)
        flag = False
        try:
            cursor.execute(sql)
            db.commit()
            flag = True
        except:
            db.rollback()
            print "invalid user or id"
            flag = False
        db.close()
    if flag == True:
        return True
    else:
        return False


def like_comment(comment_id, like_user):
    if check_like_comment(comment_id, like_user) == False:
        return False
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql = "SELECT like_cm FROM comments WHERE comment_id = '%d'" % comment_id
    try:
        cursor.execute(sql)
        data = cursor.fetchone()
        db.commit()
    except:
        db.rollback()
        print "invalid id"
        db.close()
        return False
    sql = "UPDATE comments SET like_cm = '%d' WHERE comment_id = '%d'" % (data[0]+1, comment_id)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print "cannot like"
        return False
    db.close()
    like_inserter_comment(comment_id, like_user)
    return data[0] + 1


def dislike_comment(comment_id, like_user):
    if check_like_comment(comment_id, like_user) == False:
        return False
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql = "SELECT dislike_cm FROM comments WHERE comment_id = '%d'" % comment_id
    try:
        cursor.execute(sql)
        data = cursor.fetchone()
        db.commit()
    except:
        db.rollback()
        print "invalid id"
        db.close()
        return False
    sql = "UPDATE comments SET dislike_cm = '%d' WHERE comment_id = '%d'" % (data[0]+1, comment_id)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print "cannot dislike"
        return False
    db.close()
    like_inserter_comment(comment_id, like_user)
    return data[0] + 1


def get_like_comment(comment_id):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql = "SELECT like_cm FROM comments WHERE comment_id = '%d'" % comment_id
    try:
        cursor.execute(sql)
        data = cursor.fetchone()
        db.commit()
    except:
        db.rollback()
        print "invalid id"
        return False
    db.close()
    return data[0]


def get_dislike_comment(comment_id):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql = "SELECT dislike_cm FROM comments WHERE comment_id = '%d'" % comment_id
    try:
        cursor.execute(sql)
        data = cursor.fetchone()
        db.commit()
    except:
        db.rollback()
        print "invalid id"
        return False
    db.close()
    return data[0]


def like_cm_calculator(comment_id):
    return get_like_comment(comment_id) - get_dislike_comment(comment_id)


def replying(reply_comment, reply_username, reply_post, reply):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql = "INSERT INTO replys (reply_comment,reply_username, reply_post,reply,reply_date) VALUES ('%d' , '%s', '%s','%s', NOW())" % (reply_comment, reply_username, reply_post, reply.decode('utf-8'))
    flag = False
    try:
        cursor.execute(sql)
        db.commit()
        flag = True
    except:
        db.rollback()
        print "cannot reply"
        flag = False
    db.close()
    if flag == True:
        return True
    else:
        return False


def get_reply(reply_id):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql = "SELECT reply FROM replys WHERE reply_id = '%d'" % reply_id
    try:
        cursor.execute(sql)
        data = cursor.fetchone()
        db.commit()
    except:
        db.rollback()
        print "invalid id"
    db.close()
    try:
        return data[0]
    except:
        return False


def get_reply_all(reply_comment):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql = "SELECT * FROM replys WHERE reply_comment = '%d'" % reply_comment
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        db.commit()
    except:
        db.rollback()
        print "invalid id"
    db.close()
    try:
        return data
    except:
        return False


def check_like_reply(like_re, like_user):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql = "SELECT * FROM like_re WHERE like_re = '%d' AND like_user = '%s' " % (like_re, like_user)
    try:
        cursor.execute(sql)
        data = cursor.fetchone()
        db.commit()
    except:
        db.rollback()
        print "invalid id"
    db.close()
    if data == None:
        return True
    else:
        return False


def like_inserter_reply(like_re, like_user):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    flag = False
    if check_like_reply(like_re, like_user):
        sql = "INSERT INTO like_re VALUES ('%d', '%s')" % (like_re, like_user)
        flag = False
        try:
            cursor.execute(sql)
            db.commit()
            flag = True
        except:
            db.rollback()
            print "invalid user or id"
            flag = False
        db.close()
    if flag == True:
        return True
    else:
        return False


def like_reply(reply_id, like_user):
    if check_like_reply(reply_id, like_user) == False:
        return False
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql = "SELECT like_re FROM replys WHERE reply_id = '%d'" % reply_id
    try:
        cursor.execute(sql)
        data = cursor.fetchone()
        db.commit()
    except:
        db.rollback()
        print "invalid id"
        db.close()
        return False
    sql = "UPDATE replys SET like_re = '%d' WHERE reply_id = '%d'" % (data[0]+1, reply_id)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print "cannot like"
        return False
    db.close()
    like_inserter_reply(reply_id, like_user)
    return data[0] + 1


def dislike_reply(reply_id, like_user):
    if check_like_reply(reply_id, like_user) == False:
        return False
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql = "SELECT dislike_re FROM replys WHERE reply_id = '%d'" % reply_id
    try:
        cursor.execute(sql)
        data = cursor.fetchone()
        db.commit()
    except:
        db.rollback()
        print "invalid id"
        db.close()
        return False
    sql = "UPDATE replys SET dislike_re = '%d' WHERE reply_id = '%d'" % (data[0]+1, reply_id)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        print "cannot dislike"
        return False
    db.close()
    like_inserter_reply(reply_id, like_user)
    return data[0] + 1


def get_like_reply(reply_id):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql = "SELECT like_re FROM replys WHERE reply_id = '%d'" % reply_id
    try:
        cursor.execute(sql)
        data = cursor.fetchone()
        db.commit()
    except:
        db.rollback()
        print "invalid id"
        return False
    db.close()
    return data[0]


def get_dislike_reply(reply_id):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql = "SELECT dislike_re FROM replys WHERE reply_id = '%d'" % reply_id
    try:
        cursor.execute(sql)
        data = cursor.fetchone()
        db.commit()
    except:
        db.rollback()
        print "invalid id"
        return False
    db.close()
    return data[0]


def like_re_calculator(reply_id):
    return get_like_reply(reply_id) - get_dislike_reply(reply_id)


def follow(follower, followed):
    if follower == followed or (followed in followings(follower)):
        return False
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql = "INSERT INTO follow VALUES ('%s' , '%s')" % (follower, followed)
    flag = False
    try:
        cursor.execute(sql)
        db.commit()
        flag = True
    except:
        db.rollback()
        print "invalid user or pass"
        flag = False
    db.close()
    if flag == True:
        return True
    else:
        return False


def unfollow(follower, followed):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql = "DELETE FROM follow WHERE follower = '%s' AND followed = '%s'" % (follower, followed)
    flag = False
    try:
        cursor.execute(sql)
        db.commit()
        flag = True
    except:
        db.rollback()
        print "invalid user or pass"
        flag = False
    db.close()
    if flag == True:
        return True
    else:
        return False


def followers(followed):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql = "SELECT follower FROM follow WHERE followed = '%s'" % followed
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        db.commit()
    except:
        db.rollback()
        print "invalid user"
        return False
    db.close()
    try:
        return lister_follow(data)
    except:
        return []


def followings(follower):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql = "SELECT followed FROM follow WHERE follower = '%s'" % follower
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        db.commit()
    except:
        db.rollback()
        print "invalid user"
        return False
    db.close()
    try:
        return lister_follow(data)
    except:
        return []


def lister_follow(my_list):
    temp = []
    for item in my_list:
        temp.append(item[0])
    return temp


def get_users(pattern):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql = "SELECT username,photo FROM users WHERE username LIKE '%s'" % ("%" + pattern + "%")
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
        db.commit()
    except:
        db.rollback()
        print "invalid user"
        return False
    db.close()
    try:
        return data
    except:
        return []


def forget_pass_user(username):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap", use_unicode=True, charset="utf8")
    cursor = db.cursor()
    sql = "SELECT username,password,email FROM users WHERE username = '%s'" %username
    try:
        cursor.execute(sql)
        data = cursor.fetchone()
        db.commit()
    except:
        db.rollback()
        print "invalid user"
        return False
    db.close()
    try:
        return data
    except:
        return []




#print sign_up('a','asc','sacsc','sacccccccc')
#print sign_up('b','assc','ssacaaaasc')
#print sign_up('c','assc','ssacvdasc')
#print sign_up('d','sec','ssacsvvc')
#print sign_in('a', 'asc')
#print get_photo_profile('a')
#update_password('a', 'asc', 'ee')
#print un_subscribe('d','sec')
#posting('a', 'ahhh')
#posting('a', 'argg')
#posting('b', 'aee')
#posting('c', 'accc')
#posting('d', 'aasc')
#print get_post(3)
#print check_like_post(3, 'a')
#like_inserter_post(likepost, like_user)

#like_post(2, 'a')
#like_post(3, 'a')
#dislike_post(4, 'a')
#like_post(2, 'a')
#like_post(2, 'a')
#like_post(2, 'a')
#like_post(2, 'a')
#like_post(2, 'a')

#dislike_post(post_id, like_user)

#print get_like_post(2)

#print get_dislike_post(2)

#photo_post(2, 'acsacasc','a')

#edit_post_text(2,"cscsxcxxsccccc", 'b')

#print delete_post(3, 'a')
#print delete_post(4, 'b')
#print delete_post(5, 'c')
#print delete_post(6, 'd')
#print like_post_calculator(3)

#commenting(7, 'a', 'adascvadv')
#commenting(7, 'a', 'adascvadv')
#commenting(7, 'a', 'advascadv')
#commenting(7, 'b', 'advaascdv')
#ommenting(7, 'c', 'advaascdv')
#commenting(7, 'd', 'advascascadv')
#print get_comment(2)

#print check_like_comment(2, 'a')
#like_inserter_comment(like_com, like_user)

#like_comment(2, 'a')
#like_comment(2, 'b')
#dislike_comment(2, 'c')

#dislike_comment(comment_id, like_user)
#print get_like_comment(2)

#print get_dislike_comment(2)

#print like_cm_calculator(2)

#replying(3, 'a',7,'kiram dahanet')
#replying(3, 'a',7,'kiram dahanet')
#print get_reply(2)

#print check_like_reply(2, 'a')

#like_inserter_reply(like_re, like_user)

#like_reply(2, 'a')
#like_reply(2, 'b')
#dislike_reply(2, 'c')
#dislike_reply(2, 'd')

#dislike_reply(2, 'a')
#print get_like_reply(2)
#print get_dislike_reply(2)

#print like_re_calculator(2)

#print follow('a', 'b')
#print follow('a', 'c')
#print follow('b', 'a')
#print follow('c', 'b')
#print follow('d', 'c')
#print follow('d', 'a')
#print follow('c', 'a')
#print followers('a')
#print followings('a')
#print unfollow('a', 'b')
#print get_post_all('a')
#print get_comment_all(9)
#print get_reply_all(3,'a',7)
#print followings("a")
#print posting("ww","dvdvdv")
#print commenting(12,"ww","dvcdvdv")
#print sign_up('vdvsw','dvc','sdvvvsc','saccdvcc')
#print sign_up('advwwdv','asc','sadavc','saadcccccc')
#print sign_up('wdvdv','asc','sacsdwcxc','sacccccccc')
#print sign_up('wfbvdw','asc','sacdvsc','sacccccccc')
#print sign_up('wsdvdvvvv','asc','sacwwwsc','sacccccccc')
#print sign_up('wsdvdvvvv','asc','sacwwwsc','sacccccccc')

#print sign_up('wsdvwwdvvvvw','asascc','sacwascwwsc','sacccccccc')
#print get_users("a")
#print forget_pass_user("ww")
#print get_post_all("a")[-1][0]
# print posting("a", repr("<img src='{{ url_for('static', filename='pics/211.png') }}' style='size:auto;'></img>14"), "pics/211.png")
# print followings("a")

