
### whats_happening

![whats_happening](https://github.com/Hed6eH0g/ctf/blob/main/2023/wanictf/forensics/whats_happening/whats_happening_0.png)

First, we checked the format of the given file with `file updog` and it figured out that it is `updog: ISO 9660 CD-ROM filesystem data 'ISO Label'`.
We then tried to extract some information from the file with `strings, foremost, binwalk` though the file seems to be broken.
Fortunately, we could extract the picture included in the given data with `foremost -i updog` and the flag was drawn in the picture.
