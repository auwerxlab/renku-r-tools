import click
from renku_r_tools.packrat import Packrat

@click.group()
def cli():
    """ \b
A toolbox to work with R projects on Renku
    """
    pass

@cli.group()
def packrat():
    """ \b
Commands for the packrat package
    """
    pass

@packrat.command(help = 'Link packrat libraries to another location.')
@click.option('-p', '--proj_dir',
    help = 'R project main directory path. Use absolute path.',
    required = True)
@click.option('-s', '--source',
    default = '/home/rstudio/packrat',
    help = 'Main directory path of the new packrat libraries source. \
Use absolute path.',
    required = True,
    show_default = True)
@click.option('-f', '--force',
    is_flag = True,
    help = 'Overwrite existing libraries.')
@click.option('-v', '--verbose',
    is_flag = True,
    help = 'Print various messages.')
def use_lib_links(proj_dir, source, force, verbose):
    packrat = Packrat(proj_dir = proj_dir)
    packrat.ln_lib(ln_source = source,
        force = force,
        verbose = verbose)

if __name__ == '__main__':
    cli()
