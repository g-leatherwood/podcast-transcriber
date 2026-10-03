import sys

from file_transform import delete_files
from whisper import get_file, transcribe_audio

if len(sys.argv) != 3:
    print("Usage: python main.py <path_to_file> <output_name>")
    sys.exit(1)

input_file = sys.argv[1]
output_name = sys.argv[2]


def main():
    """
    Splits the input file into chunks,
    transcribes them to output_name.txt,
    then deletes the chunks.
    """
    files = get_file(input_file)
    transcribe_audio(files, output_name)
    delete_files(files)


if __name__ == "__main__":
    main()
