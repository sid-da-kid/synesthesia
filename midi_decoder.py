import mido
import rtmidi
from mido import Message
msg = Message('note_on', note=60)
print(msg.type)
print(msg.channel)
print(msg.note)
print(msg.velocity)
outport = mido.open_output()
outport.send(msg)
