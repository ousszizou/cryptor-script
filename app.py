import click
import config

@click.group(invoke_without_command=True,context_settings=config.CONTEXT_SETTINGS)
def cli():
    print("""
                """+config.colors['yellow']+"""
                 _________________________
                #                         #
                 #    [CryptoR  Script]    #
                #      """+config.colors['green']+"""   ==V 0.1==    """+config.colors['yellow']+"""   #
                 #    """+config.colors['red']+""" {By: algorithm}  """+config.colors['yellow']+"""   #
                #_________________________#

            """+config.colors['blue']+"""[*]---------------------------[*]
                    """+config.colors['white']+"""to run the script :
                      > """+config.colors['cyan']+"""cryptor run"""+config.colors['reset']+"""
        """
    )

@cli.command(help='Show how to use the script')
def run():
    import sign

@cli.command(help='Use encryption algorithm')
@click.option('--name', default='cc', help="name of encryption algorithm", type=click.Choice(['cc', 'aes', 'des', 'idea', '3des']))
def algorithm(name):
    exec("import algorithms.{}".format(name))
