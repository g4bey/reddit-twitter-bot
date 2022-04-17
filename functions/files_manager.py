import pickle
import os
import re
import os.path

# PREVIOUS POST LIST RELATED FUNCTIONS
# ------------------------------------
# verify if the thread is the previous_postList


def has_been_posted(threadId, previous_post_list) -> bool:
    if threadId in previous_post_list:
        return True

    return False
# update the previous post list. we're using a queue as we only fetch top threads.
# Given a few days, it's sure they've never been posted.


def update_post_list(threadId, previous_post_list):
    previous_post_list.pop()
    previous_post_list.append(threadId)
    return previous_post_list
# overwrite the previous_post_file with a given list.


def update_previous_posts_file(fPREVIOUS_POSTS, previous_post_list):
    with open(fPREVIOUS_POSTS, 'wb') as file:
        pickle.dump(previous_post_list, file)
# deleted files contained in the media folder.


def empty_folder(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            os.remove(os.path.join(root, file))

# PROGRAMME STATE RELATED FUNCTIONS
# ------------------------------------
# returns the state of the program.


def fetch_state(file) -> int:
    with open(file, 'r') as f:
        val = f.read()
        if val:
            return int(val)

# increment the state of the program


def increment_state(file) -> None:
    current_state = fetch_state(file)
    with open(file, 'w') as f:
        next_state = str(current_state + 1)
        f.write(next_state)

# create the file and append a 0


def create_state_file(file) -> None:
    with open(file, 'w+') as f:
        f.write(str(0))
