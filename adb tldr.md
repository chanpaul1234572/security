## ADB TLDR
### This note is to record some basic and useful adb commands.
Android Debug Bridge (adb) is a versatile command-line tool that lets you communicate with a device. The adb command facilitates a variety of device actions, such as installing and debugging apps, and it provides access to a Unix shell that you can use to run a variety of commands on a device. It is a client-server program that includes three components:

**A client**, which sends commands. The client runs on your development machine. You can invoke a client from a command-line terminal by issuing an adb command.(TLDR: The commands sender)

**A daemon (adbd)**, which runs commands on a device. The daemon runs as a background process on each device.(TLDR: The process runs on the devices)

**A server**, which manages communication between the client and the daemon. The server runs as a background process on your development machine. (TLDR: The middle man on the computer that tranfers the commands to the daemon)

### Basic

#### check connection
```adb devices```
- To show any device(s) is/are currently connected
```
List of devices attached
FA67TBN01874    device 
``` 
``` adb devices -l ``` 
- To show which device(s) is/are currently connected
```
List of devices attached
FA67TBN01874           device usb:336855040X product:pmeuhl_00401 model:HTC_10 device:htc_pmeuhl transport_id:6
```
* **Serial number**: A string created by adb to uniquely identify the device by its port number. (The string in the begining)
* If you have muilt devices connected, you can use ``` -s ``` to select which device you want to execute commands on. In general: ```adb -s Serial number command```. For example : if you want to launch a shell on a device with serial number **FA67TBN01874**, then you can type: ```adb -s FA67TBN01874 shell```.

#### Installation
```adb install [Options] path_to_apk```
- To install a apk to the device
* options:
    * **-l**: Install the package with forward lock.
    * **-r**: Reinstall an existing app, keeping its data.
    * **-t**: Allow test APKs to be installed.(If the APK is built using a developer   preview SDK (if the targetSdkVersion is a letter instead of a number), you must include the -t option with the install command if you are installing a test APK)
    * **-i**: Installer_package_name: Specify the installer package name.
    * **-s**: Install package on the shared mass storage (such as sdcard).
    * **-f**: Install package on the internal system memory.
    * **-d**: Allow version code downgrade.
    * **-g**: Grant all permissions listed in the app manifest.
#### Uninstallation
```adb uninstall [Options] package```
- Removes a package from the system
* Options:
    * **-k** : Keep the data and cache directories around after package removal.
* Reminder: The package name id can be found in google play website using a web browser, the package name will be listed at the end of the URL after the **?id=** . For example: searching for **busybox** apps, the **url** is ```https://play.google.com/store/apps/details?id=stericson.busybox```, so the package name is **stericson.busybox**. Actually, there is a more **easy** way to find the package name, and I will disscue later.
#### Socket connection forwarding
```adb [--no-rebind] Local remote``` 
- To set up a forward socket connection, replace local and remote with tcp:(ports), For example: 

- ```adb forward tcp:port_number_of_the_host tcp:port_number_of_the_device```
    - To set up forwarding of host **port port_number_of_the_host** tcp to device port **port_number_of_the_device** . 
    - (local) may be **tcp:0** to pick any open port)

```adb forward --remove LOCAL```
- To remove specific forward

```adb forward --remove-all```
- To remove all forwards

```adb forward --list```
- list all forward socket connections
#### To copy something from device/host to device/host
```adb pull remote local```
- To copy a file or directory and its sub-directories from the device

```adb push local remote```
- To copy a file or directory and its sub-directories to the device

Replace local and remote with the paths to the target files/directory on your development machine (local) and on the device (remote). For example: 
```adb push foo.txt /sdcard/foo.txt```

```adb kill-server```
- To terminate the adb server process

### Connect over Wifi
1. Connect your Android device and adb host computer to a common Wi-Fi network accessible to both. Beware that not all access points are suitable; you might need to use an access point whose firewall is configured properly to support adb.

2. If you are connecting to an Wear OS device, turn off Bluetooth on the phone that's paired with the device.

3. Connect the device to the host computer with a USB cable.

4. Set the target device to listen for a TCP/IP connection on port 5555:
```adb tcpip 5555```

5. Disconnect the USB cable from the target device.

6. Find the IP address of the Android device. For example, on a Nexus device, you can find the IP address at **Settings > About tablet (or About phone) > Status > IP address**. Or, on an Wear OS device, you can find the IP address at **Settings > Wi-Fi Settings > Advanced > IP address**.
7. Connect to the device by its IP address : ```adb connect device_ip_address```

8. Confirm that your host computer is connected to the target device: ```adb devices -l```
```
List of devices attached
FA67TBN01874           device usb:336855040X product:pmeuhl_00401 model:HTC_10 device:htc_pmeuhl transport_id:7
192.168.0.101:5555     device product:pmeuhl_00401 model:HTC_10 device:htc_pmeuhl transport_id:8
```
9. To disconnect the devices : ```adb disconnect [HOST[:PORT]]```. For example, To disconnect a devices with a ip **192.168.0.101**, you can try ```adb disconnect 192.168.0.101```

If the adb connection is ever lost:

1. Make sure that your host is still connected to the same Wi-Fi network your Android device is.
2. Reconnect by executing the ```adb connect``` step again.
3. Or if that doesn't work, reset your adb host: ```adb kill-server```

Then start over from the beginning.

### ADB command reference
```adb [-d | -e | -s serial_number] command ```

### Some useful hack
```adb shell dumpsys window windows | grep "Focus"```
- To get the current foreground running apps's package id and current activity.
```
mCurrentFocus=Window{b24121c u0 com.google.android.dialer/com.google.android.dialer.extensions.GoogleDialtactsActivity}
mFocusedApp=AppWindowToken{c6b3f53 token=Token{9f9958d ActivityRecord{11d1624 u0 com.google.android.dialer/.extensions.GoogleDialtactsActivity t17077}}}
```
**com.google.android.dialer** is the package id
**com.google.android.dialer.extensions.GoogleDialtactsActivity** is the activity name.

```adb shell am start -c api.android.intent.LAUNCHER -a api.android.category.MAIN -n package_id/activity_name```
- To open a app at a specific activity, For example: ```adb shell am start -c api.android.intent.LAUNCHER -a api.android.category.MAIN -n com.google.android.dialer/com.google.android.dialer.extensions.GoogleDialtactsActivity```

