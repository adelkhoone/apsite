#############
#DB         #
#Triple A   #
#############
import MySQLdb


def sign_up(username, password, email, photo="__empty__"):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap")
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
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap")
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
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap")
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


def update_password(username, password, new_pass):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap")
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
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap")
    cursor = db.cursor()
    sql = "INSERT INTO posts (username_post,post,date_mod,photo_post) VALUES ('%s' , '%s', NOW(), '%s')" % (username_post, post, photo)
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
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap")
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
    return data[0]


def check_like_post(post_id, user)


def like_post(post_id):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap")
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
    return data[0] + 1


def dislike_post(post_id):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap")
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
    return data[0] + 1


def get_like_post(post_id):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap")
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
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap")
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
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap")
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


def edit_post_text(post_id, new_pot, username_post):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap")
    cursor = db.cursor()
    sql = "UPDATE posts SET post = '%s',date_mod = NOW() WHERE post_id = '%d' AND username_post = '%s'" % (new_pot, post_id, username_post)
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
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap")
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


def like_cm_calculator(post_id):
    return get_like_post(post_id) - get_dislike_post(post_id)


def commenting(comment_post, comment_username, comment):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap")
    cursor = db.cursor()
    sql = "INSERT INTO comments (comment_post,comment_username,comment,comment_date) VALUES ('%d' , '%s', '%s', NOW())" % (comment_post, comment_username, comment)
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
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap")
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
    return data[0]


def like_comment(comment_id):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap")
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
    return data[0] + 1


def dislike_comment(comment_id):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap")
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
    return data[0] + 1


def get_like_comment(comment_id):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap")
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
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap")
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


def replying(reply_comment, reply_username, reply):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap")
    cursor = db.cursor()
    sql = "INSERT INTO replys (reply_comment,reply_username,reply,reply_date) VALUES ('%d' , '%s', '%s', NOW())" % (reply_comment, reply_username, reply)
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
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap")
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
    return data[0]


def like_reply(reply_id):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap")
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
    return data[0] + 1


def dislike_reply(reply_id):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap")
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
    return data[0] + 1


def get_like_reply(reply_id):
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap")
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
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap")
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
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap")
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
    db = MySQLdb.connect("localhost", "root", "asoaso7676", "site_ap")
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


def





#sign_up("ali", "reza", "rre@dc.cdm")
#print sign_in("ali","reza")
#print posting("ali","kos nagoo daus")
#print get_dislike_post(1)
#print update_password("ali","reza","dcedc")
#print photo_post(1,"kir")
#print edit_post_text(1, 'nagofatddam an','ali')
#print commenting(1,'ali')
#print get_dislike_comment(1)
#print like_reply(1)
#print delete_post(1 , 'ali')
sign_up('a','dvdv','vdvd')
sign_up('b','vdvdv','gr')
print follow("a",'b')