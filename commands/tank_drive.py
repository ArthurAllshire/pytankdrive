from wpilib.command import Command, CommandGroup

class TankDrive(Command):

    def __init__(self, robot, name=None, timeout=None):
        """This is the constructor of the command, use this to declare subsystem dependencies"""
        #Use self.requires() here to declare subsystem dependencies
        #eg. self.requires(chassis)
        super().__init__(name, timeout)
        self.robot = robot
        #self.robot.chassis = robot.chassis
        self.requires(self.robot.chassis)

    def initialize(self):
        """Called just before this Command runs the first time"""
        self.robot.chassis.drive(0.0, 0.0, 0.0, 0.0) # just to be safe

    def execute(self):
        """Called repeatedly when this Command is scheduled to run"""
        self.robot.chassis.drive(
                self.robot.rescale_js(-self.robot.oi.getJoystickY(), deadzone=0.05),
                0.0,
                self.robot.rescale_js(self.robot.oi.getJoystickZ(), deadzone=0.2, exponential=0.3),
                1.0
                )

    def isFinished(self):
        """This should return true when this command no longer needs to run execute()"""
        return False

    def end(self):
        """Called once after isFinished returns true"""
        self.robot.chassis.drive(0.0, 0.0, 0.0, 0.0)

    def interrupted(self):
        """Called when another command which requires one or more of the same example_subsystem is scheduled to run"""
        self.end()
