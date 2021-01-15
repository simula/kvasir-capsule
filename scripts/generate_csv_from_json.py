import json
import glob
import os
import argparse
import time

_DEFAULT_DATASET_DIR_PATH = "D:\\Documents\\output_vvs_2020\\labeled"
_DEFAULT_METADATA_PATH = "C:\\Users\\Steven\\github\\kvasir-capsule\\metadata.json"

_DEFAULT_WORK_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

_ANATOMY_CLASSES = [
    "Pylorus",
    "Ileocecal valve",
    "Ampulla of Vater"
]

_LUMINAL_CLASSES = [
    "Normal clean mucosa",
    "Reduced mucosal view",
    "Blood - fresh",
    "Blood - hematin",
    "Erythema",
    "Foreign body",
    "Angiectasia",
    "Erosion",
    "Ulcer",
    "Polyp",
    "Lymphangiectasia"
]

argument_parser = argparse.ArgumentParser(description="")

argument_parser.add_argument("-d", "--dataset-dir", type=str, default=_DEFAULT_DATASET_DIR_PATH)
argument_parser.add_argument("-m", "--metadata-file", type=str, default=_DEFAULT_METADATA_PATH)
argument_parser.add_argument("-o", "--output-file", type=str, default=os.path.join(_DEFAULT_WORK_DIR, "metadata.csv"))

def match_sequence(path, start, end):
    frame_number = int(os.path.splitext(os.path.basename(path).split("_")[1])[0])
    if frame_number >= start and frame_number <= end:
        return True
    return False

def match_frame_id(path, match):
    return os.path.splitext(os.path.basename(path).split("_")[-1])[0] == match

def clean_metadata_json(dataset_dir_path, metadata_file_path, output_file_path):

    all_video_frames = list(glob.glob(os.path.join(dataset_dir_path, "*", "*")))
    timer = time.time()

    with open(metadata_file_path) as f:
        metadata = json.load(f)

    with open(output_file_path, mode="w") as f:

        f.write("filename;video_id;frame_number;finding_category;finding_class;x1;y1;x2;y2;x3;y3;x4;y4\n")

        for video_id, video_data in metadata.items():

            print("Reading video with ID %s..." % video_id)

            video_specific_frames = list(filter(
                lambda x: os.path.basename(x).split("_")[0] == video_id, all_video_frames
            ))

            for segment_id, segment_data in video_data["segments"].items():
                
                for seen_segment in segment_data["seen"]:

                    start_frame = seen_segment[0]
                    end_frame = seen_segment[1]
                    
                    segment_class = segment_data["metadata"]["pillcam_subtype"]
                    if segment_class is None:
                        segment_class = segment_data["metadata"]["segment_type"]
                    segment_category = "Anatomy" if segment_class in _ANATOMY_CLASSES else "Luminal"

                    segment_frames = list(filter(
                        lambda x: match_sequence(x, start_frame, end_frame), video_specific_frames
                    ))

                    segment_frames = sorted(
                        segment_frames,
                        key=lambda x: int(os.path.splitext(os.path.basename(x).split("_")[1])[0])
                    )
                    
                    for frame in segment_frames:
                        frame_id = os.path.splitext(os.path.basename(frame))[0].split("_")[-1]
                        f.write("%s;%s;%s;%s;%s;;;;;;;\n" % (os.path.basename(frame), video_id, frame_id, segment_category, segment_class))
                
            for finding_id, finding_data in video_data["findings"].items():
                
                finding_class = finding_data["metadata"]["pillcam_subtype"]
                finding_category = "Anatomy" if finding_class in _ANATOMY_CLASSES else "Luminal"
                
                for frame_id, frame_data in finding_data["frames"].items():

                    frame = filter(lambda x: match_frame_id(x, frame_id), video_specific_frames)
                    frame = list(frame)

                    if len(frame) <= 0:
                        print("Missing frames for %s!" % video_id)
                        continue

                    f.write("%s;%s;%s;%s;%s" % (os.path.basename(frame[0]), video_id, frame_id, finding_category, finding_class))

                    for box in frame_data["shape"]:
                        f.write(";%s;%s" % (int(box["x"]), int(box["y"])))

                    f.write("\n")

    print("Finished after %s seconds!" % int(time.time() - timer))

if __name__ == "__main__":

    args = argument_parser.parse_args()

    clean_metadata_json(
        dataset_dir_path=args.dataset_dir,
        metadata_file_path=args.metadata_file,
        output_file_path=args.output_file
    )