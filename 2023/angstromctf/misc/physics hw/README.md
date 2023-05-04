
### Physics HW

![physics_hw_chall](https://github.com/Hed6eH0g/ctf/blob/main/2023/angstromctf/misc/physics%20hw/physics_hw0.png)

This challenge gives us a PNG format file.
The content looks like a physics HW, however, the resolution seems to be a bit poor.
Since we could not figure out any crue for the challenge at a glance, we begin to gather information about the PNG file.
First, we check the property of the file with `exiftool`, however, the flag did not appear.
Second, we install `zsteg` from [here](https://github.com/zed-0xff/zsteg) which is used to detect stegano-hidden data in PNG & BMP.
Fortunately, it gave us the flag as follows.
```
b1,rgb,lsb,xy       .. text: "actf{physics_or_forensics}"
b2,r,msb,xy         .. text: "_UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU"
b2,g,msb,xy         .. text: "WUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU"
b2,b,msb,xy         .. text: ["U" repeated 239 times]
b2,rgb,msb,xy       .. text: ["U" repeated 204 times]
b2,bgr,msb,xy       .. text: "}]UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU"
b2,abgr,msb,xy      .. text: ["W" repeated 186 times]
b3,bgr,lsb,xy       .. file: very old 16-bit-int big-endian archive
b3,abgr,msb,xy      .. file: MPEG ADTS, layer I, v2,  96 kbps, Monaural
b3p,r,msb,xy        .. text: "_[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[["
b3p,g,msb,xy        .. text: ["[" repeated 233 times]
b3p,b,msb,xy        .. text: "{[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[["
b3p,rgb,msb,xy      .. text: "_[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[["
b3p,bgr,msb,xy      .. text: ["[" repeated 186 times]
b3p,abgr,lsb,xy     .. file: , 32 kHz, Monaural
b3p,abgr,msb,xy     .. text: ["_" repeated 187 times]
b4,r,msb,xy         .. text: ["w" repeated 221 times]
b4,g,msb,xy         .. text: ["w" repeated 221 times]
b4,b,msb,xy         .. text: ["w" repeated 222 times]
b4,rgb,msb,xy       .. text: ["w" repeated 152 times]
b4,bgr,msb,xy       .. text: ["w" repeated 151 times]
b5,g,msb,xy         .. file: MPEG ADTS, layer II, v1, Monaural
b5,bgr,lsb,xy       .. file: MPEG ADTS, layer II, v1, 384 kbps, JntStereo
b5p,r,msb,xy        .. text: ["o" repeated 221 times]
b5p,g,msb,xy        .. text: ["o" repeated 221 times]
b5p,b,msb,xy        .. text: ["o" repeated 222 times]
b5p,rgb,msb,xy      .. text: ["o" repeated 186 times]
b5p,bgr,lsb,xy      .. file: MPEG ADTS, layer I, v2, 24 kHz, Monaural
b5p,bgr,msb,xy      .. text: ["o" repeated 187 times]
b6,g,msb,xy         .. file: MPEG ADTS, layer I, v2, Monaural
b6,b,msb,xy         .. file: MPEG ADTS, layer I, v2, 112 kbps, Monaural
b6,abgr,msb,xy      .. file: ddis/ddif
b6p,r,msb,xy        .. text: ["_" repeated 221 times]
b6p,g,msb,xy        .. text: ["_" repeated 221 times]
b6p,b,msb,xy        .. text: ["_" repeated 222 times]
b6p,rgb,msb,xy      .. text: ["_" repeated 186 times]
b7,r,lsb,xy         .. file: AIX core file fulldump 32-bit
b7,g,lsb,xy         .. file: , Monaural
b7,b,lsb,xy         .. file: , 48 kHz, Monaural
b7p,r,msb,xy        .. text: ["?" repeated 221 times]
b7p,g,msb,xy        .. text: ["?" repeated 221 times]
b7p,b,msb,xy        .. text: ["?" repeated 222 times]
b7p,rgb,msb,xy      .. text: ["?" repeated 186 times]
b7p,bgr,lsb,xy      .. file: MPEG ADTS, layer II, v1, Monaural
b7p,bgr,msb,xy      .. text: ["?" repeated 187 times]
b8,r,msb,xy         .. file: RDI Acoustic Doppler Current Profiler (ADCP)
b8,bgr,msb,xy       .. file: ddis/ddif
b2,r,msb,xy,prime   .. text: ["U" repeated 251 times]
b2,g,msb,xy,prime   .. text: "wUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU"
b2,b,msb,xy,prime   .. text: "}UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU"
b2,rgb,msb,xy,prime .. text: "WUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU"
b2,bgr,msb,xy,prime .. text: "WUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU"
b2,abgr,msb,xy,prime.. text: ["W" repeated 237 times]
b3,g,msb,xy,prime   .. file: MPEG ADTS, layer I, v2, Monaural
b3p,r,msb,xy,prime  .. text: "_[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[["
b3p,g,msb,xy,prime  .. text: "{_[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[["
b3p,b,msb,xy,prime  .. text: "_[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[["
b3p,rgb,msb,xy,prime.. text: ["[" repeated 237 times]
b3p,bgr,msb,xy,prime.. text: ["[" repeated 237 times]
b3p,abgr,msb,xy,prime.. text: ["_" repeated 237 times]
b4,r,msb,xy,prime   .. text: ["w" repeated 246 times]
b4,g,msb,xy,prime   .. text: ["w" repeated 246 times]
b4,b,msb,xy,prime   .. text: ["w" repeated 246 times]
b4,rgb,msb,xy,prime .. text: ["w" repeated 227 times]
b4,bgr,msb,xy,prime .. text: ["w" repeated 227 times]
b4,abgr,msb,xy,prime.. file: RDI Acoustic Doppler Current Profiler (ADCP)
b5,g,lsb,xy,prime   .. file: MPEG ADTS, layer II, v1, 384 kbps, Monaural
b5,abgr,msb,xy,prime.. file: MPEG ADTS, layer II, v1, 48 kHz, Monaural
b5p,r,msb,xy,prime  .. text: ["o" repeated 246 times]
b5p,g,lsb,xy,prime  .. file: MPEG ADTS, layer I, v2, Monaural
b5p,g,msb,xy,prime  .. text: ["o" repeated 246 times]
b5p,b,msb,xy,prime  .. text: ["o" repeated 246 times]
b5p,rgb,msb,xy,prime.. text: ["o" repeated 237 times]
b5p,bgr,msb,xy,prime.. text: ["o" repeated 237 times]
b5p,abgr,msb,xy,prime.. file: RDI Acoustic Doppler Current Profiler (ADCP)
b6,abgr,msb,xy,prime.. file: MPEG ADTS, layer I, v2, 112 kbps, Monaural
b6p,r,msb,xy,prime  .. text: ["_" repeated 246 times]
b6p,g,lsb,xy,prime  .. file: , Monaural
b6p,g,msb,xy,prime  .. text: ["_" repeated 246 times]
b6p,b,msb,xy,prime  .. text: ["_" repeated 246 times]
b6p,rgb,msb,xy,prime.. text: ["_" repeated 237 times]
b7,abgr,lsb,xy,prime.. file: , Monaural
b7p,r,msb,xy,prime  .. text: ["?" repeated 246 times]
b7p,g,lsb,xy,prime  .. file: MPEG ADTS, layer II, v1, Monaural
b7p,g,msb,xy,prime  .. text: ["?" repeated 246 times]
b7p,b,msb,xy,prime  .. text: ["?" repeated 246 times]
b7p,rgb,msb,xy,prime.. text: ["?" repeated 237 times]
b7p,bgr,msb,xy,prime.. text: ["?" repeated 237 times]
b8,g,msb,xy,prime   .. file: ddis/ddif
b8,rgb,lsb,xy,prime .. file: AIX core file fulldump 64-bit
b8,bgr,lsb,xy,prime .. file: AIX core file fulldump 64-bit
b2,r,msb,yx         .. file: VISX image file
b2,g,msb,yx         .. text: "WUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU"
b2,rgb,msb,yx       .. text: "}UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU"
b2,bgr,msb,yx       .. text: "_UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU"
b2,abgr,msb,yx      .. text: ["W" repeated 255 times]
b3,bgr,lsb,yx       .. file: very old 16-bit-int big-endian archive
b3,abgr,msb,yx      .. file: MPEG ADTS, layer I, v2,  96 kbps, Monaural
b3p,r,msb,yx        .. text: ["[" repeated 195 times]
b3p,g,msb,yx        .. text: "_[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[["
b3p,rgb,msb,yx      .. text: ["[" repeated 255 times]
b3p,bgr,msb,yx      .. text: ["[" repeated 255 times]
b3p,abgr,lsb,yx     .. file: , 32 kHz, Monaural
b3p,abgr,msb,yx     .. text: ["_" repeated 255 times]
b4,g,msb,yx         .. text: ["w" repeated 255 times]
b4,rgb,msb,yx       .. text: ["w" repeated 254 times]
b4,bgr,msb,yx       .. text: ["w" repeated 255 times]
b5,bgr,lsb,yx       .. file: MPEG ADTS, layer II, v1, 384 kbps, JntStereo
b5p,g,msb,yx        .. text: ["o" repeated 255 times]
b5p,rgb,msb,yx      .. text: ["o" repeated 255 times]
b5p,bgr,lsb,yx      .. file: MPEG ADTS, layer I, v2, 24 kHz, Monaural
b5p,bgr,msb,yx      .. text: ["o" repeated 255 times]
b6,g,msb,yx         .. file: MPEG ADTS, layer I, v2, 112 kbps, Monaural
b6,abgr,msb,yx      .. file: ddis/ddif
b6p,g,msb,yx        .. text: ["_" repeated 255 times]
b6p,rgb,msb,yx      .. text: ["_" repeated 255 times]
b7,g,lsb,yx         .. file: , 48 kHz, Monaural
b7p,g,msb,yx        .. text: ["?" repeated 255 times]
b7p,rgb,msb,yx      .. text: ["?" repeated 255 times]
b7p,bgr,lsb,yx      .. file: MPEG ADTS, layer II, v1, Monaural
b7p,bgr,msb,yx      .. text: ["?" repeated 255 times]
b8,bgr,msb,yx       .. file: ddis/ddif
b2,r,msb,yx,prime   .. file: VISX image file
b2,rgb,msb,yx,prime .. file: VISX image file
b2,abgr,msb,yx,prime.. text: ["W" repeated 106 times]
b3p,r,msb,yx,prime  .. text: ["[" repeated 35 times]
b3p,rgb,msb,yx,prime.. text: ["[" repeated 106 times]
b3p,abgr,lsb,yx,prime.. file: MIT scheme (library?)
b3p,abgr,msb,yx,prime.. text: ["_" repeated 106 times]
b4,r,msb,yx,prime   .. text: ["w" repeated 53 times]
b4,rgb,msb,yx,prime .. text: ["w" repeated 159 times]
b5p,r,lsb,yx,prime  .. file: PC formatted floppy with no filesystem
b5p,r,msb,yx,prime  .. text: ["o" repeated 53 times]
b5p,rgb,lsb,yx,prime.. file: PC formatted floppy with no filesystem
b5p,rgb,msb,yx,prime.. text: ["o" repeated 106 times]
b5p,abgr,msb,yx,prime.. file: RDI Acoustic Doppler Current Profiler (ADCP)
b6,abgr,msb,yx,prime.. file: MPEG ADTS, layer I, v2, 112 kbps, Monaural
b6p,r,lsb,yx,prime  .. file: MIT scheme (library?)
b6p,r,msb,yx,prime  .. text: ["_" repeated 53 times]
b7,abgr,lsb,yx,prime.. file: , 48 kHz, Monaural
b7p,r,msb,yx,prime  .. text: ["?" repeated 53 times]
b7p,rgb,msb,yx,prime.. text: ["?" repeated 106 times]
b8,rgba,msb,yx,prime.. file: RDI Acoustic Doppler Current Profiler (ADCP)
b2,r,msb,YX         .. text: "TUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU"
b2,rgb,msb,YX       .. text: "@UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU"
b2,abgr,msb,YX      .. text: ["W" repeated 203 times]
b3p,r,msb,YX        .. text: "@[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[["
b3p,rgb,msb,YX      .. text: ["[" repeated 203 times]
b3p,abgr,msb,YX     .. text: ["_" repeated 203 times]
b4,r,msb,YX         .. text: "pwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"
b4,rgb,msb,YX       .. text: "pwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"
b5p,r,msb,YX        .. text: "`ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo"
b5p,rgb,msb,YX      .. text: ["o" repeated 203 times]
b6p,r,msb,YX        .. text: "@_____________________________________________________________________________________________________________________________________________________________________________________________________________________________________"
b7p,r,msb,YX        .. text: ["?" repeated 229 times]
b7p,rgb,msb,YX      .. text: ["?" repeated 203 times]
b1,a,lsb,YX,prime   .. file: raw G3 (Group 3) FAX, byte-padded
b1,abgr,msb,YX,prime.. file: GLS_BINARY_MSB_FIRST
b2,r,msb,YX,prime   .. text: "@UUUUUUUUUUUUUUUUUUUUUUUU"
b2,rgb,msb,YX,prime .. text: "TUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU"
b2,abgr,msb,YX,prime.. text: ["W" repeated 100 times]
b3p,r,msb,YX,prime  .. text: ["[" repeated 33 times]
b3p,rgb,msb,YX,prime.. text: ["[" repeated 100 times]
b3p,abgr,msb,YX,prime.. text: ["_" repeated 100 times]
b4,r,msb,YX,prime   .. text: "pwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"
b4,rgb,msb,YX,prime .. text: "pwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"
b5p,r,msb,YX,prime  .. text: "`ooooooooooooooooooooooooooooooooooooooooooooooooo"
b5p,rgb,msb,YX,prime.. text: ["o" repeated 100 times]
b6p,r,msb,YX,prime  .. text: "@_________________________________________________"
b7p,r,msb,YX,prime  .. text: ["?" repeated 50 times]
b7p,rgb,msb,YX,prime.. text: ["?" repeated 100 times]
b2,r,msb,Xy         .. file: VISX image file
b2,g,msb,Xy         .. file: VISX image file
b2,b,msb,Xy         .. file: VISX image file
b3p,r,msb,Xy        .. text: ["[" repeated 141 times]
b3p,g,msb,Xy        .. text: ["[" repeated 142 times]
b3p,b,msb,Xy        .. text: "[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[{"
b4,r,msb,Xy         .. text: ["w" repeated 212 times]
b4,g,msb,Xy         .. text: ["w" repeated 213 times]
b4,b,msb,Xy         .. text: ["w" repeated 213 times]
b5p,r,lsb,Xy        .. file: PC formatted floppy with no filesystem
b5p,r,msb,Xy        .. text: ["o" repeated 212 times]
b5p,g,lsb,Xy        .. file: PC formatted floppy with no filesystem
b5p,g,msb,Xy        .. text: ["o" repeated 213 times]
b5p,b,lsb,Xy        .. file: PC formatted floppy with no filesystem
b5p,b,msb,Xy        .. text: ["o" repeated 213 times]
b6p,r,lsb,Xy        .. file: MIT scheme (library?)
b6p,r,msb,Xy        .. text: ["_" repeated 212 times]
b6p,g,lsb,Xy        .. file: MIT scheme (library?)
b6p,g,msb,Xy        .. text: ["_" repeated 213 times]
b6p,b,lsb,Xy        .. file: MIT scheme (library?)
b6p,b,msb,Xy        .. text: ["_" repeated 213 times]
b7p,r,msb,Xy        .. text: ["?" repeated 212 times]
b7p,g,msb,Xy        .. text: ["?" repeated 213 times]
b7p,b,msb,Xy        .. text: ["?" repeated 213 times]
b2,r,msb,Xy,prime   .. file: VISX image file
b2,g,msb,Xy,prime   .. file: VISX image file
b2,b,msb,Xy,prime   .. file: VISX image file
b2,rgb,msb,Xy,prime .. file: VISX image file
b2,bgr,msb,Xy,prime .. file: VISX image file
b2,abgr,msb,Xy,prime.. text: ["W" repeated 82 times]
b3p,r,msb,Xy,prime  .. text: ["[" repeated 27 times]
b3p,g,msb,Xy,prime  .. text: "[[[[[[[[[[[[[[[[[[[[[[[[[[[{"
b3p,b,msb,Xy,prime  .. text: ["[" repeated 27 times]
b3p,rgb,msb,Xy,prime.. text: ["[" repeated 82 times]
b3p,bgr,msb,Xy,prime.. text: ["[" repeated 82 times]
b3p,abgr,lsb,Xy,prime.. file: MIT scheme (library?)
b3p,abgr,msb,Xy,prime.. text: ["_" repeated 82 times]
b4,r,msb,Xy,prime   .. text: ["w" repeated 41 times]
b4,g,msb,Xy,prime   .. text: ["w" repeated 41 times]
b4,b,msb,Xy,prime   .. text: ["w" repeated 41 times]
b4,rgb,msb,Xy,prime .. text: ["w" repeated 123 times]
b4,bgr,msb,Xy,prime .. text: ["w" repeated 123 times]
b5p,r,lsb,Xy,prime  .. file: PC formatted floppy with no filesystem
b5p,r,msb,Xy,prime  .. text: ["o" repeated 41 times]
b5p,g,lsb,Xy,prime  .. file: PC formatted floppy with no filesystem
b5p,g,msb,Xy,prime  .. text: ["o" repeated 41 times]
b5p,b,lsb,Xy,prime  .. file: PC formatted floppy with no filesystem
b5p,b,msb,Xy,prime  .. text: ["o" repeated 41 times]
b5p,rgb,lsb,Xy,prime.. file: PC formatted floppy with no filesystem
b5p,rgb,msb,Xy,prime.. text: ["o" repeated 82 times]
b5p,bgr,lsb,Xy,prime.. file: PC formatted floppy with no filesystem
b5p,bgr,msb,Xy,prime.. text: ["o" repeated 82 times]
b5p,abgr,msb,Xy,prime.. file: RDI Acoustic Doppler Current Profiler (ADCP)
b6,abgr,msb,Xy,prime.. file: MPEG ADTS, layer I, v2, 112 kbps, Monaural
b6p,r,lsb,Xy,prime  .. file: MIT scheme (library?)
b6p,r,msb,Xy,prime  .. text: ["_" repeated 41 times]
b6p,g,lsb,Xy,prime  .. file: MIT scheme (library?)
b6p,g,msb,Xy,prime  .. text: ["_" repeated 41 times]
b6p,b,lsb,Xy,prime  .. file: MIT scheme (library?)
b6p,b,msb,Xy,prime  .. text: ["_" repeated 41 times]
b6p,rgb,lsb,Xy,prime.. file: MIT scheme (library?)
b6p,rgb,msb,Xy,prime.. text: ["_" repeated 82 times]
b7p,r,msb,Xy,prime  .. text: ["?" repeated 41 times]
b7p,g,msb,Xy,prime  .. text: ["?" repeated 41 times]
b7p,b,msb,Xy,prime  .. text: ["?" repeated 41 times]
b7p,rgb,msb,Xy,prime.. text: ["?" repeated 82 times]
b7p,bgr,msb,Xy,prime.. text: ["?" repeated 82 times]
b8,r,msb,Xy,prime   .. file: RDI Acoustic Doppler Current Profiler (ADCP)
b8,g,msb,Xy,prime   .. file: RDI Acoustic Doppler Current Profiler (ADCP)
b8,rgb,msb,Xy,prime .. file: RDI Acoustic Doppler Current Profiler (ADCP)
b8,bgr,msb,Xy,prime .. file: RDI Acoustic Doppler Current Profiler (ADCP)
b2,g,msb,Yx         .. text: "TUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU"
b3p,g,msb,Yx        .. text: "@[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[["
b2,r,msb,Yx,prime   .. text: "@UUUUUUUUUUUUUUUUUUUUUUUU"
b3p,r,msb,Yx,prime  .. text: ["[" repeated 33 times]
```
