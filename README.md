

## Launch Singularity Interactively

```bash
singularity shell --bind /path/to/videos:/data/raw Singularity.sif
```

*Note:* If using WSL and data is on a usb drive, [mount the drive on the filesystem](https://www.howtogeek.com/331053/how-to-mount-removable-drives-and-network-locations-in-the-windows-subsystem-for-linux/) first so you can access it:
    
