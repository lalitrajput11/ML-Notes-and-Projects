# Memory Specific

## Method 1: The free command

Since the free command is the most widely used and, without any doubt, the most helpful, we will mention its usage first. This command is used to check information about the RAM usage by your system. Here is the command you will enter in the Terminal:

**$ free -m**

## Method 2: The vmstat command

To view memory statistics through the vmstat command, you can use it in the following manner:

**$ vmstat -s**
## Method 3: The /proc/meminfo command

The following command extracts memory-related information from the /proc file system. These files contain dynamic information about the system and the kernel rather than the real system files.

This is the command you will use to print memory information:

**$ cat /proc/meminfo**

## Method 4: The top command

The top command is used to print CPU and memory usage of your system. You can use this command as follows:

**$ top**

## Method 5: The htop command

Like the top command, the htop command also gives a detailed analysis of your CPU and memory usage. If you do not have installed htop on your system, you can install it by first updating your abt repositories through the following command:

**$ sudo apt-get update**

And then install htop by entering the following command as sudo:

**$ sudo apt install htop**
**$ htop**

---
