import logging

from moviepy.editor import TextClip, ColorClip, CompositeVideoClip
from django.http import FileResponse, HttpRequest
from app_ticket.models import RequestData

log = logging.getLogger(__name__)


def create_video(text: str, duration: float = 3,
                 window_size: tuple = (100, 100)) -> CompositeVideoClip:
    """
    Func for making video
    :param text: input text
    :param duration: video duration
    :param window_size: size of window
    :return: video clip
    """
    char_clips = []
    cur_text = ''
    char_clip_duration = duration / (len(text))
    for i, char in enumerate(text):
        cur_text += char

        char_clip = TextClip(cur_text, fontsize=30, font="Ubuntu", color='white', bg_color='black').set_position(
            ('center', 'center')).set_duration(char_clip_duration).set_start(i * char_clip_duration)
        if char_clip.size[0] > window_size[0]:
            cur_text = cur_text[1:]

        char_clips.append(char_clip)

    background = ColorClip(window_size, color=(0, 0, 0), duration=duration)

    final_clip = CompositeVideoClip([background] + char_clips, size=window_size)

    return final_clip


def create_video_with_caption(request: HttpRequest):
    text = request.GET.get('text')
    video_file = create_video(text)
    video_file.write_videofile(f'{text}.mp4', codec='libx264', fps=90)

    request_object = RequestData(request_method=request.method, request_text=text)
    request_object.save()

    log.info('Create function worked')
    return FileResponse(open(f'{text}.mp4', 'rb'), as_attachment=True)
