# ADB TLDR
## This note is to record some basic and useful adb commands.
Android Debug Bridge (adb) is a versatile command-line tool that lets you communicate with a device. The adb command facilitates a variety of device actions, such as installing and debugging apps, and it provides access to a Unix shell that you can use to run a variety of commands on a device. It is a client-server program that includes three components:

**A client**, which sends commands. The client runs on your development machine. You can invoke a client from a command-line terminal by issuing an adb command.(TLDR: The commands sender)

**A daemon (adbd)**, which runs commands on a device. The daemon runs as a background process on each device.(TLDR: The process runs on the devices)

**A server**, which manages communication between the client and the daemon. The server runs as a background process on your development machine. (TLDR: The middle man on the computer that tranfers the commands to the daemon)

# Basic

### check connection
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

Options       | Usage |
:------------:|:-----------
**-s**        |to use a specific device with the corresponding serial number
**-d**        |to use the only usb connecting devices  
**-e**        |to use the only one emulator 

### Kill and start adb
```adb kill-server```
- To terminate the adb server process

```adb start-server```
- To start the adb server process

```adb -P port start-server```
- To start the adb server process with a specific port


### Installation
```adb install [Options] path_to_apk```
- To install a apk to the device

options   | usage
:--------:|:-------
**-l**    |Install the package with forward lock.
**-r**    |Reinstall an existing app, keeping its data.
**-t**    |Allow test APKs to be installed.(If the APK is built using a developer preview SDK (if the targetSdkVersion is a letter instead of a number), you must include the -t option with the install command if you are installing a test APK)
**-i**    |Installer_package_name: Specify the installer package name.
**-s**    |Install package on the shared mass storage (such as sdcard).
**-f**    |Install package on the internal system memory.
**-d**    |Allow version code downgrade.
**-g**    |Grant all permissions listed in the app manifest.

```adb install-multiple [Options] path_to_apk1 path_to_apk2```
- To install multiple APKs.
### Uninstallation
```adb uninstall [Options] package```
- Removes a package from the system
* Options:
    * **-k** : Keep the data and cache directories around after package removal.

* Reminder: The package name id can be found in google play website using a web browser, the package name will be listed at the end of the URL after the **?id=** . For example: searching for **busybox** apps, the **url** is ```https://play.google.com/store/apps/details?id=stericson.busybox```, so the package name is **stericson.busybox**. Actually, there is a more **easy** way to find the package name, and I will disscue later.
## Socket connection forwarding/reversing
* To map an android device port to a computer port is called forwarding
* To map a computer port ot an android device port is called reversing

```adb forward [--no-rebind] Local remote``` 
- To set up a forward socket connection, replace local and remote with ```tcp:(port)```, For example: 

- ```adb forward tcp:port_number_of_the_host tcp:port_number_of_the_device```
    - To set up forwarding of host **port port_number_of_the_host** tcp to device port **port_number_of_the_device** . 
    - (local) may be **tcp:0** to pick any open port)

```adb forward --remove LOCAL```
- To remove specific forward

```adb forward --remove-all```
- To remove all forwards

```adb forward --list```
- list all forward socket connections

```adb reverse -l```
- list all reverse socket connections

```adb reverse [--no-rebind] remote local```
- To set up reversing socket connection, replace local and remote with tcp:(port).
    - To choose any open port, make the remote value tcp:0.
```adb reverse --remove remote```
- To remove specific reversing

```adb reverse --remove-all```
- To remove all reversing

## To run as package owner
```run-as package_name```
- Run commands on a device as an app (specified using package_name).
- For example: To read a package data:
```
over@over-ThinkPad-R52:~$ adb shell
$ run-as com.package
$ cd /data/data/com.package
$ ls
databases
lib
$ cd databases
$ ls
preferences.db
$ cat preferences.db > /mnt/sdcard/preferences1.db 
```
- Of course you need to change the "com.package" to specific package id.
- And Also
```
adb shell run-as <PACKAGE_NAME> ls <DIR>
adb shell run-as <PACKAGE_NAME> cat <FILE>
```
- Reminder:
    - /data/data/com.packagename/lib can access without run-as
    - "android:debuggable="false"" will ignore **run-as**

## Backup and restore

```adb backup [-f file] [-apk | -noapk] [-obb | -noobb] [-shared | -noshared] [-all] [-system | [-nosystem] package_names```
- Write an archive of the device's data to file. If you do not specify a file name, the default file is backup.adb. The package list is optional when you specify the -all and -shared options. The following describes the usages for the other options:

Options  | Usage
:-------:|:----------
**-apk** **-noapk** |Back up or do not back up .apk files. The default value is **-noapk**.
**-obb** **-noobb**| Back up or do not back up .obb files. The default value is **-noobb**.
**-shared** **-noshared**| Back up or do not back up shared storage. The default value is **-noshared**.
**-all**| Back up all installed apps.
**-system**  **-nosystem**| Include or do not include system apps when backing up all installed apps (**-all**). The default value is **-system**.

```adb restore file```
- Restore the device contents from file.

## To copy something from device/host to device/host
```adb pull remote local```
- To copy a file or directory and its sub-directories from the device

```adb push local remote```
- To copy a file or directory and its sub-directories to the device
    - Replace local and remote with the paths to the target files/directory on your development machine (local) and on the device (remote). For example: 
```adb push foo.txt /sdcard/foo.txt```

## Reboot the devices

```reboot [bootloader | recovery | sideload | sideload-auto-reboot ]```

- Reboot the device. This command defaults to booting the system image, but also supports bootloader and recovery. 

Options | Usage
:--------:|:-------
**bootloader** |Reboots into bootloader.
**recovery** |Reboots into recovery.
**sideload** |Reboots into recovery and starts sideload mode.
**sideload-auto-reboot** |It is the same as sideload, but reboots after side loading completes.

```adb root```
- Restart adbd with root permissions.

```adb unroot```
- Restart adbd without root permissions.

## Reconnection
```adb reconnect```
- Force a reconnect from the host.

```reconnect device```
- Force a reconnect from the device to force a reconnect.

# Connect over Wifi
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

# ADB shell command
```adb shell```
- Start a remote interactive shell in the target device

```adb shell -e escape_char [-n] [-T] [-t] [-x] [command]```
- Issue a shell command in the target device and then exit the remote shell. Use any combination of the following options:

Options | Usage
:------:|:-------
**-e**  |Specify an escape character or the value none if you do not want to use an escape character. If you do not provide a value, the default escape character (a dash (-)), is used.
**-n**  |Do not read from stdin.
**-T**  |Disable pseudo-terminal utiity (PTY) allocation.
**-t**  |Force PTY allocation.
**-x**  |Disable remote exit codes and stdout/stderr separation.

The shell command binaries are stored in the file system of the device at ```/system/bin/```

For more information, see Issue shell commands.

# Call activity manager
## Basic format

```adb shell am command``` or ```am command``` after enter the remote shell```adb shell```

### Common Commands 

```adb shell am start [options]```  
- start a specific Activity

Options | Usage
:------:|:-------
**-D**  |Enable debugging.
**-W**  | Wait for launch to complete.
**--start-profiler file** | Start profiler and send results to file.
**-P file** | Like --start-profiler, but profiling stops when the app goes idle.
**-R count** | Repeat the activity launch count times. Prior to each repeat, the top activity will be finished.
**-S** | Force stop the target app before starting the activity.
**--opengl-trace** | Enable tracing of OpenGL functions.
**--user user_id \| current** | Specify which user to run as; if not specified, then run as the current user.

Example: ```adb shell am start -n com.tencent.mm/.ui.LauncherUI```
- To launch WeChat main UI

```adb shell am startservice [options]```  
- start a specific Service

Options | Usage
:------:|:------
**--user user_id \| current** |  Specify which user to run as; if not specified, then run as the current user.

```adb shell am kill [options] package```
- Kill all processes associated with package (the app's package name). This command kills only processes that are safe to kill and that will not impact the user experience.

Options | Usage
:------:|:------
** --user user_id \| all \| current** | Specify which user to send to; if not specified then send to all users.

```adb shell am kill-all```
- Kill all background processes.

```adb shell am broadcast [options]```
- send a specific broadcast(Issue a broadcast intent.)

Options | Usage
:------:|:------
** \[--user user_id \| all \| current\]** | Specify which user to send to; if not specified then send to all users.

```adb shell am force-stop```  
- Force stop everything associated with package (the app's package name).

Specification for intent arguments:
- For activity manager commands that take an intent argument, you can specify the intent with the following options:

Options | Usage
:------:|:------
**-a action** | Specify the intent action, such as android.intent.action.VIEW. You can declare this only once.
**-c category** | Specify an intent category, such as android.intent.category.APP_CONTACTS.
**-n component** | Specify the component name with package name prefix to create an explicit intent, such as com.example.app/.ExampleActivity.

# Call package manager
## Basic format

```adb shell pm command``` or ```pm command``` after enter the remote shell ```adb shell```

## Listing
```adb shell pm list package [-f] [-d] [-e] [-s] [-3] [-i] [-u] [--user USER_ID [Filter]```

- Prints all packages, optionally only those package name contains the text in filter

Options        | Usage
:-------------:|:---------
**-f**             |See their associated file
**-d**             |Filter to only show disabled packages
**-e**             |Filter to only show enabled packages.
**-s**             |Filter to only show system packages.
**-3**             |Filter to only show third party packages.
**-i**             | See the installer for the packages.
**-u**             | Also include uninstalled packages.
**--user user_id** | The user space to query.

```adb shell pm list packages Google```
- To find all package names contains "Google"

```adb shell pm list permission-groups```
- Prints all known permission groups.

```adb shell pm list permissions [options] groups```
- Prints all known permissions, optionally only those in group.

Options | Usage
:------:|:------
**-g**  | Organize by group.
**-f**  | Print all information.
**-s**  | Short summary.
**-d**  | Only list dangerous permissions.
**-u**  | List only the permissions users will see.

```adb shell pm list features```
- Prints all features of the system.

```adb shell pm list libraries```
- Prints all the libraries supported by the current device.

```adb shell pm list users```
- Prints all users on the system.

```adb shell pm path package``` 
- Print the path to the APK of the given **package**.

## Installation and Uninstallation

```adb shell pm install [options] path```
- Installs a package (specified by path) to the system.

Options | Usgae
:------:|:---------
**-l**  | Install the package with forward lock.
**-r**  | Reinstall an existing app, keeping its data.
**-t**  | Allow test APKs to be installed. Gradle generates a test APK when you have only run or debugged your app or have used the Android Studio Build > Build APK command. If the APK is built using a developer preview SDK (if the targetSdkVersion is a letter instead of a number), you must include the -t option with the install command if you are installing a test APK.
**-i**  | installer_package_name: Specify the installer package name.
**-s**  | Install package on the shared mass storage (such as sdcard).
**-f**  | Install package on the internal system memory.
**-d**  | Allow version code downgrade.
**-g**  | Grant all permissions listed in the app manifest.

```adb shell pm uninstall [options] package```
- Removes a package from the system.

Options|Usaga
:-------:|:-----
**-k**   | Keep the data and cache directories around after package removal.

```adb shell pm clear package```
- Deletes all data(include cache) associated with a package.

## Granting and Revoking Permission 

```adb shell pm grant package_name permission```
- Grant a permission to an app. On devices running Android 6.0 (API level 23) and higher, the permission can be any permission declared in the app manifest. On devices running Android 5.1 (API level 22) and lower, must be an optional permission defined by the app.

```adb shell pm revoke package_name permission```
- Revoke a permission from an app. On devices running Android 6.0 (API level 23) and higher, the permission can be any permission declared in the app manifest. On devices running Android 5.1 (API level 22) and lower, must be an optional permission defined by the app.

## Install location
```adb shell pm set-install-location location_values```
- Changes the default install location. **Location_values**:

0: Auto: Let system decide the best location.

1: Internal: install on internal device storage.

2: External: on external media.

```adb shell pm get-install-location```
-Returns the current install location. Return value is same as **Location_values**.

## Creating and Removing User
```adb shell pm create-user user_name```
- Create a new user with the given user_name, printing the new user identifier of the user.

```adb shell pm remove-user user_id```
- Remove the user with the given user_id, deleting all data associated with that user

```abd shell pm get-max-users```
- Prints the maximum number of users supported by the device.

# Simulate touch and input
## Basic 
```adb shell input [] [...]```
```
Usage: input []  [...]

The sources are:
      mouse
      keyboard
      joystick
      touchnavigation
      touchpad
      trackball
      stylus
      dpad
      gesture
      touchscreen
      gamepad

The commands and default sources are:
      text  (Default: touchscreen)
      keyevent [--longpress]  ... (Default: keyboard)
      tap   (Default: touchscreen)
      swipe     [duration(ms)] (Default: touchscreen)
      press (Default: trackball)
      roll   (Default: trackball)
```

```adb shell input keyevent keycode```

keycode | meaning
:------:|:-------
3|HOME button
4|BACK button
5|Dialer ap
6|hang up the phone
24|volumn up
25|volumn down 
26|Power button
27|take a photo
64|Open the Browser
82|Menu buttin
224|screen on
223|screen off
- There are Too Many keycode, so plz Google **keyevent keycode** yourself

```adb shell input text hello```
- input a text

# Screencapture
```adb shell screencap file```
- To take a screenshot. Replace file with a file name such as ```/sdcard/screen.png```

# Screenrecord
```adb screenrecord [options] filename```
- Stop the screen recording by pressing Control + C, otherwise the recording stops automatically at three minutes or the time limit set by ```--time-limit```

# Logs

```adb shell dmesg```
- Get kernel log
```adb logcat [<option>] ... [<filter-spec>]```

character | Priority 
:--------:|:--------
**V** | Verbose (lowest priority)
**D** | Debug
**I** | Info
**W** | Warning
**E** | Error
**F** | Fatal
**S**     | Silent (highest priority, on which nothing is ever printed)

```adb logcat *:W```
- displays all log messages with priority level "warning" and higher, on all tags:

# Device's information

```adb shell getprop ro.product.model```
- Get device model

```adb shell dumpsys battery```
- Get battery status

```adb shell settings get secure android_id```
- Get android_id

```
adb shell
su
service call iphonesubinfo 1
```
- Get IMEI

```adb shell getprop ro.build.version.release```
- Get android version

```adb shell cat /sys/class/net/wlan0/address```
- Get Mac Address

```adb shell cat /proc/cpuinfo```
-Get CPU information

# Some useful hack
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

```adb shell vm size```
- To check devices resolution

```adb shell wm density```
- To check devices dpi

## To remount the /system to become writable
1. Enter the shell with root permission 
```
adb shell
su
```
2. Check partition mount situation
```
mount
```

Output:
```
rootfs / rootfs ro,relatime 0 0
tmpfs /dev tmpfs rw,seclabel,nosuid,relatime,mode=755 0 0
devpts /dev/pts devpts rw,seclabel,relatime,mode=600 0 0
proc /proc proc rw,relatime 0 0
sysfs /sys sysfs rw,seclabel,relatime 0 0
selinuxfs /sys/fs/selinux selinuxfs rw,relatime 0 0
debugfs /sys/kernel/debug debugfs rw,relatime 0 0
none /var tmpfs rw,seclabel,relatime,mode=770,gid=1000 0 0
none /acct cgroup rw,relatime,cpuacct 0 0
none /sys/fs/cgroup tmpfs rw,seclabel,relatime,mode=750,gid=1000 0 0
none /sys/fs/cgroup/memory cgroup rw,relatime,memory 0 0
tmpfs /mnt/asec tmpfs rw,seclabel,relatime,mode=755,gid=1000 0 0
tmpfs /mnt/obb tmpfs rw,seclabel,relatime,mode=755,gid=1000 0 0
none /dev/memcg cgroup rw,relatime,memory 0 0
none /dev/cpuctl cgroup rw,relatime,cpu 0 0
none /sys/fs/cgroup tmpfs rw,seclabel,relatime,mode=750,gid=1000 0 0
none /sys/fs/cgroup/memory cgroup rw,relatime,memory 0 0
none /sys/fs/cgroup/freezer cgroup rw,relatime,freezer 0 0
/dev/block/platform/msm_sdcc.1/by-name/system /system ext4 ro,seclabel,relatime,data=ordered 0 0
/dev/block/platform/msm_sdcc.1/by-name/userdata /data ext4 rw,seclabel,nosuid,nodev,relatime,noauto_da_alloc,data=ordered 0 0
/dev/block/platform/msm_sdcc.1/by-name/cache /cache ext4 rw,seclabel,nosuid,nodev,relatime,data=ordered 0 0
/dev/block/platform/msm_sdcc.1/by-name/persist /persist ext4 rw,seclabel,nosuid,nodev,relatime,data=ordered 0 0
/dev/block/platform/msm_sdcc.1/by-name/modem /firmware vfat ro,context=u:object_r:firmware_file:s0,relatime,uid=1000,gid=1000,fmask=0337,dmask=0227,codepage=cp437,iocharset=iso8859-1,shortname=lower,errors=remount-ro 0 0
/dev/fuse /mnt/shell/emulated fuse rw,nosuid,nodev,relatime,user_id=1023,group_id=1023,default_permissions,allow_other 0 0
/dev/fuse /mnt/shell/emulated/0 fuse rw,nosuid,nodev,relatime,user_id=1023,group_id=1023,default_permissions,allow_other 0 0
```

3. Find the /system
```
/dev/block/platform/msm_sdcc.1/by-name/system /system ext4 ro,seclabel,relatime,data=ordered 0 0
```

4. Remount 
```
mount -o remount,rw -t yaffs2 /dev/block/platform/msm_sdcc.1/by-name/system /system
```

## Get Saved Wifi Password

```
adb shell
su
cat /data/misc/wifi/*.conf
```

## Set date and time
```
adb shell
su
date -s 20160823.131500
```

## Use Monkey to conduct a pressure test
```adb shell monkey -p  -v 500```
- Generate 500 pesudorandom events