from machine import Pin, I2C, PWM
from ssd1306 import SSD1306_I2C
from hcsr04 import HCSR04
import utime

oled = SSD1306_I2C(128, 64, I2C(scl=Pin(5), sda=Pin(4)))
sonar = HCSR04(trigger_pin=14, echo_pin=12)

buzzer = PWM(Pin(15, Pin.OUT), freq=784, duty=0)

sound_delay = 500
buzzer_time = utime.ticks_ms()

while True:
    
#####
    # 設定超音波測距範圍為 2~50公分  ，這個距離值乘上10 就是while迴圈停頓的時間值（20~500 毫秒）
    # 超音波模組偵測到物體時，也要讓蜂鳴器發出短促聲響：蜂鳴器會響10毫秒在關閉，避免變成連續音，while迴圈的等待時間要再減去10毫秒
    
#####
    distance = sonar.distance_cm()
    oled.fill(0)
    oled.text("Distance:", 0, 0)
    oled.text(str(distance) + " cm", 0, 16)
    oled.show()
    print("偵測距離: " + str(distance) + " 公分")
    
    if 2 <= distance <= 50:
        buzzer.duty(512)
        utime.sleep_ms(10)
        buzzer.duty(0)
        sound_delay = int(distance) * 10 - 10
    else:
        sound_delay = 500
    
    utime.sleep_ms(sound_delay)
    

