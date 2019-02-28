import os
import sys
import config

def printSign():
    scriptName = os.path.basename(sys.argv[0])
    print("""
        """+config.colors['magenta']+"""   { Encryption algorithms are available }\n
             """+config.colors['yellow']+"""/*/ Conventional Cryptography /*/\n"""+config.colors['white']+"""
                  > """+config.colors['cyan']+""" [1] """+config.colors['white']+""" Casear Cipher(cc)
                  > """+config.colors['cyan']+""" [2] """+config.colors['white']+""" DES
                  > """+config.colors['cyan']+""" [3] """+config.colors['white']+""" AES
                  > """+config.colors['cyan']+""" [4] """+config.colors['white']+""" IDEA
                  > """+config.colors['cyan']+""" [5] """+config.colors['white']+""" 3DES
                
    """+config.colors['underline']+""""""+config.colors['red']+"""usage:"""+config.colors['reset']+""" """ + scriptName + """ """+config.colors['italic']+ """algorithm [OPTIONS]"""+config.colors['reset']+"""\n
    """+config.colors['green']+"""example:"""+config.colors['reset']+"""
    if you want to select the """+config.colors['yellow']+"""casear cipher algorithm"""+config.colors['reset']+""", Enter this command\n
            """ + scriptName + """"""+config.colors['cyan']+""" algorithm --name cc """+config.colors['reset']+"""\n
    if you want to select the """+config.colors['yellow']+"""3DES algorithm"""+config.colors['reset']+""", Enter this command\n
            """ + scriptName + """"""+config.colors['cyan']+""" algorithm --name=3des """+config.colors['reset']+"""\n"""
    )

printSign()
