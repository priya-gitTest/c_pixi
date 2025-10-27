# c_pixi
# MathOps

A simple Python package for basic math operations.

## Installation
```bash
pip install mathops
```

## Usage
```python
from mathops import add, multiply

result = add(5, 3)
print(result)  # 8

result = multiply(4, 7)
print(result)  # 28
```

## SETUP

Let's add a dependency-group, which Pixi calls a feature, named test. And add the pytest package to this group.
```bash
pixi add --pypi --feature test pytest
✔ Added pytest
Added these as pypi-dependencies.
Added these only for feature: test
```bash

```toml
[dependency-groups]
test = ["pytest"]
```bash

After we have added the dependency-groups to the pyproject.toml, Pixi sees these as a feature, which can contain a collection of dependencies, tasks, channels, and more.
```bash
pixi workspace environment add default --solve-group default --force
✔ Updated environment default
pixi workspace environment add test --feature test --solve-group default
✔ Added environment test
```

```toml
[tool.pixi.environments]
default = { solve-group = "default" }
test = { features = ["test"], solve-group = "default" }
```
Without specifying the environment name, Pixi will default to the default environment. If you want to install or run the test environment, you can specify the environment with the --environment flag.

```bash
pixi install --environment test
pixi run --environment test pytest

pixi add --pypi --feature dev ruff
pixi add --pypi --feature dev build
pixi add --pypi --feature dev twine
```

```toml
[dependency-groups]
test = ["pytest>=8.4.2,<9", "ruff>=0.14.2,<0.15"]
dev = ["ruff", "build", "twine"]
```
```bash
pixi workspace environment add dev  --feature dev  --solve-group default
✔ Added environment dev
```
```toml
[tool.pixi.environments]
default = { solve-group = "default" }
test = { features = ["test"], solve-group = "default" }
dev = { features = ["dev"], solve-group = "default" }

[dependency-groups]
test = ["pytest>=8.4.2,<9", "ruff>=0.14.2,<0.15"]
dev = ["ruff", "build", "twine"]
```
---
Copy the given Pyproject.toml,
then run in the order
```bash
# Lint
pixi run lint
pixi run lint-fix 
pixi run format

# Test
pixi install
pixi run test

#  Build
git init
git add .
git commit -m "Initial commit of pixi calculator package"
git tag v0.1.0
pixi run build-package
pixi run check-package

# Publish
pixi run upload-test

# for subsequent releases,
git add .
git commit -m "feat: Add division operation and update documentation"
git push
# Create the tag for the second release
git tag v0.2.0
```
# Push the new tag to your remote repository
git push origin v0.2.0
