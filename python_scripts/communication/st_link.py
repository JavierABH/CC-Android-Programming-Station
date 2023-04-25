import subprocess

program_path = r'C:\Program Files (x86)\STMicroelectronics\st_toolset\stvp\STVP_CmdLine.exe'
bootloader_path = r'C:\Club Car Programming\firmware\bootloader\stm8bootloader.s19'

command = [
    program_path,
    '-BoardName=ST-LINK',
    '-Port=USB',
    '-ProgMode=SWIM',
    '-Device=STM8AF528',
    f'-FileProg={bootloader_path}',
    '-verif',
    '-no_loop',
    '-no_log',
    '-verbose'
]

subprocess.call(command)