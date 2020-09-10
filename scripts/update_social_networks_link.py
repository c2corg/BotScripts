"""

"""
import os
from datetime import date
import re

from campbot import CampBot

login = os.environ["SCRIPT_LOGIN"]
password = os.environ["SCRIPT_PASSWORD"]
topic_id = os.environ["SCRIPT_TOPIC_ID"]
post_id = os.environ["SCRIPT_POST_ID"]
poll_name = os.environ["SCRIPT_POLL_NAME"]
option_id = os.environ["SCRIPT_OPTION_ID"]

bot = CampBot(min_delay=0.01)
bot.login(login, password)

voters = bot.forum.get_voters(post_id=post_id, poll_name=poll_name, option_id=option_id)

ids = set("2") # prevent an empty list with camptocamp profile id

for voter in voters:
    try:
        user = bot.wiki.get_user(forum_name=voter["username"])
    except Exception:
        pass # user not found > don't care
    else:
        print("Allow {} (@{})".format(user.document_id, voter["username"]))
        ids.add(str(user.document_id))

url = "https://www.camptocamp.org/outings?u={}".format(",".join(ids))

post = bot.forum.get_post(topic_id, 1)

raw = re.sub(
    r"\[Liste des sorties éligibles au [0-9]{4}-[0-9]{2}-[0-9]{2}\]\(https://www.camptocamp.org/outings\?u=[0-9,]*\)", 
    "[Liste des sorties éligibles au {}]({})".format(date.today(), url), 
    post["raw"]
)

print(raw)

bot.forum.put("/posts/{}".format(post["id"]), {"topic_id": post["topic_id"], "raw": raw})
