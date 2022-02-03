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

## Launch Jupyter Lab

```
singularity run --app jupyter Singularity.sif
```


## Installing Singularity 3.8

These were the best instructions!
https://github.com/apptainer/singularity/blob/master/INSTALL.md

### Docs
https://sylabs.io/guides/3.8/user-guide/


## Working on the SWC Cluster: An Interactive Session

  1. SSH to the Login Node to get into SWC's :  `ssh username@ssh.swc.ucl.ac.uk`
  2. Once logged in, SSH from there to the HPC Login Node to get into the HPC Network: `ssh username@hpc-gw1`
  3. Once in, start an interactive bash session using the **srun** command: `srun --pty bash -i`
  4. You're in!  Start coding! 

