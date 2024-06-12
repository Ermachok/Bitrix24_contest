from flask import Flask, request, send_file
from moviepy.editor import TextClip, ColorClip, CompositeVideoClip

app = Flask(__name__)


@app.route('/create_video', methods=['GET'])
def create_video_with_caption():
    text = request.args.get('text')
    duration = 3

    caption = TextClip(text, fontsize=50, color='white', bg_color='black').set_position(
        ('center', 'bottom')).set_duration(duration)

    background = ColorClip(size=(caption.w, caption.h), color=(0, 0, 0)).set_duration(duration)

    final_clip = CompositeVideoClip([background, caption.set_position(('center', 'bottom'))])

    final_clip = final_clip.set_duration(duration).set_fps(24)

    final_clip.write_videofile(f'{text}.mp4', codec='libx264', fps=24)

    return send_file(f'{text}.mp4', as_attachment=True)


if __name__ == '__main__':
    app.run()
