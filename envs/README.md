# Environments 

This directory contains conda and singularity environment files for
getting needed software.  

## Conda Environmnets

Note that on the HPC you'll always need to activate miniconda first:
```
module load miniconda
```

### Building 

Example for snakemake shown below:



Then to build:
```
conda env create -n snakemake -f envs/snakemake/env_snakemake.yml
```

### Running

```
conda activate snakemake
snakemake --cores 1 --use-conda
```

## Singularity Containers


### Building 

On the HPC, you'll need "fakeroot" permission, since we don't have sudo access.  Once that's given, you can use the following command to turn a **.def** singularity recipe file into a **.sif** singlarity image file:

**Note**: Many of the singularity environments rely on conda environment
files, and have relative paths from the working directory.  Accordingly,
you should build them from the project root directory.

```
singularity build --fakeroot snakemake.sif envs/snakemake/snakemake.def
```

### Running

Run default program (usually indicated by the name of the def):

```
singularity run snakemake.sif --cores 1  --use-conda
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