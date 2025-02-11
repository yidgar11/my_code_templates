# 1. Repository management 

## Add Repository
```shell
helm repo add NAME URL
```

## Update Repositories
```shell
helm repo update
```

## Search Charts in Repositories
```shell
helm search repo KEYWORD
```

# 2. Basic commands 
## Package the chart (optional):
```shell
helm package my-helm-chart/
```
## Install the chart with default values:
```shell
helm install my-release my-helm-chart/
```
## Override values during installation (example): 
```shell
helm install my-release my-helm-chart/ --set replicaCount=3 --set ingress.enabled=true --set ingress.hosts[0].host=myapp.local
```
## Upgrade a Release
```shell
helm upgrade RELEASE CHART
```

## Uninstall a Release
```shell
helm uninstall RELEASE
```

# 3. Chart Management

## Download a Chart
Downloads a chart locally. Use `--untar` to extract it into a directory.

```shell
helm pull CHART
```

## List Chart Dependencies
Displays the dependencies of a chart.
```shell
helm dependency list CHART
```

## Package a Chart
Packages a chart directory into a `.tgz` archive.
```shell
helm package DIR
```
