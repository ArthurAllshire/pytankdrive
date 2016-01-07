#!/usr/bin/env python3

import wpilib
from wpilib import command

#from subsystems.example_subsystem import ExampleSubsystem
from subsystems import Chassis
#from commands.example_command import ExampleCommand
from oi import OI

import logging

class TankDriveRobot(wpilib.IterativeRobot):

    #example_subsystem = ExampleSubsystem()

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.oi = OI(self)
        self.chassis = Chassis(self)
        self.logger = logging.getLogger("robotpy")
        #Create the command used for the autonomous period
        #self.autonomous_command = ExampleCommand(self)

    def disabledInit(self):
        pass

    def disabledPeriodic(self):
        """This function is called periodically when disabled."""
        command.Scheduler.getInstance().run()

    def autonomousInit(self):
        #Schedule the autonomous command
        #self.autonomous_command.start()
        pass

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        command.Scheduler.getInstance().run()

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        command.Scheduler.getInstance().run()

    def testPeriodic(self):
        """This function is called periodically during test mode."""
        wpilib.LiveWindow.run()

if __name__ == "__main__":
    wpilib.run(TankDriveRobot)
