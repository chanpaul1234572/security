## Ping cheatsheet
```ping www.aaa.com```
- In Windows, this command will send 4 ICMP ECHO_REQUEST packages. 
- But in Linux, it will send packages repeatedly until the user press ```Ctrl + C```

```ping -n 10 

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
