import configparser

from traceability.traceability import Traceability

config = configparser.ConfigParser()
config.read(r'C:\Club Car Programming\python_scripts\config\config.ini')

newtonsoftjson_path = config['Paths']['Newtonsoft.Json.Dll']
wsconnector_path = config['Paths']['WSConnector.Dll']

stationName = config['Process']['StationName']
partNumber = config['Process']['PartNumber']
processName = config['Process']['ProcessName']

def main():
    KEMX_traz = Traceability(wsconnector_path, newtonsoftjson_path)
    KEMX_traz.set_general_pcb(stationName, partNumber, processName)
    serial = 'FNTD001WA'
    KEMX_traz.set_pcb_test(serial)

    
    pn = KEMX_traz._traceability_partNumber()
    print(f'pn {pn}')
    bk = KEMX_traz._traceability_backCheck()
    print(f'bk {bk}')


if __name__ == "__main__":
    main()
