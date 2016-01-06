#
# See the notes for the other physics sample
#


from pyfrc.physics import drivetrains

from robot_map import RobotMap


class PhysicsEngine(object):
    '''
       Simulates a 4-wheel robot using Tank Drive joystick control
    '''


    def __init__(self, physics_controller):
        '''
            :param physics_controller: `pyfrc.physics.core.Physics` object
                                       to communicate simulation effects to
        '''

        self.physics_controller = physics_controller
        self.physics_controller.add_gyro_channel(1)

    def update_sim(self, hal_data, now, tm_diff):
        '''
            Called when the simulation parameters for the program need to be
            updated.

            :param now: The current time as a float
            :param tm_diff: The amount of time that has passed since the last
                            time that this function was called
        '''

        # Simulate the drivetrain
        motor_a = hal_data['pwm'][RobotMap.motor_a_talon_id]['value']#['CAN'][RobotMap.motor_a_talon_id]['value']
        motor_b = hal_data['pwm'][RobotMap.motor_b_talon_id]['value']#['CAN'][RobotMap.motor_b_talon_id]['value']
        motor_c = hal_data['pwm'][RobotMap.motor_c_talon_id]['value']#['CAN'][RobotMap.motor_c_talon_id]['value']
        motor_d = hal_data['pwm'][RobotMap.motor_c_talon_id]['value']#['CAN'][RobotMap.motor_d_talon_id]['value']


        speed, rotation = drivetrains.four_motor_drivetrain(motor_b, motor_c, motor_a, motor_d)#lr_motor, rr_motor, lf_motor, rf_motor)
        self.physics_controller.drive(speed, rotation, tm_diff)
