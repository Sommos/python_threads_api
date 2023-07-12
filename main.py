from threads_api.src.threads_api import ThreadsAPI
import asyncio
import os

async def get_user_id_from_username(username):
    # saves instance of ThreadsAPI class to variable api
    api = ThreadsAPI()
    # sets the username to the username passed in
    user_id = await api.get_user_id_from_username(username)
    # if user_id is not None, print the user_id
    if user_id:
        print(f"The user ID for username {username} is: {user_id}")
    else:
        print(f"User ID not found for username: {username}")

    return user_id

async def get_user_threads(username, user_id):
    # saves instance of ThreadsAPI class to variable api
    api = ThreadsAPI()
    # capitalizes the first letter of the username
    username = username.capitalize()
    # if user_id is not None, print threads for user
    if user_id:
        threads = await api.get_user_threads(user_id)
        print(f"Threads for user {username} are: ")
        # loops through threads and prints the caption and like count
        for thread in threads:
            # caption removes {'text': ' and '} from text output
            caption = thread['thread_items'][0]['post']['caption']['text']
            print(f"{username}'s Post: {caption} || Likes: {thread['thread_items'][0]['post']['like_count']}")
    else:
        print(f"User ID not found for username: {username}")

user_id = asyncio.run(get_user_id_from_username("zuck"))
asyncio.run(get_user_threads("zuck", user_id))