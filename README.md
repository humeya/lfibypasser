# lfibypasser
A simple script aimed to achieve a LFI, bypassing  some security restrictions. 
It will perform a double encoding on your payload, so you can reach the server bypassing security measures if you're lucky enough.

Usage: lfibypasser.py url-including-vulnerable-parameter payload
Example: lfibypasser.py http://notsosecureweb?vulnparam= ../../../../etc/passwd

*Disclaimer: Yeah, I know. No cookies support, not the best parsing out there, only one type of encoding available. It's useful for me and that's enough for now.*
