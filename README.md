*Note:* If using WSL and data is on a usb drive, [mount the drive on the filesystem](https://www.howtogeek.com/331053/how-to-mount-removable-drives-and-network-locations-in-the-windows-subsystem-for-linux/) first so you can access it:

## Run Apps

### Jupyter Lab

This project contains a jupyter lab instance with many nice features pre-installed:
  - Python Kernel
  - R Kernel
  - Real-Time Collaboration


#### Install

Build singularity container:
```
sudo singularity build --fakeroot --sandbox -F jupyter.sif jupyter.def
```

#### Run

Run Jupyter in the container:
```
singularity run --writable --bind /path/to/videos:/data/raw jupyter.sif
```


### Snakemake

#### Install

```
sudo singularity build --fakeroot --sandbox -F snakemake.sif snakemake.def
```

#### Run

To run snakemake with default arguments:

```bash
singularity run --bind /path/to/videos:/data/raw snakemake.sif
```

To run with custom arguments:
```bash
singularity exec --bind /path/to/videos:/data/raw snakemake.sif snakemake --cores 1
```

## Installing Singularity 3.8




## Working on the SWC Cluster: An Interactive Session

  1. SSH to the Login Node to get into SWC's :  `ssh username@ssh.swc.ucl.ac.uk`
  2. Once logged in, SSH from there to the HPC Login Node to get into the HPC Network: `ssh username@hpc-gw1`
  3. Once in, start an interactive bash session using the **srun** command: `srun --pty bash -i`
  4. You're in!  Start coding! 



# FAQs

### How do I mount a usb drive in linux?

```sudo mount -t drvfs f: /mnt/f```


### How access Jupyter lab on my computer if it's running on the server?

After running jupyter lab, note the port number and ip address.  
Then make a new SSH connection, forwarding the port from that node to your
local machine:

```
 ssh -L 8888:node-ip-name:8888 username@ssh.swc.ucl.ac.uk
``` 