from threads_api.src.threads_api import ThreadsAPI
from tqdm import tqdm
import asyncio
import os

async def get_user_id_from_username(api, username):
    # sets the username to the username passed in
    user_id = await api.get_user_id_from_username(username)
    # if user_id is not None, print the user_id
    if user_id:
        print(f"The user ID for username {username} is: {user_id}")
    else:
        print(f"User ID not found for username: {username}")

    return user_id

async def get_user_threads(api, username, user_id, number_of_threads):
    # capitalizes the first letter of the username
    username = username.capitalize()
    # if user_id is not None, print threads for user
    if user_id:
        threads = await api.get_user_threads(user_id)
        print(f"Threads for user {username} are: ")
        # use tqdm to display the loading spinner
        with tqdm(total = min(number_of_threads, len(threads)), bar_format = '{postfix}') as pbar:
            # loops through threads and prints the caption and like count for the latest 10 threads
            for i, thread in enumerate(threads[:number_of_threads], start = 1):
                # caption removes {'text': ' and '} from text output
                caption = thread['thread_items'][0]['post']['caption']['text']
                print(f"{username}'s Thread {i}: \n{caption} \n\nLikes: {thread['thread_items'][0]['post']['like_count']}\n")
                # update the progress bar
                pbar.update(1)  

        if len(threads) > number_of_threads:
            print(f"Total threads available: {len(threads)}. Displayed the latest 10 threads.")
    else:
        print(f"User ID not found for username: {username}")

async def get_user_replies(api, username, user_id, number_of_replies):
    # capitalizes the first letter of the username
    username = username.capitalize()
    # if user_id is not None, print replies for user
    if user_id:
        replies = await api.get_user_replies(user_id)
        print(f"Replies for user {username} are: ")
        # use tqdm to display the loading spinner
        with tqdm(total = min(number_of_replies, len(replies)), bar_format = '{postfix}') as pbar:
            # loops through replies and prints the caption and like count for the latest 10 replies
            for i, reply in enumerate(replies[:number_of_replies], start = 1):
                # caption removes {'text': ' and '} from text output
                caption = reply['thread_items'][1]['post']['caption']['text']
                print(f"{username}'s Reply {i}: \n{caption} \n\nLikes: {reply['thread_items'][1]['post']['like_count']}\n")
                # update the progress bar
                pbar.update(1)

        if len(replies) > number_of_replies:
            print(f"Total replies available: {len(replies)}. Displayed the latest {number_of_replies} replies.")
    else:
        print(f"User ID not found for username: {username}")

async def get_user_profile(api, username, user_id):
    # capitalizes the first letter of the username
    username = username.capitalize()
    if user_id:
        user_profile = await api.get_user_profile(user_id)
        print(f"User profile for {username}: ")
        # use tqdm to display the loading spinner
        with tqdm(total = 3, bar_format = '{postfix}') as pbar:
            pbar.update(1)
            print(f"Name: {user_profile['username']}")
            pbar.update(1)
            print(f"Bio: {user_profile['biography']}")
            pbar.update(1)
            print(f"Followers: {user_profile['follower_count']}")
            pbar.update(1)
    else:
        print(f"User ID not found for username: {username}")

# saves instance of ThreadsAPI class to variable api
api = ThreadsAPI()

user_id = asyncio.run(get_user_id_from_username(api, "zuck"))
asyncio.run(get_user_profile(api, "zuck", user_id))
# add a break 
print("-"*40 + "\n")

asyncio.run(get_user_threads(api, "zuck", user_id, 10))
# add a break 
print("\n" + "-"*40 + "\n")

asyncio.run(get_user_replies(api, "zuck", user_id, 10))