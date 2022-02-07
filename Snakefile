

VIDEO_NAMES, = glob_wildcards("/data/raw/{rawmov}.MOV")


rule all:
    input:
        "./data/final/movie_paths.csv"


rule extract_metadata:
    input:
        "/data/raw/{rawmov}.MOV"
    output:
        "./data/processed/{rawmov}.json"
    conda:
        "environment.yml"
    shell:
        "python scripts/extract_metadata.py {input} > {output}"



rule merge_metadata_to_csv:
    input:
        expand("../data/processed/{vid}.json", vid=VIDEO_NAMES)
    output:
        "../data/final/movie_paths.csv"
    conda:
        "environment.yml"
    script:
        "scripts/merge_json_to_csv.py"
    