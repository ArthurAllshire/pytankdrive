#!/usr/bin/env python3

import math

import wpilib
from wpilib import command

#from subsystems.example_subsystem import ExampleSubsystem
from subsystems import Chassis
from subsystems import Intake
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
        self.chassis = Chassis(self)
        self.intake = Intake(self)
        self.oi = OI(self)
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

    def rescale_js(self, value, deadzone=0.0, exponential=0.0, rate=1.0):
        value_negative = 1.0
        if value < 0:
            value_negative = -1.0
            value = -value
        # Cap to be +/-1
        if abs(value) > 1.0:
            value /= abs(value)
        # Apply deadzone
        if abs(value) < deadzone:
            return 0.0
        elif exponential == 0.0:
            value = (value-deadzone)/(1-deadzone)
        else:
            a = math.log(exponential+1)/(1-deadzone)
            value = (math.exp(a*(value - deadzone))-1)/exponential
        return value*value_negative*rate

if __name__ == "__main__":
    wpilib.run(TankDriveRobot)
