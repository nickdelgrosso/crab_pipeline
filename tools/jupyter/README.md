
## Run Jupyter Lab

*Note*: may take a while the first time.

### With Conda

```
module load miniconda
conda env create -n jupyter env_jupyter.yml  # only first time
conda activate jupyter
jupyter lab --no-browser --ip "*" --collaborative --allow-root
```

To get R Kernel:
```
module load miniconda
conda env create -n rkernel envs/jupyter/env_rkernel.yml  # only first time
```

To get Python Kernel:
```
module load miniconda
conda env create -n pykernel envs/jupyter/env_pykernel.yml  # only first time
```

### With Singularity

Build image:
```
singularity build --fakeroot jupyter.sif jupyter.def
```

Run image:
```
singularity run jupyter.sif
```
