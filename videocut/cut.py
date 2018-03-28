# -*- coding: utf-8 -*-
# sudo pip install moviepy
# sudo apt-get install ffmpeg
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
ffmpeg_extract_subclip("video1.mp4", 6*60+41,10*60+37 , targetname="test.mp4")

# 快速地获得视频剪辑

# 已用我爱我家亲家母来我家做过测试。