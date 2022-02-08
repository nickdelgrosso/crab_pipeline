configfile: "config.yaml"
print(config)

SESSION, CAMERA, VIDEO_NAMES, = glob_wildcards(config['raw_path'] + "/{session}/cam{camera}/{rawmov}.MOV")


rule all:
    input:
        "data/final/movie_paths.csv"


rule extract_metadata:
    input:
        config['raw_path'] + "/{session}/cam{camera}/{rawmov}.MOV"
    output:
        "data/processed/{session}_cam-{camera}_mov-{rawmov}.json"
    conda:
        "envs/pipeline/env_pipeline.yml"
    shell:
        "python scripts/extract_metadata.py --camera {wildcards.camera} --session {wildcards.session} {input} > {output}"

  
rule extract_metadata2:
    input:
        config['raw_path'] + "/{session}/cam{camera}/{rawmov}.MOV"
    output:
        "data/processed2/{session}_cam-{camera}_mov-{rawmov}.json"
    conda:
        "envs/jupyter/env_jupyter.yml"
    notebook:
        "notebooks/check_metadata.py.ipynb"


rule merge_metadata_to_csv:
    input:
        expand("data/processed/{session}_cam-{camera}_mov-{rawmov}.json", zip, session=SESSION, camera=CAMERA, rawmov=VIDEO_NAMES)
    output:
        "data/final/movie_paths.csv"
    conda:
        "envs/pipeline/env_pipeline.yml"
    script:
        "scripts/merge_json_to_csv.py"
    
  