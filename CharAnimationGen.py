import cv2
import numpy as np
import math
import time
import os
import subprocess

ending = False

char_list = " .,-'`:!1+*abcdefghijklmnopqrstuvwxyz<>()/{}[]?234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ%&@#$"
len_char_list = len(char_list)

def process_frame(frame, target_width=180):
    height, width, _ = frame.shape  
    aspect_ratio = height / width
    target_height = int(target_width * aspect_ratio / 2) 

    frame_resize = cv2.resize(frame, (target_width, target_height))
    frame_gray = cv2.cvtColor(frame_resize, cv2.COLOR_BGR2GRAY)

    txt = ""
    height, width = frame_gray.shape

    for y in range(height):
        for x in range(width):
            pixel = frame_gray[y, x]
            normalized_pixel = math.log1p(pixel) / math.log1p(255.0)
            idx = int(normalized_pixel * len_char_list)
            if idx >= len_char_list:
                idx = len_char_list - 1
            txt += char_list[idx]
        txt += "\n"
    return txt

def play_video(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    video_duration = cap.get(cv2.CAP_PROP_FRAME_COUNT) / fps

   
    terminal_rows, terminal_columns = os.popen('stty size', 'r').read().split()
    terminal_columns = int(terminal_columns)

    
    audio_process = subprocess.Popen(["ffplay", "-nodisp", "-autoexit", video_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) 

    start_time = time.time()
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        txt = process_frame(frame, terminal_columns)

        
        print("\033c", end="")  
        print(txt)


        frame_count += 1
        elapsed_time = time.time() - start_time
        expected_time = frame_count / fps
        sleep_time = expected_time - elapsed_time
        if sleep_time > 0:
            time.sleep(sleep_time)

    audio_process.wait() 


def main():
    global ending
    video_path = input("Enter the video path: ")
    while ending == False:
        play =  input("Play video? (y/n): ")
        if play == "y" or "Y":
            play_video(video_path)
            ending = True
        else:
            print("Exiting...")
            ending = True

if __name__ == "__main__":
    main()