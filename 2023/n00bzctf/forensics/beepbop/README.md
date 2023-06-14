### BeepBop

![BeepBop](https://github.com/Hed6eH0g/ctf/blob/main/2023/n00bzctf/forensics/beepbop/beepbop_0.png)

Though checking the spectrum and the metadata with tools listed [here](https://0xrick.github.io/lists/stego) and SonicVisualizer, there was no clue for the flag.
Then, we reached [this post](https://www.chonky.net/hamradio/decoding-sstv-from-a-file-on-a-linux-system) during the survey concerning the way to visualize the sounds.
Based on the webpage, we installed PulseAudio, Qsstv, and VLC with apt command on kali and set up the configs as shown in the post, as a result, we got the flag.

Briefly, we conducted the following steps:
```
$ sudo apt instll pulseaudio qsstv vlc -y
$ pactl load-module module-null-sink sink_name=virtual-cable
$ pavucontrol
```
Then, check that `Null Output` is added in the "Output Devices" tab of the pop-upped volume control menu.

Next, start Qsstv and confirm that "Audio interfaces" in [Options] -> [Configuration] -> [Sounds] is set to PulseAudio.
Closing the configuration menu and switching back the volume control menu, change "Built-in Audio Analog Stereo" to "Monitor of Null Output" in [Recording] tab. 

Finally, start the receiver in the Qsstv and start the target wav file on VLC with "Null Output" option in [Audio] -> [Audio Device].

![flag](https://github.com/Hed6eH0g/ctf/blob/main/2023/n00bzctf/forensics/beepbop/beepbop_flag.png)