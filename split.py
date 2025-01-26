import board
from storage import getmount

from kmk.modules.split import Split, SplitType, SplitSide

_splitSide = (
    SplitSide.RIGHT if str(getmount("/").label).endswith("R") else SplitSide.LEFT
)

split = Split(
    split_side=_splitSide,
    split_type=SplitType.UART,
    split_target_left=True,
    data_pin=board.RX,
    data_pin2=board.TX,
    uart_flip=True,
    use_pio=True,
)
