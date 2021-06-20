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


arduino = serial.Serial('COM7', 115200, timeout=.1)
time.sleep(1)
window = list()
# time = 0; prev = 0; delta = 0; window_counter = 0;
delta = 0
signal.signal(signal.SIGINT, signal_handler)



if not (Path("./output/" + file_name + ".csv").exists()):
    with open("./output/" + file_name + ".csv", "a") as f:
        f.write("keypressed,")
        output = ""
        for i in range(no_sensors):
            output += f",sensor {i}"
        f.write(output[1:] + "time\n")
        
        
ftime = time.time()
file = open("./output/" + file_name + '.csv', "a")
while True:
    keypress = 1 if keyboard.is_pressed(' ') else 0
    data = arduino.readline() # 3rd sensor
    if data:
        data = list(data)
        for a,b in enumerate(data):
            if b == 0:
                start = a + 1
                break
        for i in range(start, len(data)):
            if (data[i] == 0):
                if len(window) == 8:
                    ws = []
                    for i in range(4):
                        ws.append(window[2*i]*256 + window[(2*i)+1])
                    window = []
                    output = f"{keypress}," + ",".join([str(x) for x in ws]) + "," + str(time.time() - ftime)
                    file.write(output + "\n")
                    print(delta)
                else:
                    window = []
                delta += 1
                
            else:
                window.append(data[i])
        break
    # data = arduino.readline() # 3rd sensor
    # if data:
        # print(list(data))
while True:
    keypress = 1 if keyboard.is_pressed(' ') else 0
    data = arduino.readline()
    # print(data)
    if data:
        for i in range(0, len(data)):
            if (data[i] == 0):
                if len(window) == 8:
                    ws = []
                    for i in range(4):
                        ws.append(window[2*i]*256 + window[(2*i)+1])
                    window = []
                    output = f"{keypress}," + ",".join([str(x) for x in ws]) + "," + str(time.time() - ftime)
                    file.write(output + "\n")
                    print(output)
                else:
                    window = []
                delta += 1
                
            else:
                window.append(data[i])
            
