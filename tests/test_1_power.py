import unittest
import time
import SonyCP

# Test the power on / status of the Sony Projector
#
# You will notice that we have a sleep function in here. This is because the
# projector needs time to warm up / cool off
#
# In order to minimize the stress on the projector, we will not test
# power off in this suite of tests. We will put the power off testing
# in another suite so that we can test lens position, etc.

class ProjectorPower(unittest.TestCase):
    def setUp(self):
        self.projector = SonyCP.Projector("192.168.102.74")

    def test_1_powered_off(self):
        self.assertFalse(self.projector.get_power())

    def test_2_power_on(self):
        self.projector.set_power(True)
        time.sleep(60)
        self.assertTrue(self.projector.get_power())

    def tearDown(self):
        del self.projector
