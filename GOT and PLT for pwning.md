# GOT and PLT for pwning
[learnt and some notes from system overload](https://systemoverlord.com/2017/03/19/got-and-plt-for-pwning.html)
## Relocations
### .got
This is the GOT, or Global Offset Table. This is the actual table of offsets as filled in by the linker for external symbols.
### .plt
This is the PLT, or Procedure Linkage Table. These are stubs that look up the addresses in the .got.plt section, and either jump to the right address, or trigger the code in the linker to look up the address. (If the address has not been filled in to .got.plt yet.)
### .got.plt
This is the GOT for the PLT. It contains the target addresses (after they have been looked up) or an address back in the .plt to trigger the lookup. Classically, this data was part of the .got section.
### .plt.got
It seems like they wanted every combination of PLT and GOT! This just seems to contain code to jump to the first entry of the .got. I’m not actually sure what uses this. (If you know, please reach out and let me know! In testing a couple of programs, this code is not hit, but maybe there’s some obscure case for this.)

### TL;DR
Those starting with .plt contain stubs to jump to the target, those starting with .got are tables of the target addresses.

![Header sector](https://github.com/chanpaul1234572/security/blob/master/Capture.PNG)
![PLT and GOT routine](https://github.com/chanpaul1234572/security/blob/master/PLT_GOT.png)
