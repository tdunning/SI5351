# SPDX-FileCopyrightText: 2024 Ted Dunning

# SPDX-License-Identifier: Apache-2.0

# Demonstrates how the SI5351 clock generator can generate signals in quadrature
# Two signals are generated on clocks 1 and 3 that are at 30MHz but which are 90%
# out of phase
from machine import I2C
from SI5351 import SI5351

i2c = I2C(1, sda=machine.Pin(2), scl=machine.Pin(3), freq=40000)

si5351 = SI5351(i2c, address=0x60)

si5351.pll_a.configure_integer(30)  # Multiply 25MHz by 30
si5351.clock_0.configure_integer(si5351.pll_a, 25) # and divide by 25 to get 30MHz

si5351.clock_2.configure_integer(si5351.pll_a, 25) # same frequency
si5351.clock_2.phase_delay(1.0)

si5351.outputs_enabled = True


