import clr

class Traceability:
    def __init__(self, wsconnector_path, newtonsoftjson_path):
        clr.AddReference(newtonsoftjson_path)
        clr.AddReference(wsconnector_path)
        from WSConnector import Connector
        self.connector = Connector()

        self.expected_part_number = ""
        self.part_number = ""
        self.station_name = ""
        self.process_name = ""
        self.employee = ""

    def set_general_pcb(self):
        pass

    def set_pcb_test(self, serial):
        self.serial = serial

    def _traceability_partNumber(self):
        useless = ""
        self.part_number, useless = self.connector.CIMP_PartNumberRef(self.serial, 2, useless)
        return self.part_number


    def _traceability_backcheck(self):
        pass

    def _traceability_insert_process(self):
        pass

    def reply_part_number(self):
        pass

    def reply_backcheck(self):
        pass

    def reply_insert_process(self):
        pass
