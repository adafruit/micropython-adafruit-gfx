import gfx

import machine
import ili9341
spi = machine.SPI(1, baudrate=32000000)
display = ili9341.ILI9341(spi, cs=machine.Pin(0), dc=machine.Pin(15))
display.fill(0)
graphics = gfx.GFX(240, 320, display.pixel)
#graphics.line(0, 0, 120, 160, ili9341.color565(255, 0, 0))
#graphics.line(239, 319, 120, 170, ili9341.color565(255, 255, 0))
#graphics.fill_circle(120, 160, 30, ili9341.color565(255, 0, 255))
#graphics.fill_rect(0, 0, 120, 160, ili9341.color565(255, 0, 0))
graphics.fill_triangle(0,0,120,165,0,160, ili9341.color565(255,0,0))
