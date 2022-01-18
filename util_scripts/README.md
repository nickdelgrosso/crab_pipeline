

## Running JupyterLab on a Remote Server

Awesome article: https://towardsdatascience.com/how-to-connect-to-jupyterlab-remotely-9180b57c45bb

Exposing Jupyter to the outside

```
 jupyter lab --no-browser --ip "*" --collaborative
```


Port forwarding SSH

```
 ssh -L 8888:localhost:8888 username@ipaddress
```

