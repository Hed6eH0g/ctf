
### Just_mp4

![just_mp4](https://github.com/Hed6eH0g/ctf/blob/main/2023/wanictf/forensics/just_mp4/just_mp4_0.png)

First, we examined `strings chall.mp4 | grep FLAG` but any information could not find.
Then, applying `exiftool` gave us the base64 encoded flag as follows:
```
$ exiftool chall.mp4

ExifTool Version Number         : 12.57
File Name                       : chall.mp4
Directory                       : .
File Size                       : 152 kB
File Modification Date/Time     : 2021:05:03 00:00:00-07:00
File Access Date/Time           : 2023:05:05 04:24:22-07:00
File Inode Change Date/Time     : 2023:05:05 04:24:07-07:00
File Permissions                : -rw-r--r--
File Type                       : MP4
File Type Extension             : mp4
MIME Type                       : video/mp4
Major Brand                     : MP4 v2 [ISO 14496-14]
Minor Version                   : 0.0.0
Compatible Brands               : mp41, isom
Media Data Size                 : 151250
Media Data Offset               : 71
Movie Header Version            : 0
Create Date                     : 2023:04:26 13:09:50
Modify Date                     : 2023:04:26 13:09:50
Time Scale                      : 30000
Duration                        : 1.00 s
Preferred Rate                  : 1
Preferred Volume                : 100.00%
Preview Time                    : 0 s
Preview Duration                : 0 s
Poster Time                     : 0 s
Selection Time                  : 0 s
Selection Duration              : 0 s
Current Time                    : 0 s
Next Track ID                   : 2
Track Header Version            : 0
Track Create Date               : 2023:04:26 13:09:50
Track Modify Date               : 2023:04:26 13:09:50
Track ID                        : 1
Track Duration                  : 1.00 s
Track Layer                     : 0
Track Volume                    : 0.00%
Matrix Structure                : 1 0 0 0 1 0 0 0 1
Image Width                     : 512
Image Height                    : 512
Media Header Version            : 0
Media Create Date               : 2023:04:26 13:09:50
Media Modify Date               : 2023:04:26 13:09:50
Media Time Scale                : 30000
Media Duration                  : 1.00 s
Media Language Code             : und
Handler Description             : VideoHandler
Graphics Mode                   : srcCopy
Op Color                        : 0 0 0
Compressor ID                   : avc1
Source Image Width              : 512
Source Image Height             : 512
X Resolution                    : 72
Y Resolution                    : 72
Compressor Name                 : AVC Coding
Bit Depth                       : 24
Video Frame Rate                : 30
Handler Type                    : Metadata
Publisher                       : flag_base64:RkxBR3tINHYxbl9mdW5fMW5uMXR9
Image Size                      : 512x512
Megapixels                      : 0.262
Avg Bitrate                     : 1.21 Mbps
Rotation                        : 0
```

Thus, we can decode it with the `base64` command to obtain the flag.
```
echo "RkxBR3tINHYxbl9mdW5fMW5uMXR9" | base64 -d
```
