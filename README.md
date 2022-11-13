create conda enviroment
```bash
conda create -n BigMartSale python=3.8 -y
```
run requirements.txt
```bash
pip install -r requirements.txt
```
initialize git
```bash
git init
```

initialize dvc
```bash
dvc init
```
to track data by dvc
```bash
dvc add data_given/bigmartdata.csv
```
check to metrics and scores using dvc
```bash
dvc metrics show
```
to check the metrics differences and scores

```bash
dvc metrics diff
```


