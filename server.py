import pyaudio, socket

port = 5000
chunk = 8192
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()
stream = p.open(format = FORMAT, channels = CHANNELS, rate = RATE, input = True, output = True, frames_per_buffer = chunk)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create the socket
server_socket.bind(('', port)) # listen on port 5000
server_socket.listen(50) # queue max 5 connections
client_socket, address = server_socket.accept()

print("Your IP address is: ", socket.gethostbyname(socket.gethostname()))
print("Server Waiting for client on port ", port)

while True:
    try:
        client_socket.sendall(stream.read(chunk))
    except IOError as e:
        if e[1] == pyaudio.paInputOverflowed:
            print(e)
            x = '\x00'*16*8192*2


stream.stop_stream()
stream.close()
server_socket.close()
client_socket.close()
p.terminate()