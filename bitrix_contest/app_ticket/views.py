import logging

from moviepy.editor import TextClip, ColorClip, CompositeVideoClip
from django.http import FileResponse, HttpRequest
from app_ticket.models import RequestData

log = logging.getLogger(__name__)


def create_video(text: str, duration_sec: float = 3, window_size: tuple = (100, 100), fps=50) -> CompositeVideoClip:
    width, height = window_size[0], window_size[1]
    x, y = width, height // 2

    frames = int(fps * duration_sec)
    fontsize = 30
    symbols_in_window = int(width/fontsize)
    per_symbol = width / symbols_in_window
    all_distance = 2 * len(text) // symbols_in_window * per_symbol + width
    step_size = all_distance / frames

    char_clips = []
    for t in range(frames):
        x -= step_size
        char_clip = TextClip(text, fontsize=fontsize, font="Ubuntu", color='white', bg_color='black').set_position((x, y)).set_duration(1 / fps).set_start(t / fps)
        char_clips.append(char_clip)

    background = ColorClip(window_size, color=(0, 0, 0), duration=duration_sec)
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
