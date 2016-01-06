
import pytest
import math

from subsystems.chassis import Chassis

def test_chassis(wpilib):#, hal_data):
    chassis = Chassis()

    for motor in chassis._motors:
        assert isinstance(motor, wpilib.CANTalon)

    chassis.drive(0.0, 0.0, 0.0, 0.0)

    for motor in chassis._motors:
        assert motor.get() == 0.0

    chassis.drive(1.0, 0.0, 0.0, 0.0)

    for motor in chassis._motors:
        assert motor.get() == 0.0

    chassis.drive(1.0, 0.0, 0.0, 0.5)

    assert chassis._motors[0].get() == 0.5
    assert chassis._motors[1].get() == 0.5
    assert chassis._motors[2].get() == -0.5
    assert chassis._motors[3].get() == -0.5

    chassis.drive(0.0, 0.0, 1.0, 1.0)

    for motor in chassis._motors:
        assert motor.get() == -1.0
