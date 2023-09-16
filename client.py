import pyaudio, socket

port = 5000
ip = "127.0.0.1"

chunk = 8192
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()
stream = p.open(format = FORMAT, channels = CHANNELS, rate = RATE, input = True,output = True, frames_per_buffer = chunk)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip, port))
while True:
    data = client_socket.recv(32768)
    if data == b"":
        continue
    stream.write(data,chunk)

socket.close()