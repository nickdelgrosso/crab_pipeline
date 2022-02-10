configfile: "config.yaml"
print(config)

SESSION, CAMERA, VIDEO_NAMES, = glob_wildcards(config['raw_path'] + "/{session}/cam{camera}/{rawmov}.MOV")


rule all:
    input:
        config['processed_path'] + "/metadata_csv/movie_paths.csv",


rule extract_metadata:
    input:
        config['raw_path'] + "/{session}/cam{camera}/{rawmov}.MOV"
    output:
        config['processed_path'] + "/metadata_jsons/{session}_cam-{camera}_mov-{rawmov}.json"
    conda:
        "envs/pipeline/env_pipeline.yml"
    shell:
        "python scripts/extract_metadata.py --camera {wildcards.camera} --session {wildcards.session} {input} > {output}"


rule merge_metadata_to_csv:
    input:
        expand(config['processed_path'] + "/metadata_jsons/{session}_cam-{camera}_mov-{rawmov}.json", zip, session=SESSION, camera=CAMERA, rawmov=VIDEO_NAMES)
    output:
        config['processed_path'] + "/metadata_csv/movie_paths.csv"
    conda:
        "envs/pipeline/env_pipeline.yml"
    script:
        "scripts/merge_json_to_csv.py"
    
  