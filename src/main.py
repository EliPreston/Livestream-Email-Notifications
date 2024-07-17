import requests
from dotenv import load_dotenv
import time
import os
import smtplib


def getTwitchAuthToken():
    url = 'https://id.twitch.tv/oauth2/token'
    params = {
        # 'client_id':client_id,
        'client_id': os.getenv('TWITCH_CLIENT_ID'),
        # 'client_secret':client_secret,
        'client_secret': os.getenv('TWITCH_CLIENT_SECRET'),
        'grant_type':'client_credentials'
    }

    req = requests.post(url=url,params=params)
    token = req.json()['access_token']
    # print(f'{token=}')

    return token


def getStreamerInfo(twitch_auth_token, twitch_username):
    #getting user data (user id for example)
    url = f'https://api.twitch.tv/helix/users?login={twitch_username}'
    headers = {
        'Authorization': f'Bearer {twitch_auth_token}',
        'Client-Id': os.getenv('TWITCH_CLIENT_ID')
    }
    req = requests.get(url=url,headers=headers)
    userdata = req.json()
    streamerID = userdata['data'][0]['id']
    # print(f'{streamerID=}')

    return streamerID


def getStreamStatus(twitch_auth_token, twitch_userid):
    #getting stream info (by user id for example)
    url = f'https://api.twitch.tv/helix/streams?user_id={twitch_userid}'
    headers = {
        'Authorization':f'Bearer {twitch_auth_token}',
        'Client-Id': os.getenv('TWITCH_CLIENT_ID')
    } 
    req = requests.get(url=url,headers=headers)
    streaminfo = req.json()
    
    return streaminfo


def sendEmailNotif(streamer, stream_title):

    host = os.getenv('SMTP_HOST')
    port = os.getenv('HOST_PORT')
    smtp = smtplib.SMTP(host, port)

    from_email = os.getenv('FROM_EMAIL')
    from_pass = os.getenv('FROM_EMAIL_PASS')
    to_email = os.getenv('TO_EMAIL')

    message = f"""Subject: {streamer} is live - {stream_title}"""


    status_code, response = smtp.ehlo()
    print(f"[*] Echoing the server: {status_code} {response}")

    status_code, response = smtp.starttls()
    print(f"[*] Starting TLS connection: {status_code} {response}")

    status_code, response = smtp.login(from_email, from_pass)
    print(f"[*] Logging in: {status_code} {response}")

    smtp.sendmail(from_email, to_email, message)
    smtp.quit()




if __name__ == "__main__":
    
    load_dotenv()
    twitch_auth_token = getTwitchAuthToken()

    streamers = {
        "connoreatspants": 0,
        "hasanabi": 0,
        "bigguy": 0,
        "schlatt": 0,
        "fitz": 0,
        "mf_ib": 0
    }
    
    try:
        while True:
            # os.system('cls||clear')

            for streamer in streamers:
                
                streamer_id = getStreamerInfo(twitch_auth_token, streamer)
                streaminfo = getStreamStatus(twitch_auth_token, streamer_id)
                # print(f'{streaminfo}')
                
                # if live and previously not live
                if len(streaminfo['data']) > 0 and streamers[streamer] == 0:
                    print(f'{streamer} is live')
                    streamers[streamer] = 1
                    sendEmailNotif(streaminfo['data'][0]['user_name'], streaminfo['data'][0]['title'])

                # if not live and prevously live
                elif len(streaminfo['data']) == 0 and streamers[streamer] == 1:
                    streamers[streamer] = 0
                    print(f'{streamer} was live and has gone offline')
                    
                # no change in stream status
                else:
                    print(f'no change to {streamer}\'s stream')
                    pass
                
            print("")
                
            time.sleep(5)
    except KeyboardInterrupt:
        pass
    