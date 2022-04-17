"""Handle every function related to files."""

import pickle
import os
import re
import os.path


def has_been_posted(threadId, previous_post_list) -> bool:
    """Verify if the thread is the previous_postList."""
    if threadId in previous_post_list:
        return True

    return False


def update_post_list(threadId, previous_post_list):
    """Update the previous post list.

    We're using a queue as we only fetch top threads.
    Given a few days, it's sure they've never been posted.
    """
    previous_post_list.pop()
    previous_post_list.append(threadId)
    return previous_post_list


def update_previous_posts_file(fPREVIOUS_POSTS, previous_post_list):
    """Overwrite the previous_post_file with a given list."""
    with open(fPREVIOUS_POSTS, 'wb') as file:
        pickle.dump(previous_post_list, file)


def empty_folder(folder):
    """Delete files contained in the media folder.

    Args:
        folder (_type_): _description_
    """
    for root, dirs, files in os.walk(folder):
        for file in files:
            os.remove(os.path.join(root, file))


def fetch_state(file) -> int:
    """Return the state of the program."""
    with open(file, 'r') as f:
        val = f.read()
        if val:
            return int(val)


def increment_state(file) -> None:
    """Increment the state of the program."""
    current_state = fetch_state(file)
    with open(file, 'w') as f:
        next_state = str(current_state + 1)
        f.write(next_state)


def create_state_file(file) -> None:
    """Create the file."""
    with open(file, 'w+') as f:
        f.write(str(0))
