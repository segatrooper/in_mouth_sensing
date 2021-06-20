import serial, time, keyboard, signal, sys
from pathlib import Path

def signal_handler(sig, frame):
    print('exiting mode')
    file.close()
    sys.exit(0)

file_name = input("what is the file name?: ")
no_sensors = 4 # int(input("how many sensors?: "))
# sample_per_window = float(input("what is the sample per window: "))
# window_offset = float(input("what is the offset (in seconds): ")) * 1000000

if not (Path("./output/" + file_name + ".csv").exists()):
    with open(file_name + '.csv', "a") as f:
        f.write("keypressed,")
        output = ""
        for i in range(no_sensors):
            output += f",sensor {i}"
        f.write(output[1:] + "\n")
arduino = serial.Serial('COM4', 115200, timeout=.1)
time.sleep(1)
window = list()
time = 0; prev = 0; delta = 0; window_counter = 0;
file = open("./output/" + file_name + '.csv', "a")
signal.signal(signal.SIGINT, signal_handler)
while True:
    data = arduino.readline()
    # print(data)
    if data:
        keypress = 1 if keyboard.is_pressed(' ') else 0
        proc_data = str(data)[2:-6]
        print(f"{keypress}," + proc_data)
        file.write(f"{keypress}," + proc_data +"\n")


