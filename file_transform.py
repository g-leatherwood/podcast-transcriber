import math
from pathlib import Path

from pydub import AudioSegment


def get_audio_intervals(file):
    """
    Takes an audio file and breaks it into
    ten minute chunks for use with whisper
    transcription.
    """
    file_names = []

    audio = AudioSegment.from_mp3(file)
    length = len(audio)

    # PyDub handles time in milliseconds
    ten_minutes = 10 * 60 * 1000

    intervals = math.ceil(length / ten_minutes)

    for i in range(intervals):
        new_file = f"{file}_{i + 1}_ten.mp3"
        chunk = audio[i * ten_minutes : (i + 1) * ten_minutes]
        chunk.export(new_file, format="mp3")
        file_names.append(new_file)

    return file_names


def delete_files(file_names):
    """
    Deletes the given files. Used to clean up
    the ten minute chunks once the transcript
    is written. Files that are already gone
    are skipped.
    """
    for file in file_names:
        Path(file).unlink(missing_ok=True)
