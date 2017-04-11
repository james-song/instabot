import json
import time
import hashlib
import hmac
from instabot.new import Config


def send_request(session, endpoint, post=None):
    try:
        if post is not None:  # POST
            response = session.post(Config.API_URL + endpoint, data=post)
        else:  # GET
            response = session.get(Config.API_URL + endpoint)
    except Exception as e:
        print(str(e))
        return False

    if response.status_code == 200:
        print("OK")
        return json.loads(response.text)
    else:
        print("Request return " + str(response.status_code) + " error!")
        print(response.text)
        if response.status_code == 429:
            sleep_minutes = 5
            print("That means 'too many requests'. I'll go to sleep for %d minutes." % sleep_minutes)
            time.sleep(sleep_minutes * 60)
        exit()


def generate_signature(data):
    return 'ig_sig_key_version=' + Config.SIG_KEY_VERSION + '&signed_body=' + hmac.new(
        Config.IG_SIG_KEY.encode('utf-8'), data.encode('utf-8'), hashlib.sha256).hexdigest() + '.' + data
