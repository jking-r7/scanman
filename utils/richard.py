#!/usr/bin/env python3

# from rich.table import Table
from rich import box
from rich.console import Console
from rich.logging import RichHandler
from rich.panel import Panel
from rich.theme import Theme
from utils import arguments
import logging



# Args - init.
args = arguments.parse_args()
loglevel = args.loglevel

# Rich console and theme init.
themefile = './utils/theme.ini'
mytheme = Theme().read(themefile)
console = Console(theme=mytheme)

# logger - Rich
logging.basicConfig(
	# filename='',
	level=loglevel,
	format='%(message)s',
	datefmt='[%X]',
	handlers=[RichHandler(console=console, rich_tracebacks=True, omit_repeated_times=False)]
	)
logging = logging.getLogger('rich')


def banner(banner_title):
	''' Rich util Banner.'''

	print('\n')
	console.print(Panel('', title=f'[h1]{banner_title}', 
		height=1, width=125, box=box.DOUBLE_EDGE, style='deep_sky_blue4'))