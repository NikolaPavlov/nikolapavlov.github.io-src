Title: Mr Robot CTF
Date: 2016-07-13 11:00
Category: VulnHub CTF


**This is a Mr.Robot challenge from vulnhub.com. You can obtain the virtual machine from:
[here](https://www.vulnhub.com/entry/mr-robot-1,151/)**

First lets find the target in our network:

![netdiscover target](images/1_netdiscover.png)

Our target machine is 10.0.0.135, lets run nmap scan on it:

![nmap scan target](images/2_nmap.png)

Nothing interesting just web server, and close ssh port 22.
Browse the target and run nikto on the web server.

![nikto scan target](images/3_nikto.png)
The site is wordpress. The interesting things are in red.

Spidering the site from Owasp Zap and found robots.txt:

![robots.txt on target](images/4_robots_txt.png)

We are able to locate the first of three keys :)

![first key is found](images/5_first_key.png)

Exploring after nikto scan, and in license.txt we found some encrypt text,
thanks to firebug. The text was hidden on the bottom of the page after long
blank space.

![found encrypted text](images/6_license_txt_key.png)

Run the encrypted text through HashID but I can't determine it's type. Then I 
decide to try it in Owasp Zap, and decrypt it as base64:

![zap decrypt txt](images/7_zap_decode_hash.png)

This is the username:password. I tried to log in with this credentials and
this is the result:

![](images/8_in_the_wp.png)

We are successfully log in to the admin panel. Now I think about how to upload
reverse shell. We know that WordPress is Php based, so I decide to upload php
reverse shell in the footer of the theme:

![](images/9_upload_shell.png)

Catching the reverse shell with ncat and we are daemon on the target machine:

![](images/10_catch_reverse_shell.png)

After looking around I locate the second key. But we weren't able to read it
because of permissions.

![](images/11_locate_second_key.png)

Let's try to crack the freshly found md5 hash. I didn't want to fire up John
for this, so i ended up looking online at crackstation for decrypt it. The
    password is the alphabet.

![](images/12_crack_md5.png)

Now I try to log in as SU but my shell didn't allow me to do that, perhaps i
need to spawn /bin/bash:

![](images/13_cant_su.png)

So i upgrade the shell with this python script, and log in successfully as
robot user:

![](images/14_upgrade_shell_with_py.png)

Now we can read the second key:

![](images/15_key2found.png)

I can't find the last key for now ... Probably i will need root access to the
target machine, but for now didn't find a way to obtain it.
