# stop script if an error occurs
set -e

# Run the pipeline
singularity run --bind /nfs/winstor/branco/Tiago/Field:/data/raw snakemake.sif

# Render the pipeline to an image (so it's up to date)
singularity run --bind /nfs/winstor/branco/Tiago/Field/:/data/raw --app rulegraph snakemake.sif > docs/pipeline_dag.svg
