import unittest
import time
import SonyCP

# Test the lens position of the Sony Projector
#
# You will notice that we have a sleep function in here. This is because the
# projector needs time to warm up / cool off

class ProjectorLensPosition(unittest.TestCase):

    curr_pic_pos = "1.85.1"
    
    def setUp(self):
        self.projector = SonyCP.Projector("192.168.102.74")

    # Get the picture (lens) position

    def test_1_lens_pos(self):
        self.__class__.curr_pic_pos = self.projector.get_picture_position()

        # What is the picture (lens) position. Do the opposite and
        # then make sure the lens moved

        if self.__class__.curr_pic_pos == "1.85.1":
            new_pic_pos = "2.35.1"
        else:
            new_pic_pos = "1.85.1"

        self.projector.set_picture_position(new_pic_pos)
        time.sleep(15)

        # Now get the picture (lens) position and make sure it
        # moved

        self.__class__.curr_pic_pos = self.projector.get_picture_position()
        self.assertTrue(new_pic_pos == self.__class__.curr_pic_pos)

    # Move the lens to the opposite position (if 1.85.1, then move to 2.35.1 or vice-versa)
    
    def test_2_lens_pos(self):

        # What is the picture (lens) position. Do the opposite and
        # then make sure the lens moved

        if self.__class__.curr_pic_pos == "1.85.1":
            new_pic_pos = "2.35.1"
        else:
            new_pic_pos = "1.85.1"

        self.projector.set_picture_position(new_pic_pos)
        time.sleep(15)

        # Now get the picture (lens) position and make sure it
        # moved

        pic_pos = self.projector.get_picture_position()
        self.assertTrue(new_pic_pos == pic_pos)

    # Turn off the projector
    
    def test_3_powered_off(self):
        self.projector.set_power(False)
        time.sleep(10)
        self.assertFalse(self.projector.get_power())

    # Getting the picture (lens) position while it is powered off should throw an exception
    
    def test_4_lens_pos_powered_off(self):
        with self.assertRaises(Exception) as context:
            self.projector.get_picture_position()

        self.assertTrue("Received failed" in str(context.exception)[0:15])

    def tearDown(self):
        del self.projector
