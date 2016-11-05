from os import listdir
from sys import argv
from random import randint
from apscheduler.schedulers.blocking import BlockingScheduler
from twitterbot_utils import Twibot

sched = BlockingScheduler()
api = Twibot().api
images = filter(lambda f: 'png' in f or 'jpg' in f, listdir('images/'))


@sched.scheduled_job('interval', hours=20)
def update_image():
    image = images[randint(0, len(images))]
    api.update_profile_image('images/' + image)


if __name__ == '__main__':
    update_image()
    if '--test' in argv or '--oneshot' in argv:
        exit(0)
    sched.start()
