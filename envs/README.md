# Environments 

This directory contains conda and singularity environment files for
getting needed software.  

## Singularity Containers


### Building 

On the HPC, you'll need "fakeroot" permission, since we don't have sudo access.  Once that's given, you can use the following command to turn a **.def** singularity recipe file into a **.sif** singlarity image file:

**Note**: Many of the singularity environments rely on conda environment
files, and have relative paths from the working directory.  Accordingly,
you should build them from the project root directory.

```
singularity build --fakeroot myimage.sif envs/myimage/myimage.def
```

### Running

Run default program (usually indicated by the name of the def):

```
singularity run myimage.sif
```

Activate environment:

```
singularity shell myimage.sif
```


## Conda Environments

Alternatively, you can use conda:

### Building

```
conda env create -f myenv.yml -n name
```

### Activating

```
conda activate name
```