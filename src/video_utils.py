"""
Functions to be implemented:
- save_video(file: str) -> str:
- crop_video(video_path: str, start_time: float, end_time: float) -> str:
"""

import cv2
import os

def extract_first_frame(video_path: str) -> str | None:
    """Extract the first frame from a video file and save it as an image."""
    video_capture = cv2.VideoCapture(video_path)
    success, frame = video_capture.read()
    
    if success:
        frame_path = os.path.join(FRAME_FOLDER, 'frame1.jpg')
        cv2.imwrite(frame_path, frame)  # Save the first frame as an image
        video_capture.release()
        return 'frame1.jpg'
    else:
        video_capture.release()
        return None
