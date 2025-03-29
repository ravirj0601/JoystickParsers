
# Import the necessary libraries
import asyncio
import socketio

# Create a SocketIO client
sio = socketio.AsyncClient()

# Connect to the server
async def connect():
    await sio.connect('http://10.0.1.18:5000')

# Define a function to handle incoming messages
@sio.on('message')
async def on_message(data):
    print('Received message:', data)

# Define a function to send messages to the server
async def send_message():
    while True:
        message = input('Enter message to send: ')
        await sio.emit('message', message)

# Start the event loop and connect to the server
async def main():
    await connect()

    # Create a task to send messages to the server
    send_task = asyncio.create_task(send_message())

    # Wait for the tasks to complete
    await send_task

    # Disconnect from the server
    await sio.disconnect()

if __name__ == '__main__':
    asyncio.run(main())
