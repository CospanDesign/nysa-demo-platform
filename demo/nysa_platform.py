#Distributed under the MIT licesnse.
#Copyright (c) 2014 Dave McCoy (dave.mccoy@cospandesign.com)

#Permission is hereby granted, free of charge, to any person obtaining a copy of
#this software and associated documentation files (the "Software"), to deal in
#the Software without restriction, including without limitation the rights to
#use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
#of the Software, and to permit persons to whom the Software is furnished to do
#so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

"""
Demo Interface
"""
__author__ = 'dave.mccoy@cospandesign.com (Dave McCoy)'

import sys
import os
import glob
import json
import hashlib


from nysa.host.nysa_platform import Platform
from nysa.ibuilder.lib.xilinx_utils import find_xilinx_path
from demo import Demo


class DemoPlatform(Platform):
    def __init__(self, status = None):
        super (DemoPlatform, self).__init__(status)

    def get_type(self):
        if self.status: self.status.Verbose("Returnig 'demo' type")
        return "demo"

    def scan(self):
        """
        Nysa will call this function when the user wants to scan for the
        platform specific boards

        Args:
            Nothing


        Returns:
            Dictionary of demo instances, where the key is the serial number
            or unique identifier of a board

        Raises:
            NysaError: An error occured when scanning for devices

        """
        inst_dict = {}
        if self.status: self.status.Warning("Scan function not implemented yet!")
        return inst_dict
        #raise AssertionError("%s not implemented" % sys._getframe().f_code.co_name)

    def test_build_tools(self):
        """
        Runs a test to determine if the Vendor specific build tools are present

        Args:
            Nothing

        Returns:
            Boolean:
                True: Build tools found
                False: Build tools not found

        Raises:
            NysaError: An error occured when scanning for the build tools
        """
        #raise AssertionError("%s not implemented" % sys._getframe().f_code.co_name)
        if self.status:  self.status.Warning("By default build tools is Xilinx this can be changed in demo/nysa_platform.py")
        if find_xilinx_path() is None:
            return False
        return True

    def setup_platform(self):
        """
        Run this to configure the system to recognize your platform, such as:
            -installing drivers
            -assigning PCIE express ports
            -etc

        Args:
            Nothing

        Return:
            Nothing

        Raises:
            Nothing
        """
        if self.status: self.status.Warning("Setup Function Not Implemented Yet!")

    def uninstall_platform(self):
        """
        Run this to uninstall your platform from the system

        Args:
            Nothing

        Return:
            Nothing

        Raises:
            Nothing
        """
        if self.status: self.status.Warning("Uninstall Function Not Implemented Yet!")

