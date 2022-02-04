

rule all:
    input:
        "./data/processed/NINJAV_S001_S001_T003.json"


rule extract_metadata:
    input:
        "/data/raw/{rawmov}.MOV"
    output:
        "./data/processed/{rawmov}.json"
    conda:
        "scripts/extract_rawvid_metadata/environment.yml"
    shell:
        "python pipeline_steps/extract_rawvid_metadata/extract_metadata.py {input} > {output}"
