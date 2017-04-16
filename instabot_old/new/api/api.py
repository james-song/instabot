from instabot.new.api import request


def get_profile_data(user):
    return request.send(user.session, 'users/' + str(user.id) + '/info/')


def get_user_feed(user, maxid='', minTimestamp=None):
    return request.send(user.session,
                        'feed/user/' + str(user.id) + '/?max_id=' + str(maxid) + '&min_timestamp=' + str(minTimestamp) +
                        '&rank_token=' + str(user.rank_token) + '&ranked_content=true')


def get_user_followers(user, user_id, maxid=''):
    return request.send(user.session,
                        'friendships/' + str(user_id) + '/followers/?max_id=' + str(maxid) + '&rank_token=' + user.rank_token)


def get_user_followings(user, user_id, maxid=''):
    return request.send(user.session,
                        'friendships/' + str(user_id) + '/following/?max_id=' + str(maxid) + '&rank_token=' + user.rank_token)