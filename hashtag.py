from instabot import *
import os
import shutil
import time
import random
# from important import config

import config
def delay(num):
    time.sleep(random.randint(5 * num, 10 * num))


def hashtag_username():
    hash1 = input("Enter hashtag = ")
    prev = []

    if not os.path.isdir(f'output/{hash1}'):
        os.mkdir(f'output/{hash1}')
    if not os.path.isfile(f'output/{hash1}/username.csv'):
        prev = []
        with open(f'output/{hash1}/username.csv', 'a') as file:
            file.write('')
            file.close()

    else:
        with open(f'output/{hash1}/username.csv', 'r') as file:
            f = file.read()
            prev = f.split('\n')
            file.close()
    for i in range(1000):
        start1 = time.time()
        users = insta.get_hashtag_users(str(hash1))
        print(users)
        print(len(users))
        delay(2)
        new = list(set(users) - set(prev))
        print(new)
        print(len(new))
        prev = prev + list(new)
        with open(f'output/{hash1}/username.csv', 'a') as outfile:
            outfile.write("\n".join(str(item) for item in new))
        end1 = time.time()
        print("total time taken : ", end1 - start1)


def userfollowerfollowing():
    username = str(input("Enter target Username = "))

    if not os.path.isdir(f'output/{username}'):
        os.mkdir(f'output/{username}')

    followings = insta.get_user_following(username)
    with open(f'output/{username}/following.csv', 'a') as file:
        for following in followings:
            print(following)
            file.write(str(following) + '\n')
        file.close()

    delay(5)

    followers = insta.get_user_followers(username)
    with open(f'output/{username}/followers.csv', 'a') as file:
        for follower in followers:
            print(follower)
            file.write(str(follower) + '\n')
        file.close()
    delay(4)


if os.path.isdir('config'):
    shutil.rmtree('config')

insta = Bot()

insta.login(username="hasnainkhan", password="galaxyj5")

while True:

    delay(3)
    print("___________MENU__________\n \n"
          "  1) Get Usernames From HashTag \n"
          "  2) Get Followers and Following From Username\n")
    choose = int(input("Choose (1-2) = "))
    start = time.time()

    if choose == 1:
        hashtag_username()
    elif choose == 2:
        userfollowerfollowing()
    else:
        print("Incorrect Selection")
        break

    end = time.time()
    print("total time taken : ", end - start)








