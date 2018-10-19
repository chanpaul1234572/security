# SSH Port Forwarding

## There are 3 types SSH Port Forwarding: **Local Port Forwarding**, **Remote Port Forwarding** and **Dynamic Port Forwarding**

### Local Port Forwarding

- **local port forwarding**:By sending the requests to a local port and forward to our target port.
- Syntax:

```bash
-L <local machine network ip(under its subnet)>:<local machine port>:<target ip(under its subnet)>:<target port>
```

- For example, on a cloud computer B1(103.59.22.17) with a opened port 3000(e.g. Node.js service), a local machine A want to access.

```javascript
var http = require('http');

var server = http.createServer(function(request, response)
{
    response.writeHead(200,
    {
        "Content-Type": "text/plain"
    });
    response.end("Hello World\n");
});

server.listen(3000);
```

- To access it,```http://103.59.22.17:3000```
- But the firewall of the cloud just opened 22(SSH port), also the IP of local machine may be dyanmic allocated...

- For example, A sends HTML requests to B1 using port 2000:

    1. ```ssh -L localhost:2000:localhost:3000 root@103.59.22.17``` 
    2. ```curl http://localhost:2000```

- Normally, we can omit local machine network ip, for example: ```ssh -L 2000:localhost:3000 root@103.59.22.17``` will mean the same to the previous example.
- We can choose another ip for another machine under the subnet
- For example, to connect with B1 and do port forwarding to B2 (192.168.59.100):

```bash
ssh -L 2000:192.168.59.100:3000 root@103.59.22.17
```

### Remote Port Forwarding

- To redirect the request from remote machine to target machine
- Syntax:

```bash
ssh -R <remote machine ip(under its subnet)>:<remote machine port>:<target ip(under its subnet)>:<target port>
```

- For example: to redirect all requests from B1(port 2000) to A1(port 3000)

```bash
ssh -R localhost:2000:localhost:3000 root@103.59.22.17
```

- Similarly, remoste machine ip can be omitted(default value is localhost), target ip can be another ip.
- For example A2(192.168.0.100) under the same subnet with A1, To login B1 from A1 and perform port forwarding from B1 to A2

```bash
ssh -R 2000:192.168.0.100:3000 root@103.59.22.17
```

### Dynamic Port Forwarding

- This works by allocating a socket to listen to port on the localside, optionally bound to the specified bind_address.  Whenever a connection is made to this port, the connection is forwarded over the secure channel, and the application protocol is then used to determine where to connect to from the remote machine.  Currently the SOCKS4 and SOCKS5 protocols are supported, and ssh will act as a SOCKS server.
- Send the requests to SOCKS server and let the SOCKS server to handle the request.
- For example, we are inside the firewall and we can only connect a outbound remote machine B1, we can make B1 to be a SOCKS proxy and let B1 to send requests for us.
- Syntax:
  
``` bash
ssh -D <local machine ip>:<local machine port>
```

- For example, a remote machine B1(103.59.22.17)

```
ssh -D localhost:2000 root@103.59.22.17
```

- Next you would tell Firefox to use your proxy:

1. go to Edit -> Preferences -> Advanced -> Network -> Connection -> Settings...
2. check "Manual proxy configuration"
3. make sure "Use this proxy server for all protocols" is cleared
4. clear "HTTP Proxy", "SSL Proxy", "FTP Proxy", and "Gopher Proxy" fields
5. enter "127.0.0.1" for "SOCKS Host"
6. enter "2000" (or whatever port you chose) for Port. 

- You can also set Firefox to use the DNS through that proxy, so even your DNS lookups are secure:

1. Type in about:config in the Firefox address bar
2. Find the key called "network.proxy.socks_remote_dns" and set it to true 

- The SOCKS proxy will stop working when you close your SSH session. You will need to change these settings back to normal in order for Firefox to work again. 

- Then, You may want to browse B1:3000 and you can type localhost:3000 (it means port 3000 in machine B1)
- Or, you can go google by typing google.com:80

### Port Forwarding Chain

- There are 3 machines, machine A is on company, machine B is at home and machine C(103.59.22.17) is on Cloud

- By local port forwarding, we can redirect all B:3000 requests to C:2000:

```
ssh -L localhost:3000:localhost:2000 root@103.59.22.17
```

- Then by remote port forwarding, we can redirect all C:2000 requests to A:3000
```
ssh -R localhost:2000:localhost:3000 root@103.59.22.17
```

- Turn out that all B:3000 request will forward to C:2000 then forward to A:3000, that means you can access A by B.

### Some Permeter:
-C: enables compression, which speeds the tunnel up when proxying mainly text-based information (like web browsing)
-N: Tells SSH that no command will be sent once the tunnel is up
-q: Uses quiet mode
-f: Forks the process to the background


### Some useful website:
https://help.ubuntu.com/community/SSH/OpenSSH/PortForwarding
https://gist.github.com/suziewong/4413491#ssh