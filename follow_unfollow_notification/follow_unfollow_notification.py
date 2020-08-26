import subprocess
from docopt import docopt
import xdg
import json
import os


def fun_initialize():
    """
    Usage:
        fun_initialize --consumer-key <CONSUMER_KEY> --consumer-secret <CONSUMER_SECRET>
        fun_initialize -h | --help
    """
    args = docopt(fun_initialize.__doc__)
    consumer_key = args["<CONSUMER_KEY>"]
    consumer_secret = args["<CONSUMER_SECRET>"]
    if consumer_key and consumer_secret:
        pass
    else:
        print(fun_initialize.__doc__)
        return
    res = subprocess.run(
        [
            "twurl",
            "authorize",
            "--consumer-key",
            consumer_key,
            "--consumer-secret",
            consumer_secret,
        ]
    )
    return


def get_followers_list(screen_name):

    followers_list = []

    res = json.loads(
        subprocess.run(
            ["twurl", "/1.1/followers/ids.json?screen_name=" + screen_name],
            stdout=subprocess.PIPE,
        ).stdout
    )
    followers_list += res["ids"]
    next_cursor_str = res["next_cursor_str"]
    while next_cursor_str != "0":
        res = json.loads(
            subprocess.run(
                [
                    "twurl",
                    "/1.1/followers/ids.json?screen_name="
                    + screen_name
                    + "&cursor="
                    + next_cursor_str,
                ],
                stdout=subprocess.PIPE,
            ).stdout
        )
        followers_list += res["ids"]
        next_cursor_str = res["next_cursor_str"]

    return list(map(lambda x: str(x), followers_list))


def convert_names(user_id_list):

    if len(user_id_list) == 0:
        return []

    request_url = "/1.1/users/lookup.json?user_id=" + user_id_list[0]
    for user_id in user_id_list:
        request_url += "," + user_id

    res = json.loads(
        subprocess.run(["twurl", request_url], stdout=subprocess.PIPE,).stdout
    )

    return list(map(lambda x: x["name"] + " (@" + x["screen_name"] + ")", res))


def fun_notify():
    """
    Usage:
        fun_notify --screen-name <SCREEN_NAME>
        fun_notify -h | --help
    """
    args = docopt(fun_notify.__doc__)
    screen_name = args["<SCREEN_NAME>"]

    followers_prev_file = (
        xdg.XDG_CONFIG_HOME
        / "follow-unfollow-notification"
        / ("followers_" + screen_name + ".txt")
    )

    if os.path.exists(followers_prev_file):
        with open(followers_prev_file) as f:
            s = f.read()
    else:
        s = ""

    followers_prev = list(filter(lambda x: x != "", s.split("\n")))
    followers = get_followers_list(screen_name)

    new_followers = list(filter(lambda x: x not in followers_prev, followers))
    new_unfollowers = list(filter(lambda x: x not in followers, followers_prev))

    print("New Follower(s):")
    for user_name in convert_names(new_followers):
        print(user_name)

    print("New Unfollower(s):")
    for user_name in convert_names(new_unfollowers):
        print(user_name)

    with open(followers_prev_file, mode="w") as f:
        for user_id in followers:
            f.write(user_id + "\n")

    return
