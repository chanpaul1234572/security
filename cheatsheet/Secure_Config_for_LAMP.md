# Security Setting For LAMP

## Block All Port unless you need: 22, 80, 443(firewall setting)

## Information Disclosure

### Disable Apache 2 Test Page to prevent information disclosure

- As the Test Page will show the Apache 2 version, it is better to disable it.

1. ```cd /etc/httpd/conf.d```
2. ```sudo vim welcome.conf```
3. It will show something like that:

```bash
#
# This configuration file enables the default "Welcome" page if there
# is no default index page present for the root URL.  To disable the
# Welcome page, comment out all the lines below.
#
# NOTE: if this file is removed, it will be restored on upgrades.
#
<LocationMatch "^/+$">
    Options -Indexes
    ErrorDocument 403 /.noindex.html
</LocationMatch>

<Directory /usr/share/httpd/noindex>
    AllowOverride None
    Require all granted
</Directory>

#Alias /.noindex.html /usr/share/httpd/noindex/index.html
```

4. You can comment all the content in ```welcome.conf``` or you can change the ```.noindex.html```

```bash
#
# This configuration file enables the default "Welcome" page if there
# is no default index page present for the root URL.  To disable the
# Welcome page, comment out all the lines below.
#
# NOTE: if this file is removed, it will be restored on upgrades.
#
<LocationMatch "^/+$">
    Options -Indexes
    ErrorDocument 403 /.noindex.html
</LocationMatch>

<Directory /usr/share/httpd/noindex>
    AllowOverride None
    Require all granted
</Directory>

#Alias /.noindex.html /usr/share/httpd/noindex/index.html
Alias /.noindex.html /var/www/html/error/index.html
```

5.Restart Apache: ```sudo systemctl restart httpd```

### Hide the version of OS, Apache and PHP in HTTP Header

1. ```sudo vim /etc/httpd/conf/httpd.conf```
2. Add ```ServerTokens Prod```  Or Change it to what you need
```
ServerTokens Prod[uctOnly]
Server sends (e.g.): Server: Apache
ServerTokens Major
Server sends (e.g.): Server: Apache/2
ServerTokens Minor
Server sends (e.g.): Server: Apache/2.0
ServerTokens Min[imal]
Server sends (e.g.): Server: Apache/2.0.41
ServerTokens OS
Server sends (e.g.): Server: Apache/2.0.41 (Unix)
ServerTokens Full (or not specified)
Server sends (e.g.): Server: Apache/2.0.41 (Unix) PHP/4.2.2 MyMod/1.2
```

### PHP error display hiding

1. ```sudo vim /etc/php.ini```
2. Add those to the doc:
```
file_uploads = On : whether or not to allow http file uploads
display_errors = Off  : whether the error message will be displayed on the screen 
display_startup_errors = Off : whether the error message in the initialization process will be showed
log_errors = On :whether will the error messages be logged
```
Reference: http://php.net/manual/zh/ini.list.php 

### Apache Config for Max number of requests

1. ```sudo vim /etc/httpd/conf/httpd.conf```
2. 
```
KeepAlive on:  whether or not to allow persistent connections
MaxKeepAliveRequests 500: Max number of requests during a persistent connection.
```
3. Restart httpd

### Disable directory Browsing in Apache

1. ```sudo vim /etc/httpd/conf/httpd.conf```
2. Find a line ```Options Includes Indexes ... ```
3. Remove ```Indexes``` and save the file
4. restart the server

or 

- set .htaccess: [11 個強化 WordPress 網站安全的 .Htaccess 設定技巧](https://free.com.tw/wordpress-htaccess-tips-and-tricks/)
