from machine import Pin
import time

# 4 顆 LED，依左到右排列
PINS = [5, 2, 15, 4]
leds = [Pin(p, Pin.OUT) for p in PINS]

def all_off():
    for led in leds:
        led.off()

# -------------------------------------------------------
# Knight Rider 效果：
#   LED 從左到右掃描，到底後反向，來回不停。
#
# 執行結果（每步 0.15 秒）：
#   [*][ ][ ][ ]
#   [ ][*][ ][ ]
#   [ ][ ][*][ ]
#   [ ][ ][ ][*]
#   [ ][ ][*][ ]
#   [ ][*][ ][ ]
#   [*][ ][ ][ ]  ← 重複
#
# 變數說明：
#   pos       目前亮的 LED 索引（0 = 最左，3 = 最右）
#   direction 移動方向（+1 向右，-1 向左）
# -------------------------------------------------------

pos = 0
direction = 1

while True:
<<<<<<< HEAD
    # 熄滅所有 LED
    all_off()

    # 點亮索引 pos 的 LED
=======
    all_off()
>>>>>>> 073cd20a7462cdd452fe386bbc0d52a10643ed92
    leds[pos].on()

    time.sleep(0.15)

<<<<<<< HEAD
    # 將 pos 移動一步（依 direction）
    pos += direction

    # 若 pos 超出範圍，反轉 direction，並把 pos 修正回合法範圍內
=======
    pos += direction
>>>>>>> 073cd20a7462cdd452fe386bbc0d52a10643ed92
    if pos >= len(leds):
        direction = -1
        pos = len(leds) - 2
    elif pos < 0:
        direction = 1
        pos = 1
