from moviepy.editor import TextClip, ColorClip, CompositeVideoClip


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

        char_clip = TextClip(cur_text, fontsize=30, color='white', bg_color='black').set_position(
            ('center', 'center')).set_duration(char_clip_duration).set_start(i * char_clip_duration)
        if char_clip.size[0] > window_size[0]:
            cur_text = cur_text[1:]

        char_clips.append(char_clip)

    background = ColorClip(window_size, color=(0, 0, 0), duration=duration)

    final_clip = CompositeVideoClip([background] + char_clips, size=window_size)

    return final_clip



