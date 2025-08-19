from kb import encoderAPin, encoderBPin
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler


def setUpEncoder(encoder_handler):
    encoder_handler.pins = ((encoderAPin, encoderBPin, None),)

    encoder_handler.map = [
        ((KC.VOLD, KC.VOLU, KC.MUTE),),
    ]


encoder_handler = EncoderHandler()
