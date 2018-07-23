# function Stack frame and Ret2libc basic 
## Standard segment layout overview in a Linux process
- The above figure represent virtual addresses that are mapped to physical memory.
```
+--------------------------------------------------------+ <==0xffffffff
|                    Kernel space(1GB)                   |
|User code cannot read from nor write to these addresses,| 
|        doing so results in a Segmentation Fault.       |
|                                                        |
|                                                        |
+--------------------------------------------------------+ <==0xc0000000 == TASK_SIZE
|          Random stack offset(security purpose)         | 
+--------------------------------------------------------+ <-|
|                    Stack (grow down)                   |   |
|                           |                            |   |> RLIMIT_STACK (e.g., 8MB) 
+--------------------------------------------------------+   |                       
|                                                        | <-| 
|          Random mmap offset(security purpose)          |
+--------------------------------------------------------+
|           Memory Mapping Segment(grow down)            |
|    File mappings (including dynamic libraries) and     |
|    anonymous mappings. Example: /lib/libc.so           |             
+--------------------------------------------------------+ <- program break brk
|                      Heap(grow up)                     |
|                                                        |
|                                                        |        
```

## function Stack frame

```
low memory
0x0000
+----+<-----ESP
|AAAA|
+----+
|AAAA|
+----+
|AAAA|
+----+

high memory
```