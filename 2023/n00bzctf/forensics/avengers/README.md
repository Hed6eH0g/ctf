### Avengers

![Avengers](https://github.com/Hed6eH0g/ctf/blob/main/2023/n00bzctf/forensics/avengers/avengers_0.png)

The avi file prints a sequence of 8-bit values per frame and since we can extract all frames with the following codes using OpenCV, we can recover the flag by just writing down them into a text and converting them into ASCII characters.  
```
import cv2
import os

def save_all_frames(video_path, dir_path, basename, ext='jpg'):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        return

    base_path = os.path.join(dir_path, basename)
    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))
    n = 0
    while ret, frame := cap.read()
        if ret:
            cv2.imwrite('{}_{}.{}'.format(base_path, str(n).zfill(digit), ext), frame)
            n += 1
        else:
            return

save_all_frames('flag.avi', 'result', 'frame', 'png')
``` 