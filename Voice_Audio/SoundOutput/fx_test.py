from SoundFX import PlayEffect
from time import sleep

effect = 'good'

PlayEffect(effect)
sleep(1.0)
effect = 'bad'
PlayEffect(effect)


