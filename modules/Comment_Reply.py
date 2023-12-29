import json
import time
import random
import pickle
from instagrapi import Client
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag

# Media ID
media_id = "3099414201550848661"
# Comment ID
comment_og = "18220170175225278"

try:
    # Open Comments
    with open(f'C:/BlackAquaPython/comments/Comment_Reply.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        comment_reply = random.choice(lines)
        # Reply to the comment
        cl.media_comment(media_id=media_id, text=comment_reply, replied_to_comment_id=comment_og)
        print(f'Reply to Comment Post Successs')
except Exception as e:
    print(f"Failed to Reply Comment: {e}")

