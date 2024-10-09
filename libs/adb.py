#!/usr/bin/env python
# coding=utf-8

"""ADB"""

import subprocess
    
    
class adbKit(object):
        
    def screenshots(self, serialNumber=None):
        self.command(' exec-out screencap -p > ./screencap.png', serialNumber)



    def command(self, cmd, serialNumber=None):
        cmdstr = 'adb '
        if serialNumber:
            cmdstr = cmdstr + '-s ' + serialNumber + ' '
        cmdstr += cmd

        try:
            result = subprocess.run(cmdstr, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return [result.returncode, result.stdout]
        except subprocess.CalledProcessError as e:
            return [e.returncode, e.stderr]
        
    def click(self, point, serialNumber=None):
        return self.command('shell input tap '+str(point[0])+' '+str(point[1]), serialNumber)
    
    def swip(self, a,b,speed, serialNumber=None):
        return self.command(f'shell input swipe {a[0]} {a[1]} {b[0]} {b[1]} {speed}')
    
