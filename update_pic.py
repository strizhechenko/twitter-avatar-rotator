from tweet import Twibot
from os import listdir
from random import randint
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()
api = Twibot().api
images = filter(lambda f: 'png' in f or 'jpg' in f, listdir('images/'))


@sched.scheduled_job('interval', minutes=15)
def update_image():
    image = images[randint(0, len(images))]
    api.update_profile_image('images/' + image)


if __name__ == '__main__':
    sched.start()
