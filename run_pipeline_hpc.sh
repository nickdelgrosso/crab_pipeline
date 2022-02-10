# stop script if an error occurs
set -e

# Build the snakemake container if it doesn't exist
if [ ! -f snakemake.sif ]; then
    singularity build --fakeroot snakemake.sif envs/snakemake/snakemake.def
fi

# Run the pipeline
singularity run --bind /nfs:/nfs snakemake.sif --cores 2 --use-conda --rerun-incomplete

# Render the pipeline to an image (so it's up to date)
singularity run --bind /nfs:/nfs --app rulegraph snakemake.sif > docs/pipeline_dag.svg
