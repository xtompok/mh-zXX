import serial
import logging

class MhZ(object):

	cmd_zero_sensor = b'\xff\x87\x87\x00\x00\x00\x00\x00\xf2'
	cmd_span_sensor = b'\xff\x87\x87\x00\x00\x00\x00\x00\xf2'
	cmd_get_sensor = b'\xff\x01\x86\x00\x00\x00\x00\x00\x79'
	
	def __init__(self,port):
		self.ser = serial.Serial(port,9600,timeout=1)
	
	def _checksum_check(self,data):
		checksum = sum(data[1:8])
		checksum = 0xFF-(checksum%256)+1
		if checksum == data[8]:
			return True
		return False
		
	def read_CO2_temp(self):
		try:
			self.ser.write(self.cmd_get_sensor)
			data = list(self.ser.read(9))
			if not self._checksum_check(data):
				logging.warning("Checksum error")
				return None
			logging.debug("data: {}".format(str(data)))
			return (data[3]+256*data[2],data[4]-40)
		except IOError:
			logging.warning("IO error when reading")
			return None
	
	def read_CO2(self):
		CO2_temp = self.read_CO2_temp()
		if CO2_temp:
			return CO2_temp[0]
		return None
	
	def read_temp(self):
		CO2_temp = self.read_CO2_temp()
		if CO2_temp:
			return CO2_temp[1]
		return None
					

	def calibrate_zero(self):
		try:
			self.ser.write(self.cmd_zero_sensor)
			logging.info("Zero calibrated")
		except IOError:
			logging.warning("Write error when calibrating")

		
	
	def calibrate_span(self):
		raise NotImplementedError("Span calibration not implemented")
	

