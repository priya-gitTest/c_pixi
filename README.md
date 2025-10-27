# c_pixi
c and Pixi

Let's add a dependency-group, which Pixi calls a feature, named test. And add the pytest package to this group.

pixi add --pypi --feature test pytest
✔ Added pytest
Added these as pypi-dependencies.
Added these only for feature: test

[dependency-groups]
test = ["pytest"]

After we have added the dependency-groups to the pyproject.toml, Pixi sees these as a feature, which can contain a collection of dependencies, tasks, channels, and more.

pixi workspace environment add default --solve-group default --force
✔ Updated environment default
pixi workspace environment add test --feature test --solve-group default
✔ Added environment test

[tool.pixi.environments]
default = { solve-group = "default" }
test = { features = ["test"], solve-group = "default" }

Without specifying the environment name, Pixi will default to the default environment. If you want to install or run the test environment, you can specify the environment with the --environment flag.


pixi install --environment test
pixi run --environment test pytest