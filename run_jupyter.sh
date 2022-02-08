# stop script if an error occurs
set -e

# Build the Jupyter container if it doesn't exist
if [ ! -f jupyter2.sif ]; then
    singularity build --fakeroot jupyter2.sif envs/jupyter/jupyter.def
fi

# Run Jupyter
singularity run --bind /nfs/winstor/branco/Tiago/Field:/data/raw jupyter.sif
