class SMBus:
    def __init__(self, bus):
        pass

    def write_byte(self, addr, data):
        raise NotImplementedError()

    def write_byte_data(self, addr, reg, data):
        raise NotImplementedError()

    def write_i2c_block_data(self, addr, reg, data):
        raise NotImplementedError()

    def read_byte(self, addr):
        raise NotImplementedError()

    def read_i2c_block_data(self, addr, reg, num):
        raise NotImplementedError()

    def write_word_data(self, addr, reg, data):
        raise NotImplementedError()
