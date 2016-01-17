#!/usr/bin/env python
# Copyright (c) 2016 CNRS
# Author: Joseph Mirabel
#
# This file is part of hpp-baxter.
# hpp-baxter is free software: you can redistribute it
# and/or modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation, either version
# 3 of the License, or (at your option) any later version.
#
# hpp-baxter is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Lesser Public License for more details.  You should have
# received a copy of the GNU Lesser General Public License along with
# hpp-baxter.  If not, see
# <http://www.gnu.org/licenses/>.

from hpp.corbaserver.robot import Robot as Parent

##
#  Control of robot Baxter in hpp
#
#  This class implements a client to the corba server implemented in
#  hpp-corbaserver. It derive from class hpp.corbaserver.robot.Robot.
#
#  At creation of an instance, the urdf and srdf files are loaded using
#  idl interface hpp::corbaserver::Robot::loadRobotModel.
class Robot (Parent):
    ##
    #  Information to retrieve urdf and srdf files.
    packageName = "hpp-baxter"
    meshPackageName = "baxter_description"
    rootJointType = "anchor"
    ##
    #  Information to retrieve urdf and srdf files.
    urdfName = "baxter"
    urdfSuffix = "_colman"
    srdfSuffix = ""

    def __init__ (self, robotName, load = True):
        Parent.__init__ (self, robotName, self.rootJointType, load)
        self.tf_root = "base_footprint"