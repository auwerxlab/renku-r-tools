import click
from renku_r_tools.packrat import Packrat
from renku_r_tools.renv import Renv

@click.group()
def cli():
    """ \b
A toolbox to work with R projects on Renku
    """
    pass

@cli.group()
def packrat():
    """ \b
Commands linked to the R packrat package
    """
    pass

@packrat.command(name = "use_lib_links",
    help = 'Replace packrat libraries locations by links.')
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
def packrat_use_lib_links(proj_dir, source, force, verbose):
    packrat = Packrat(proj_dir = proj_dir)
    packrat.ln_lib(ln_source = source,
        force = force,
        verbose = verbose)

@cli.group()
def renv():
    """ \b
Commands linked to the R renv package
    """
    pass

@renv.command(name = "use_lib_links",
    help = 'Replace renv libraries locations by links.')
@click.option('-p', '--proj_dir',
    help = 'R project main directory path. Use absolute path.',
    required = True)
@click.option('-s', '--source',
    default = '/home/rstudio/renv',
    help = 'Main directory path of the new renv libraries source. \
Use absolute path.',
    required = True,
    show_default = True)
@click.option('-f', '--force',
    is_flag = True,
    help = 'Overwrite existing libraries.')
@click.option('-v', '--verbose',
    is_flag = True,
    help = 'Print various messages.')
def renv_use_lib_links(proj_dir, source, force, verbose):
    renv = Renv(proj_dir = proj_dir)
    renv.ln_lib(ln_source = source,
        force = force,
        verbose = verbose)
        
if __name__ == '__main__':
    cli()
