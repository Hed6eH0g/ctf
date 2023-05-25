
### What does the cougar say?

![what does the cougar say](https://github.com/Hed6eH0g/ctf/blob/main/2023/byuctf/forencics/what_does_the_cougar_say/figs/what_does_the_cougar_say_0.png)


Since an mp4 file was given, a brief look at the contents allows us to find that there are a few different frames in the movie.
Thus, extracting each frame in the video with `ffmpeg -i baby_cougar.mp4 -vcodec png ffmpeg_png/outpu_%06d.png` gives the following image.
![flag1](https://github.com/Hed6eH0g/ctf/blob/main/2023/byuctf/forencics/what_does_the_cougar_say/figs/ffmpeg.png)

But it was not the correct flag.
So, we reviewed the statement "What does the cougar say?" and tried to analyze the sounds in the video.
[Sonic Visualizer](https://www.sonicvisualiser.org/) is a convenient freeware to analyze sounds such as spectrum.
Since it could not import an mp4 file on kali in our case, we converted it into wav format with `ffmpeg -i baby_cougar.mp4 -ac 2 -f wav baby_cougar.wav`.

Sometimes flags were embedded into the spectrum of sounds, we also began to check it in this time.
It can be done by following [Pane] in the toolbar > [Add Spectrogram] > [baby_cougar.wav: Channel1] after launching the Sonic Visualizer and importing the wav file.
Then, one can find the remaining part of the flag below.
![flag2](https://github.com/Hed6eH0g/ctf/blob/main/2023/byuctf/forencics/what_does_the_cougar_say/figs/sonic_visualizer.png)
