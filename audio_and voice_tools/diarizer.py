# diarizers are mediocre at best. This implementation is no different. Use at your own risk

import json
from pydub import AudioSegment

# Paths to the files
audio_path = r"path\to\wav\.wav"
json_path = r"path\to\json\.json"

audio = AudioSegment.from_wav(audio_path)

import json
import re


def time_to_milliseconds(time_str):
    match = re.match(r"(\d+):(\d+):(\d+\.\d+)", time_str)
    if not match:
        raise ValueError(f"Invalid time format: {time_str}")

    hours, minutes, seconds = match.groups()
    total_seconds = int(hours) * 3600 + int(minutes) * 60 + float(seconds)
    return int(total_seconds * 1000)



with open("output.json", "r") as file:
    data = json.load(file)


for segment in data["segments"]:
    start_time = time_to_milliseconds(segment["start"])
    stop_time = time_to_milliseconds(segment["stop"])
    print(
        f"Speaker: {segment['speaker']}, Start: {start_time} ms, Stop: {stop_time} ms"
    )

output_audio = AudioSegment.silent(duration=0)


for segment in segment:

    if (
        "speaker" in segment and segment["speaker"] == "B"
    ):  # change to the speaker you want to extract
        start_time = int(float(segment["start"]) * 1000)
        end_time = int(float(segment["end"]) * 1000)

        speaker_segment = audio[start_time:end_time]

        output_audio += speaker_segment
        break

# Export the result
output_audio.export(
    r"path\to\output\wavfile.wav",  # change to the path where you want to save the output
    format="wav",
)
