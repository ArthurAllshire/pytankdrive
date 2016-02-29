
from wpilib.command import Command, CommandGroup

class ToggleIntake(Command):

    def __init__(self, robot, name=None, timeout=None):
        """This is the constructor of the command, use this to declare subsystem dependencies"""
        #Use self.requires() here to declare subsystem dependencies
        #eg. self.requires(chassis)
        super().__init__(name, timeout)
        self.robot = robot
        #self.robot.chassis = robot.chassis
        self.requires(self.robot.intake)

    def initialize(self):
        """Called just before this Command runs the first time"""
        pass

    def execute(self):
        """Called repeatedly when this Command is scheduled to run"""
        self.robot.intake.toggle()

    def isFinished(self):
        """This should return true when this command no longer needs to run execute()"""
        return True

    def end(self):
        """Called once after isFinished returns true"""
        pass

    def interrupted(self):
        """Called when another command which requires one or more of the same example_subsystem is scheduled to run"""
        self.end()