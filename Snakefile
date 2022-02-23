configfile: "config.yaml"

SESSION, CAMERA, VIDEO_NAMES, = glob_wildcards(config['raw_path'] + "/{session}/cam{camera}/{rawmov}.MOV")

rule all:
    input:
        config['processed_path'] + "/metadata_csv/movie_paths.csv",
        expand(config['processed_path'] + "/videos/{session}_cam{camera}_{rawmov}.mp4", session=SESSION, camera=CAMERA, rawmov=VIDEO_NAMES)


rule build_singularity_image_file:
    input:
        "envs/{recipe}/{recipe}.def"
    output:
        "{recipe}.sif"
    shell:
        "singularity build --fakeroot {output} {input}"


rule convert_mov_to_mp4:
    input:
        video = config['raw_path'] + "/{session}/cam{camera,[0-9]}/{rawmov}.MOV"
    output:
        config['processed_path'] + "/videos/{session}_cam{camera,[0-9]}_{rawmov}.mp4"
    conda:
        "envs/ffmpeg/ffmpeg.yml"
    container:
        "docker://jrottenberg/ffmpeg:3-alpine"
    log:
        config['processed_path'] + "/videos/log/{session}_cam{camera,[0-9]}_{rawmov}.log"
    shell:
        "ffmpeg -i {input.video} {output} 2> {log}"


rule extract_metadata:
    input:
        config['raw_path'] + "/{session}/cam{camera}/{rawmov}.MOV"
    output:
        config['processed_path'] + "/metadata_jsons/{session}_cam-{camera}_mov-{rawmov}.json"
    conda:
        "envs/pipeline/env_pipeline.yml"
    shell:
        "python scripts/extract_metadata.py --camera {wildcards.camera} --session {wildcards.session} {input} > {output}"


# rule extract_metadata2:
#     input:
#         config['raw_path'] + "/{session}/cam{camera}/{rawmov}.MOV"
#     output:
#         config['processed_path'] + "/metadata_ffprobe_jsons/{session}_cam-{camera}_mov-{rawmov}.json"
#     container:
#         "envs/vid_metadata/ffprobe.def"
#     shell:
#         "python scripts/extract_metadata_ffprobe.py --camera {wildcards.camera} --session {wildcards.session} {input} > {output}"


rule merge_metadata_to_csv:
    input:
        expand(config['processed_path'] + "/metadata_jsons/{session}_cam-{camera}_mov-{rawmov}.json", zip, session=SESSION, camera=CAMERA, rawmov=VIDEO_NAMES)
    output:
        config['processed_path'] + "/metadata_csv/movie_paths.csv"
    conda:
        "envs/pipeline/env_pipeline.yml"
    script:
        "scripts/merge_json_to_csv.py"
    
  