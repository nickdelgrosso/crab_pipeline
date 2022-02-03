

rule all:
    input:
        "./NINJAV_S001_S001_T003.json"


rule extract_metadata:
    input:
        "/data/raw/NINJAV_S001_S001_T003.MOV"
    output:
        "./NINJAV_S001_S001_T003.json"
    shell:
        "python scripts/extract_metadata.py {input} > {output}"