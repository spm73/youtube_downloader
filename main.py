import pytube
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
import os


def get_input():
    return input("Insert video url\n")


def download_both_files(url):
    video = pytube.YouTube(url)
    # print(video.streams)
    try:
        audio = video.streams.filter(mime_type="audio/mp4", type="audio").first()
        audio.download(filename_prefix="audio")
    except AttributeError as err:
        print("Something went wrong downloading the audio :(")
        raise RuntimeError from err
    try:
        video = video.streams.filter(res="1080p", mime_type="video/mp4").first()
        video.download(filename_prefix="video")
    except AttributeError as err:
        print("Something went wrong downloading the video:(")
        print("Check the quality of the video as only converts to 1080p")
        raise RuntimeError from err


def get_audio_file():
    audio_file = list(filter(lambda file: file[:5] == 'audio', os.listdir(os.getcwd())))
    return audio_file[0]


def get_video_file():
    """Rudimentary way (same happens with get_audio_file())"""
    """video_file = ""
    for file in os.listdir(os.getcwd()):
        if file[:5] == 'video':
            video_file = file
    return video_file"""

    """With filter (more fashionable)"""
    video_file = list(filter(lambda file: file[:5] == 'video', os.listdir(os.getcwd())))
    return video_file[0]


def convert_into_one(audio_file, video_file):
    audio = AudioFileClip(audio_file)
    video = VideoFileClip(video_file)
    final_clip = video.set_audio(audio)
    name = video_file[5:]
    final_clip.write_videofile(name)


def delete_files(audio_file, video_file):
    os.remove(audio_file)
    os.remove(video_file)


def main():
    url = get_input()
    download_both_files(url)
    audio_file = get_audio_file()
    video_file = get_video_file()
    convert_into_one(audio_file, video_file)
    delete_files(audio_file, video_file)
    print("Done")
    exit(0)


if __name__ == '__main__':
    main()
