import click
from renku_r_tools.packrat import Packrat

@click.group()
def cli():
    pass

@cli.command(help = 'Link packrat libraries to another location.')
@click.option('-p', '--proj_dir',
    help = 'R project main directory path. Use absolute path.',
    required = True)
@click.option('-s', '--source',
    default = '/home/rstudio/packrat',
    help = 'Main directory path of the new packrat libraries source. \
Use absolute path.',
    required = True,
    show_default = True)
def ln_packrat_lib(proj_dir, source):
    packrat = Packrat(proj_dir = proj_dir)
    packrat.ln_lib(ln_source = source)

if __name__ == '__main__':
    cli()
