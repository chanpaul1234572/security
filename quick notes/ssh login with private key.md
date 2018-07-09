### OpenSSH: How to login with private key
1. On the Client side: run ```ssh-keygen``` to generate a public key file ```id_rsa.pub``` and a private key file ```id_rsa```.
2. Put the ```id_rsa.pub``` to the server's authorized_keys folder.
Usually, it is located in ```/home/{$user}/.ssh/authorized_keys```. There are mainly 2 ways to do it:
    1. After logged in the server and transferred the ```id_ras.pub``` to the server, run ```cat id_rsa.pub >> authorized_keys```
    2. Directly run ```ssh-copy-id -i id_ras.pub {user}@{host}```
3. The permission of ```authorized_keys``` and ```id_ras``` file should be set as ```600``` or ```400```, which means only the owner can read and modify it.
4. Modify ```/etc/ssh/sshd_config```
```
RSAAuthentication yes
PubkeyAuthentication yes
ChallengeResponseAuthentication no 
PasswordAuthentication no
```
5. Restart the service: ```sudo service ssh restart```
6. ```ssh -i id_ras {user}@{host}```

