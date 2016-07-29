Title: TommyBoy1
Date: 2016-07-29 09:00
Category: VulnHub CTF

**This is a TommyBoy1 challenge from vulnhub.com. You can obtain the virtual
machine from: [here](https://www.vulnhub.com/entry/tommy-boy-1,157/)**

> '''
> The primary objective is to restore a backup copy of the homepage to Callahan 
> Auto's server. However, to consider the box fully pwned, you'll need to collect 
> 5 flags strewn about the system, and use the data inside them to unlock one 
> final message.
> '''

At first scanning the target with nmap:
![](images/TommyPics/1_nmap.png)

Then version detection:
![](images/TommyPics/1_1_nmap.png)

Strange thing... at first port 65534 was open now it's closed. I launch
wireshark and start snooping the trafic to realize what happened. We have 22, 80
and 8008 open so lets focus on that for now.
At index page on the website on port 80 in the source we found this comments:
![](images/TommyPics/1_3_comment_in_index_html.png)

From the comments we conclude:

- **Nick** is the administrator of the site

- **Richard** is someone who wants admin access

- The backup of the site is in Big Tom's home folder

- **Tom** share important information on the company blog

- The company blog is at **/prehistoricforest**

The company blog is WP site. And one of the blog posts is password protected.
The answer from the first post in the blog give as clue about /richard directory
in which we found img file 'shockedrichard'. I tried to unlock the password
protected post with 'richard', 'shockedrichard' etc. didn't work. This is what
we found in the picture:
![](images/TommyPics/5_found_hash_in_picture.png)

Decrypt the hash:
![](images/TommyPics/6_decrypt_hash.png)

Then unlock the second post in which we found important info:

- Another user Michelle

- Nick is the IT guy

- there is backup called **callahanbak.bak** that you can just rename to
  index.html and everything will be good again. (You have to do this under Big Tom’s account via SSH to perform this restore)

- Big Tom's accontt shoud be found in the userlist (probably it's not called
  bigtom)

- The home folder of Nick can be accesed via FTP, the port is the one we
  found at the first scan with nmap (65534). The FTP server goes on/off every
  15 minutes.

- Nick ftp account = **nickburns** (the password is very easy)

- Nick didn't have ssh access

From there I decide to try nick ftp account with hydra:
![](images/TommyPics/8_hydra_brute.png)

In the ftp dir we found this readme.txt:
![](images/TommyPics/9_ftp_readme.png)

- There should be encrypted .zip file in 'NickIzL33t' contained Big Tom's passwords.
The 'NickIzL33t' is at [target ip]:8008/NickIzL33t but there is nothing there so 
lets scan the webserver. I used nikto, nessus and wpscan for that.


