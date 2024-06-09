
# COnvert TensorFlow events.out.tfevent file to a json

import os
import json
import numpy as np
from tensorboard.backend.event_processing.event_accumulator import EventAccumulator


def tabulate_events(dpath):
    final_out = {}
    for dname in os.listdir(dpath):
        print(f"Converting run {dname}", end="")
        ea = EventAccumulator(os.path.join(dpath, dname)).Reload()
        tags = ea.Tags()["scalars"]

        out = {}
        for tag in tags:
            tag_values = []
            wall_time = []
            steps = []

            for event in ea.Scalars(tag):
                tag_values.append(event.value)
                wall_time.append(event.wall_time)
                steps.append(event.step)

            out[tag] = {"steps": steps, "values": tag_values, "wall_time": wall_time}

        if len(tags) > 0:
            with open(f"{dname}.json", "w") as f:
                json.dump(out, f)
            print("- Done")
        else:
            print("- No scalars to write")

        final_out[dname] = out

    return final_out


if __name__ == "__main__":
    path = r"E:\trmp\tools\srt"
    steps = tabulate_events(path)
    with open("all_result.json", "w") as f:
        json.dump(steps, f)
