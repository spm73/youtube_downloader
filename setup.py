from distutils.core import setup
import py2exe
import pytube
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
import os


setup(zipfile=None,
      options={'py2exe': {"bundle_files":1},
               'includes': ['pytube', 'moviepy.video.io.VideoFileClip.VideoFileClip',
                            'moviepy.audio.io.AudioFileClip.AudioFileClip', 'os']},
      console=["main.py"])