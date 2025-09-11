My personal Python Package

## Create a Python virtual enviroment

```bash
python3 -m venv vevn
```

#### Enter

```bash
source source venv/bin/activate
```

- To leave run
```bash
deactivate
```

### intall build

```bash
pip install build
```

#### In the same dir of .toml

```bash
python3 -m build
```

This will create a dist folder with:
ft_package-0.0.1-py3-none-any.whl and ft_package-0.0.1.tar.gz

You can install the package from any one of those.

### Install ft_package

```bash
pip install /dist/ft_package-0.0.1-py3-none-any.whl
or 
pip install /dist/ft_package-0.0.1.tar.gz
```


Run the test
