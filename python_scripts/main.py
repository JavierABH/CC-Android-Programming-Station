import configparser

from traceability.traceability import Traceability

config = configparser.ConfigParser()
config.read(r'C:\Club Car Programming\python_scripts\config\config.ini')

newtonsoftjson_path = config["Paths"]["Newtonsoft.Json.Dll"]
wsconnector_path = config["Paths"]["WSConnector.Dll"]

def main():
    KEMX_traz = Traceability(wsconnector_path, newtonsoftjson_path)

    KEMX_traz.set_pcb_test('47752390001REV DFNTD001X4')
    pn = KEMX_traz._traceability_partNumber()
    print(pn)

if __name__ == "__main__":
    main()
