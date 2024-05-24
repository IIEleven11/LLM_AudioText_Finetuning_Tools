# This script uses the whisperx command line tool to transcribe .wav files

import os
import subprocess
import glob

# Path to the directory containing the .wav files
wav_dir = "path/to/wav/files"


wav_files = glob.glob(os.path.join(wav_dir, "*.wav"))

# Iterate
for wav_file in wav_files:
    print(f"Processing file: {wav_file}")
    cmd = [
        "whisperx",
        wav_file,
        "--model",
        "large-v2",  # adjust this to the model you want to use
        "--align_model",
        "WAV2VEC2_ASR_LARGE_LV60K_960H",
    ]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error processing file {wav_file}: {e}")
