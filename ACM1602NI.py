from utime import sleep_ms

lcd_addr = 0x50
_command = 0x00
_data = 0x80
_clear = 0x01
_home = 0x02
_mode = 0x38  # 8bit 2line 5×8dot
display_On = 0x0c
LCD_HOME_ADDRESS = 0x80

LINE_MAX = 2
LINE_CHARA_MAX = 16
LINE_HEAD_ADDR_TBL = [0x00, 0x40]


class ACM1602NI:

    def __init__(self, i2c=None, address=lcd_addr):
        self.i2c = i2c
        self.address = address

    def writeReg(self, reg_address, data):
        self.i2c.writeto_mem(lcd_addr, reg_address, data)

    def command(self, code):
        dt = bytearray(1)
        dt[0] = code
        self.writeReg(_command, dt)
        sleep_ms(3)

    def write_lcd(self, text):
        dt = bytearray(1)
        bin = text.encode("utf-8")
        for ch in bin:
            dt[0] = ch
            self.writeReg(_data, dt)

    def localte(self, x, y):
        if x >= LINE_CHARA_MAX:
            x = LINE_CHARA_MAX - 1
        if y >= LINE_MAX:
            y = LINE_MAX - 1
        lineaddr = 0x80 + LINE_HEAD_ADDR_TBL[y] + x
        self.command(lineaddr)

    def lcd_clear(self):
        self.command(_clear)

    def lcd_home(self):
        self.command(_home)

    def init(self):
        self.command(_mode)
        self.command(_clear)
        self.command(display_On)
