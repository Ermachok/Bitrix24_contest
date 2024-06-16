from django.http import FileResponse, HttpRequest
from utils.utils import create_video


def create_video_with_caption(request: HttpRequest):
    text = request.GET.get('text')

    video_file = create_video(text)
    video_file.write_videofile(f'{text}.mp4', codec='libx264', fps=90)

    return FileResponse(open(f'{text}.mp4', 'rb'), as_attachment=True)

