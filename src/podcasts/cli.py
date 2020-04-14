# -*- coding: utf-8 -*-

"""Console script for podcasts."""
import sys
import click
from podcasts import recommendations


@click.command()
def afterhours(args=None):
    """Console script for podcasts."""
    click.echo("Replace this message by putting your code into "
               "podcasts.cli.main")

    return recommendations(url="http://feeds.harvardbusiness.org/harvardbusiness/after-hours")

#
# if __name__ == "__main__":
#     sys.exit(main())  # pragma: no cover
