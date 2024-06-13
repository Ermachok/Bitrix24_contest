from flask import Flask, request, send_file
from utils import create_video

app = Flask(__name__)


@app.route('/create_video', methods=['GET'])
def create_video_with_caption():
    text = request.args.get('text')

    video_file = create_video(text)
    video_file.write_videofile(f'{text}.mp4', codec='libx264', fps=90)

    return send_file(f'{text}.mp4', as_attachment=True)


if __name__ == '__main__':
    app.run()
