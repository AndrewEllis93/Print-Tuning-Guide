# coding: utf-8

##
# install python-click, python-numpy and openscad to use this script
#

import subprocess
import numpy as np
import click 

@click.group()
def cli():
    pass


def generate_cube(cube_width, cube_depth, cube_height, layer_height, label, text_size):
   command = [
        'openscad', 'em_cube.scad',
        '-D', f'em_value={label}',
        '-D', f'cube_width={cube_width:.3f}',
        '-D', f'cube_depth={cube_depth:.3f}',
        '-D', f'cube_height={cube_height:.3f}',
        '-D', f'layer_height={layer_height:.3f}',
        '-D', f'text_size={text_size:.1f}',
        '-o', f'em_cube_{label}.stl',
        '--export-format', 'binstl',
        ]
   result = subprocess.run(command, capture_output=True)
   print(f'openscad ..... -D em_value="{label}" -o em_cube_{label}.stl .....') 
   print(result)
 

@click.command('generate')
@click.option('--cube-width', default=30.0, type=float, help='width of the cube')
@click.option('--cube-depth', default=30.0, type=float, help='depth of the cube')
@click.option('--cube-height', default=3.0, type=float, help='height of the cube')
@click.option('--text-size', default=6, type=float, help='text size of the label')
@click.option('--layer-height', default=0.2, type=float, help='layer height')
@click.argument('label', type=str)
def generate_cube_subcmd(cube_width, cube_depth, cube_height, layer_height, label, text_size) :
    """ generate a em_cube.stl"""
    generate_cube(cube_width, cube_depth, cube_height, layer_height, label, text_size)
 
@click.command()
@click.argument('em_start', type=float, default=0.85)
@click.argument('em_end', default=1.05)
@click.argument('em_interval', default=0.01)
@click.option('--cube-width', default=30.0, type=float, help='width of the cube')
@click.option('--cube-depth', default=30.0, type=float, help='depth of the cube')
@click.option('--cube-height', default=3.0, type=float, help='height of the cube')
@click.option('--text-size', default=6, type=float, help='text size of the label')
@click.option('--layer-height', default=0.2, type=float, help='layer height')
def generate_cubes(em_start, em_end, em_interval, cube_width, cube_depth, cube_height, layer_height, text_size):
    """A script to generate multiple extrusion multiplier cubes"""
    for em_value in np.arange(em_start, em_end, em_interval ):
        generate_cube(cube_width, cube_depth, cube_height, layer_height, str(f'{em_value:.3f}'), text_size)


cli.add_command(generate_cubes)
cli.add_command(generate_cube_subcmd)


if __name__ == '__main__':
    cli()
