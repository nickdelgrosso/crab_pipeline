*Note:* If using WSL and data is on a usb drive, [mount the drive on the filesystem](https://www.howtogeek.com/331053/how-to-mount-removable-drives-and-network-locations-in-the-windows-subsystem-for-linux/) first so you can access it:



## Build Containers

### Jupyter Lab

This project contains a jupyter lab instance with many nice features pre-installed:
  - Python Kernel
  - R Kernel
  - Real-Time Collaboration Extension
  - Git Extension
  - Singularity 


#### Install

Build singularity container:
```
singularity build --fakeroot --sandbox -F jupyter.sif singularity_recipes/jupyter.def 
```

#### Run

Run Jupyter in the container:
```
singularity run --writable --bind /path/to/videos:/data/raw jupyter.sif
```


### Snakemake

#### Install

```
sudo singularity build --fakeroot -F snakemake.sif singularity_recipes/snakemake.def
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


ssh -L 8888:hpc-gw1:8888 -J ngrosso@ssh.swc.ucl.ac.uk ngrosso@hpc-gw1
# FAQs

###  How do I start an Interactive Session on the SWC Cluster?

  1. SSH to the Login Node to get into SWC's :  `ssh username@ssh.swc.ucl.ac.uk`
  2. Once logged in, SSH from there to the HPC Login Node to get into the HPC Network: `ssh username@hpc-gw1`
  3. Once in, start an interactive bash session using the **srun** command: `srun --pty bash -i`
  4. You're in!  Start coding! 

### I don't like typing my password all the time.  Is there a way to send a keypair instead?

Yep!  Do the following twice: once for connecting to the ssh from your computer, then again
from the ssh node to connect to the hpc-gw1 node:

```
ssh-keygen -t ed25519
ssh-copy-id username@ssh.swc.ucl.ac.uk
```


You can learn more here: https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys-2

### Can I jump directly to the hpc-gw1 node without typing two sets of ssh commands?

Yes, you can jump hosts with the '-J' flag:

```
ssh -J username@ssh.swc.ucl.ac.uk username@hpc-gw1
```

### How do I mount a usb drive in linux?

```sudo mount -t drvfs f: /mnt/f```


### How access Jupyter lab on my computer if it's running on the server?

After running jupyter lab, note the port number and ip address.  
Then make a new SSH connection, forwarding the port from that node to your
local machine:

```
 ssh -L 8888:node-ip-name:8888 username@ssh.swc.ucl.ac.uk
``` 
