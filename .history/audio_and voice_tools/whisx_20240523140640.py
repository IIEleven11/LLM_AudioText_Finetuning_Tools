import os
import subprocess
import glob

# Path to the directory containing the .wav files
wav_dir = "/mnt/e/trmp/xtts-trainer-no-ui-auto/whisperxx"

# Get a list of all .wav files in the directory
wav_files = glob.glob(os.path.join(wav_dir, "*.wav"))

# Iterate over each .wav file and process it with whisperx
for wav_file in wav_files:
    print(f"Processing file: {wav_file}")
    cmd = [
        "whisperx",
        wav_file,
        "--model",
        "large-v2",
        "--align_model",
        "WAV2VEC2_ASR_LARGE_LV60K_960H",
    ]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error processing file {wav_file}: {e}")
