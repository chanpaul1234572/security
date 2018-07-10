## Ping cheatsheet
```ping www.aaa.com```
- In Windows, this command will send 4 ICMP ECHO_REQUEST packages. 
- But in Linux, it will send packages repeatedly until the user press ```Ctrl + C```

```ping -n 10 www.aaa.com``` (Windows) \ ```ping -c 10 www.aaa.com``` (Linux and macos)
- Ping www.aaa.com 10 times

```ping -t www.aaa.com``` (Windows)
- Ping repeatedly until ```Ctrl + C```

```ping -4 www.aaa.com``` (Windows)
- Ping the IPv4 address of the domain name

```ping -6 www.aaa.com```(Windows)
- Ping the IPv6 address of the domain name

```ping -a 216.58.220.196```(Windows)
- Ping the IP with DNS Reverse solution(find the domain name by IP)

```ping -l 1200 www.aaa.com```(Windows) \ ```ping -s 1200 www.aaa.com```(Linux and macos)
- Ping www.aaa.com with 1200 bytes of data

```ping -l 1200 -f www.aaa.com```(Windows) \ ```ping -s 1200 -M www.aaa.com```(Linux) \ ```ping -s 1200 -D www.aaa.com```
- Ping www.aaa.com with 1200 bytes of data without fragmentation

```ping -h```(Windows, Linux and macos)
- Get **ping** help pages

```ping -a www.aaa.com```(Linux and macos)
- Ping www.aaa.com, if the computer receive an ICMP ECHO_RESPONSE, it will give a sound. (audible ping)

```ping -A www.aaa.com```(Linux and macos)
- Ping www.aaa.com, if the computer lost an ICMP ECHO_REQUEST, it will give a sound. (audible ping)

```ping -i 0.4 www.aaa.com```(Linux and macos)
- Ping www.aaa.com in every 0.4 second

```ping -I eth0 www.aaa.com```(Linux and macos)
- Ping www.aaa.com with specific network interface (network card) eth0

```ping -I 45.118.135.69 blog.gtwang.org```(Linux and macos)
- Ping www.aaa.com with specific network interface (network card) that has an address 45.118.135.69

```ping -n www.aaa.com```(Linux and macos)
- Ping www.aaa.com without DNS Reverse solution(find the domain name by IP)

### Use ping and arp to generation a IP-MAC pairs table
- Linux
```bash
for ip in 192.168.1.{1..254}; do
  # 刪除舊的 arp 記錄
  sudo arp -d $ip > /dev/null 2>&1
  # 藉由 ping 取得新的 arp 資訊
  ping -c 5 $ip > /dev/null 2>&1 &
done

# 等待所有背景的 Ping 結束
wait

# 輸出 ARP table
arp -n | grep -v incomplete
```
- Or you can use ```arping```

- macOS
```bash
#!/bin/bash
# Ping 區域網路中所有的 IP 位址
for ip in 140.110.99.{1..254}; do
  # 刪除舊的 arp 記錄
  sudo arp -d $ip > /dev/null 2>&1
  # 藉由 ping 取得新的 arp 資訊
  ping -c 5 $ip > /dev/null 2>&1 &
done

# 等待所有背景的 Ping 結束
wait

# 輸出 ARP table
arp -na | grep -v incomplete
```

- Windows
```
arp -d
```

**This command requires Admin permission**

```
for /L %i in (1,1,254) do ping 192.168.1.%i -n 1 -w 300 > NUL
```
```
arp -a | find "192.168" | find "動態"
```
