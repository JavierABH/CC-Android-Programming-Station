import clr

class Traceability:
    def __init__(self, wsconnector_path, newtonsoftjson_path):
        clr.AddReference(newtonsoftjson_path)
        clr.AddReference(wsconnector_path)
        from WSConnector import Connector
        self.connector = Connector()

        self.expected_partNumber = ""
        self.stationName = ""
        self.processName = ""
        self.employee = ""

        self.serial = ""
        self.partNumber = ""

    def set_general_pcb(self, stationName, partNumber, processName):
        self.stationName = stationName
        self.expected_partNumber = partNumber
        self.processName = processName

    def set_pcb_test(self, serial):
        self.serial = serial     

    def _traceability_partNumber(self):
        str_useless = ""
        partNumber, str_useless = self.connector.CIMP_PartNumberRef(self.serial, 2, str_useless)
        return partNumber

    def _traceability_backCheck(self):
        reply_backCheck = self.connector.BackCheck_Serial(self.serial, self.stationName)
        return reply_backCheck

    def _traceability_partNumberVirtual(self):
        partNumberVirtual = self.connector.FindFinishedPartNumVirtual(self.serial)
        return partNumberVirtual
  
    def _MacAddres_BySerial(self):
        reply_mac = self.connector.Get_MacAddres_BySerial(self.serial, self.expected_partNumber, self.stationName)
        return reply_mac

    def _traceability_insertProcess(self):
        pass

    def reply_partNumber(self):
        pass

    def reply_backCheck(self):
        pass

    def reply_insertProcess(self):
        pass
