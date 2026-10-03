# Podcast Transcriber

Transcribe podcast episodes (or any mp3) to plain text with OpenAI's Whisper API.

The episode is split into 10-minute chunks so it stays under Whisper's upload size limit. Each chunk is transcribed, the results are written to a single `.txt` file, and the chunks are deleted. Your original mp3 is left untouched.

## Requirements

- Python 3.13+
- These Python packages (also listed in `pyproject.toml`):
  - `openai`
  - `python-dotenv`
  - `pydub`
  - `audioop-lts`, which pydub needs on Python 3.13+ because `audioop` was removed from the standard library
- [ffmpeg](https://ffmpeg.org/), which pydub needs to read and write mp3s. It isn't a Python package, so install it separately:
  ```sh
  brew install ffmpeg        # macOS
  sudo apt install ffmpeg    # Debian/Ubuntu
  ```
- An OpenAI API key. Whisper usage is billed per minute of audio.

## Setup

Install the requirements above with whatever tool you use, then create a `.env` file in the project folder with your API key:

```
OPENAI_API_KEY=sk-...
```

`.env` is gitignored, so your key won't be committed.

## Usage

```sh
python main.py <path_to_file> <output_name>
```

Both arguments are required. Run the command from the project folder so the `.env` file is found.

- `path_to_file`: the mp3 to transcribe
- `output_name`: where to write the transcript, **without** `.txt`, which is added for you. This can be a path to another folder.

### Example

Transcribe an episode from your Downloads folder and keep the transcript in a `podcast_notes` folder:

```sh
python main.py ~/Downloads/podcast-name.mp3 ~/podcast_notes/podcast-name
```

This writes `~/podcast_notes/podcast-name.txt`. If `~/podcast_notes` doesn't exist yet, it's created for you.

While it runs, temporary chunk files (`podcast-name.mp3_1_ten.mp3`, `podcast-name.mp3_2_ten.mp3`, …) are created next to the original mp3. They're deleted once the transcript is written. If something fails before then, they're kept.

### Notes

- The output folder is created if it doesn't exist.
- If the output file already exists, it's overwritten.
