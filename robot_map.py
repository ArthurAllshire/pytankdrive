from wpilib import CANTalon

class RobotMap:
    """
    The RobotMap is a mapping from the ports sensors and actuators are wired into
    to a variable name. This provides flexibility changing wiring, makes checking
    the wiring easier and significantly reduces the number of magic numbers
    floating around.
    """

    # For example to map the left and right motors, you could define the
    # following variables to use with your drivetrain subsystem.
    # left_motor = 1
    # right_motor = 2
    motor_a_talon_id = 4
    motor_b_talon_id = 7
    motor_c_talon_id = 1
    motor_d_talon_id = 3

    gamepad_port = 1
    joystick_port = 0

    gamepad_left_stick_x = 0
    gamepad_left_stick_y = 1
    gamepad_left_stick_x = 4
    gamepad_left_stick_y = 5

    drive_motor_mode = CANTalon.ControlMode.PercentVbus

    deadzone = 0.05
    pass
