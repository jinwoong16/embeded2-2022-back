import board
import adafruit_dht
import psutil

def temphum(): 
  for proc in psutil.process_iter():
    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
      proc.kill()
  sensor = adafruit_dht.DHT11(board.D23)

  temperature = sensor.temperature
  humidity = sensor.humidity
  return temperature, humidity

if __name__=="__main__":
  a, b = temphum()
  print(a, b)