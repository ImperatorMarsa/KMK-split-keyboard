import board

from kmk.modules.split import Split, SplitType

split = Split(
    split_type=SplitType.UART,
    split_target_left=True,
    data_pin=board.RX,
    data_pin2=board.TX,
    uart_flip=True,
    use_pio=True,
)
