singularity run --app rulegraph snakemake.sif  > docs/pipeline_graph.svg
singularity run --bind /nfs/winstor/branco/Tiago/Field:/data/raw snakemake.sif
