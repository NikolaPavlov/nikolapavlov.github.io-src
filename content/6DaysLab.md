Title: 6DaysLab
Date: 2016-09-01 12:55
Category: VulnHub CTF

**Boot2root machine for educational purposes
Our first boot2root machine, execute /flag to complete the game.
Try your skills against an environment protected by IDS and sandboxes!
“Our product Rashomon IPS is so good, even we use it!” they claim.
Hope you enjoy.**


Our target at 10.0.0.143.
Nmap scan:

![](images/6DaysLab/0_nmap.png)

Request the web server:

![](images/6DaysLab/01_web_server.png)

There is some type of difence on the form witch stop us to try SQLi, and there
is external link to the picture. The picture is vulnerable to local file
disclousere.

![](images/6DaysLab/1_lfi_passwd.png)

From nikto scan which we made early we knew there is config.php. Let's try to
get it with curl:

![](images/6DaysLab/2_lfi_config.png)

And this is the script running the form when we enter the promocode:

![](images/6DaysLab/3_lfi_checkpromo.png)

The checkpromo.php script look vulnerable to SQLi.
