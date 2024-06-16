from django.http import FileResponse, HttpRequest
from utils.utils import create_video
from app_ticket.models import RequestData


def create_video_with_caption(request: HttpRequest):

    text = request.GET.get('text')
    video_file = create_video(text)
    video_file.write_videofile(f'{text}.mp4', codec='libx264', fps=90)

    request_object = RequestData(request_method=request.method, request_text=text)
    request_object.save()

    return FileResponse(open(f'{text}.mp4', 'rb'), as_attachment=True)
