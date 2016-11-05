# Twitter Avatar Rotator

Why won't make everyone angry because of useless mobile traffic waste to fetch your avatar every day?:D

# Prepare

You need to:

## Choose photos

Choose photos and put them to ./images/

## Environment

This repo is designed to run in heroku, but it is simple enough to understand how it works.

You can run it locally:
```shell
virtualenv env
pip install -r requirements.txt
python update_pic.py
```

## App running

Register your twitter application or if you already have one get your consumer key and consumer secret.

```shell
export consumer_key=PUT_YOUR_CONSUMER_KEY_HERE
export consumer_secret=PUT_YOUR_CONSUMER_SECRET_HERE
export user_access_token=PUT_YOUR_ACCESS_TOKEN_HERE
export user_access_secret=PUT_YOUR_ACCESS_SECRET_HERE
```

You can get access token / secret by running on desktop:

```shell
python -u twitterbot_utils.TwiAuth
```
