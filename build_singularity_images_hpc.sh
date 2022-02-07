# stop script on error
set -e

# build both images
singularity build --fakeroot -F snakemake.sif singularity_recipes/snakemake.def
singularity build --fakeroot -F jupyter.sif singularity_recipes/jupyter.def
