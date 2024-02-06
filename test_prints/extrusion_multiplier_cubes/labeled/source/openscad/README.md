
To use the python script yout have to install python-click and python-numpy. 


```
Usage: em_cube.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  generate        generate a em_cube.stl
  generate-cubes  A script to generate multiple extrusion multiplier cubes


```

```
Usage: em_cube.py generate [OPTIONS] LABEL

  generate a em_cube.stl

Options:
  --cube-width FLOAT    width of the cube
  --cube-depth FLOAT    depth of the cube
  --cube-height FLOAT   height of the cube
  --text-size FLOAT     text size of the label
  --layer-height FLOAT  layer height
  --help                Show this message and exit.
```

```
Usage: em_cube.py generate-cubes [OPTIONS] [EM_START] [EM_END] [EM_INTERVAL]

  A script to generate multiple extrusion multiplier cubes

Options:
  --cube-width FLOAT    width of the cube
  --cube-depth FLOAT    depth of the cube
  --cube-height FLOAT   height of the cube
  --text-size FLOAT     text size of the label
  --layer-height FLOAT  layer height
  --help                Show this message and exit.
```