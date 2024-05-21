# Concatenates the segments of a WAV file corresponding to a specific speaker based on a text file with timestamps and speaker labels.

from pydub import AudioSegment
import re

# Path to the original WAV file and the text file
wav_path = r"path\to\wav\.wav"
txt_path = r"path\to\txt\.txt"

# Load the original WAV file
audio = AudioSegment.from_wav(wav_path)


# Function to parse time in the format [hh:mm:ss.xxx]
def parse_time(time_str):
    parts = re.split("[:.]", time_str)
    return (
        int(parts[0]) * 3600000
        + int(parts[1]) * 60000
        + int(parts[2]) * 1000
        + int(parts[3])
    )


segments = []
with open(txt_path, "r") as file:
    for line in file:
        match = re.match(
            r"\[\s*(\d{2}:\d{2}:\d{2}\.\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2}\.\d{3})\]\s*\w+\s*SPEAKER_02",  # change SPEAKER_02 to the speaker you want to extract
            line,
        )
        if match:
            start_time = parse_time(match.group(1))
            end_time = parse_time(match.group(2))
            segments.append((start_time, end_time))

# Extract and concatenate segments
speaker_02_audio = AudioSegment.empty()  # change to the speaker you want to extract
for start, end in segments:
    speaker_02_audio += audio[start:end]


output_path = r"output\path\wavfile.wav"  # path to wav file to save
speaker_02_audio.export(output_path, format="wav")

print(f"New WAV file with only SPEAKER_01 segments saved to {output_path}")
