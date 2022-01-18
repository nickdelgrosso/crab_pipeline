*Note:* If using WSL and data is on a usb drive, [mount the drive on the filesystem](https://www.howtogeek.com/331053/how-to-mount-removable-drives-and-network-locations-in-the-windows-subsystem-for-linux/) first so you can access it:

## Launch Singularity Interactively

### If building a full sandbox (so you can pip install during a session, try out applications, etc)

```
sudo singularity build --sandbox -F Singularity.sif Singularity.def
singularity shell --writable --bind /path/to/videos:/data/raw Singularity.sif
```

### If just runing code insteractively, or already have the container built

### Build

```
sudo singularity build --sandbox -F Singularity.sif Singularity.def
```

### Run

```bash
singularity shell --bind /path/to/videos:/data/raw Singularity.sif
```


    
