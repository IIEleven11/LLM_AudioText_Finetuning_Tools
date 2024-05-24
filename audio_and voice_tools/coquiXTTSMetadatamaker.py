# This script is used to generate metadata files for training and evaluation from a directory of audio files. This is the one directly taken from coqui's formatter.py

import os

# Define the path to your audio files directory
audio_dir = "E:/trmp/xtts-trainer-no-ui-auto/finetune_models/dataset/segmentedAudionew/"


audio_types = (".wav", ".mp3", ".flac")


audio_files = [
    os.path.join(audio_dir, file)
    for file in os.listdir(audio_dir)
    if file.endswith(audio_types)
]
out_path = "E:/trmp/xtts-trainer-no-ui-auto/finetune_models/dataset/segmentedAudionew/"


def format_audio_list(
    audio_files,
    target_language="en",
    whisper_model="large-v3",
    out_path=None,
    speaker_name="coqui",
    eval_percentage=0.15,
):

    train_metadata_path, eval_metadata_path, audio_total_size, lang_file_path = (
        format_audio_list(
            audio_files,
            target_language=target_language,
            whisper_model=whisper_model,
            out_path=out_path,
            speaker_name=speaker_name,
            eval_percentage=eval_percentage,
        )
    )

    print(f"Training metadata saved to: {train_metadata_path}")
    print(f"Evaluation metadata saved to: {eval_metadata_path}")
    print(f"Total audio size: {audio_total_size} seconds")
    print(f"Language file saved to: {lang_file_path}")
