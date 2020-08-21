Include data files here.

This file may be accessed with:

```Python
from pkg_resources import resource_filename
data_file = resource_filename("{{ cookiecutter.project_slug }}", "data/README.md")
```
