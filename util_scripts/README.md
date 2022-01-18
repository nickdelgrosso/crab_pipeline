

## Running JupyterLab on a Remote Server

Exposing Jupyter to the outside

```
 jupyter lab --no-browser --ip "*" --collaborative
```


Port forwarding SSH

```
 ssh -L 8888:localhost:8888 username@ipaddress
```

