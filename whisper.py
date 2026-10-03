from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

from file_transform import get_audio_intervals

load_dotenv()


def get_file(file_name):
    """
    Splits the audio file into ten minute
    chunks and returns the chunk file names.
    """
    file = get_audio_intervals(file_name)
    return file


def transcribe_audio(file_names, output_name):
    """
    Transcribes each audio chunk with whisper
    and writes the combined text to
    output_name.txt, creating the output
    folder if it doesn't exist.
    """
    contents = ""
    path = Path(f"{output_name}.txt")
    path.parent.mkdir(parents=True, exist_ok=True)
    for file in file_names:
        client = OpenAI()
        with open(file, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                file=audio_file,
                model="whisper-1",
                response_format="verbose_json",
                timestamp_granularities=["segment"],
            )

        contents += (
            "\n".join(segment.text.strip() for segment in transcription.segments) + "\n"
        )
    path.write_text(contents)
