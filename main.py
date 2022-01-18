from pickle import NONE
from bluepy import btle
import sys

DEVICE_UUID = "f4:d4:88:61:ce:97"
SERVICE_UUID = "FCC6AD8D-A8EF-475F-B0FD-D106C00882FC"
CHARACTERISTIC_UUID = "B5D06B73-0B67-4861-B336-3386C2FF8A7B"

def handleCharacteristic(char):
  # print("handleCharacteristic()")
  data = char.read()
  print(data)

scanner = btle.Scanner(0) #index=0 が /dev/hci0 に対応する


peripheral = btle.Peripheral()

def loop():
  devices = scanner.scan(0.1)
  for device in devices:
    if device.addr == "f4:d4:88:61:ce:97":
      peripheral.connect(device.addr, btle.ADDR_TYPE_PUBLIC)

  if peripheral.addr:
    for service in peripheral.getServices():
      if service.uuid == SERVICE_UUID:
        for characteristic in service.getCharacteristics():
          if characteristic.uuid == CHARACTERISTIC_UUID:
            handleCharacteristic(characteristic)
            break
        break

while True:
  try:
    loop()
  except btle.BTLEException:
    ex, ms, tb = sys.exc_info()
    # print("BLE Exeption" + str(type(ms)) + "at" + sys._getframe().f_code.co_name)
