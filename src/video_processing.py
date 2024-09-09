import cv2
import os
from preprocessing import create_directories, preprocess_frame
from segmentation import segment_text1, segment_text2, segment_text3

def main():
    video_path = 'input_video.mp4'
    base_directory = 'output'
    subfolders = ['frames', 'processing-frames', 'segmented-frames']
    
    create_directories(base_directory, subfolders)

    output_folder = os.path.join(base_directory, subfolders[0])
    processed_folder = os.path.join(base_directory, subfolders[1])
    segmented_folder = os.path.join(base_directory, subfolders[2])

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error opening video file: {video_path}")
        return

    frame_idx = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        original_frame_path = f"{output_folder}/frame_{frame_idx:04d}.jpg"
        cv2.imwrite(original_frame_path, frame)

        gray_frame, blurred_frame, binary_frame = preprocess_frame(frame)
        cv2.imwrite(f"{processed_folder}/gray_frame_{frame_idx:04d}.jpg", gray_frame)
        cv2.imwrite(f"{processed_folder}/blurred_frame_{frame_idx:04d}.jpg", blurred_frame)
        cv2.imwrite(f"{processed_folder}/thresholded_frame_{frame_idx:04d}.jpg", binary_frame)

        segmented_frame = segment_text1(frame)
        segmented_frame = segment_text2(segmented_frame)
        segmented_frame = segment_text3(segmented_frame)

        cv2.imwrite(f"{segmented_folder}/segmented_frame_{frame_idx:04d}.jpg", segmented_frame)
        frame_idx += 1

    cap.release()

    # Create video from segmented frames
    segmented_filenames = sorted(os.listdir(segmented_folder))
    output_video_filename = os.path.join(base_directory, 'output_video.mp4')
    first_frame = cv2.imread(os.path.join(segmented_folder, segmented_filenames[0]))
    height, width, _ = first_frame.shape

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_video = cv2.VideoWriter(output_video_filename, fourcc, 30, (width, height))

    for filename in segmented_filenames:
        frame_path = os.path.join(segmented_folder, filename)
        frame = cv2.imread(frame_path)
        output_video.write(frame)

    output_video.release()
    print(f"Video created successfully: {output_video_filename}")

if __name__ == "__main__":
    main()
