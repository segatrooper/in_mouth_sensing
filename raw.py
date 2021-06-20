import serial, time, keyboard, signal, sys
from pathlib import Path


def signal_handler(sig, frame):
    print('exiting mode')
    file.close()
    sys.exit(0)


def getInput():
    return input("what is the file name?: "), int(input("how many sensors?: "))




if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    file_name, no_sensors = getInput()
    # sample_per_window = float(input("what is the sample per window: "))
    # window_offset = float(input("what is the offset (in seconds): ")) * 1000000

    # if not (Path("./" + file_name + ".csv").exists()):
        # with open(file_name + '.csv', "a") as f:
            # f.write("window,time")
            # for i in range(no_sensors):
                # f.write(f",sensor{i}")
            # f.write("\n")

    arduino = serial.Serial('COM5', 115200, timeout=.1)
    time.sleep(0.5)
    window = list()
    time = 0; prev = 0; delta = 0; window_counter = 0;
    if not Path("./output").is_dir():
        Path("./output").mkdir()
    file = open("./output/"+ file_name + '.csv', "a")
    while True:
        data = arduino.readline()
        if data:
            if str(data)[2:-6].split(",")[0] == '': continue
            output = ",".join([str(int(i) - 2048) for a, i in enumerate(str(data)[2:-6].split(","))])
            keypress = 1 if keyboard.is_pressed(' ') else 0
            file.write(output + "," + str(keypress) + "\n")
            print(output + "," + str(keypress))
            # print(str(data)[2:-6]
            prev = time; time = int(str(data)[2:-6].split(",")[0]); delta += time - prev
            # print(str(data))
            # print(str(data)[2:-6])

