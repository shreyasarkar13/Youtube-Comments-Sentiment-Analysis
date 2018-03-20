import sys




sys.path.append("D:\data analytics and ML\Analytics\CommentsTesting.py")


#
#
#
# from Search_data_by_keyword import youtube_search
#
# from Comments_by_Channel import get_videos_FromChanel, youtube , get_comment_threads

# from Comments_by_videoid import get_comment_threads2

from CommentsTesting import YouTubeApi


import json


y= YouTubeApi()

y.get_video_comment()