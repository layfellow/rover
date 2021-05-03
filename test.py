import unittest
from rover import MarsRover

class TestMarsRover(unittest.TestCase):

	def assert_coordinates(self, rover, x, y, heading):
		self.assertEqual(rover.x, x)
		self.assertEqual(rover.y, y)
		self.assertEqual(rover.heading, heading)

	def test_full_rotation(self):
		spirit = MarsRover(2, 3, 'S', 5, 5)
		spirit.right().right().right().right().left().left().left().left()
		self.assert_coordinates(spirit, 2, 3, 'S')

	def test_trips(self):
		curiosity = MarsRover(1, 2, 'N', 5, 5)
		perseverance = MarsRover(3, 3, 'E', 5, 5)

		curiosity.left().move().left().move().left().move().left().move().move()
		self.assert_coordinates(curiosity, 1, 3, 'N')

		perseverance.move([curiosity]).move([curiosity]).right()
		perseverance.move([curiosity]).move([curiosity]).right()
		perseverance.move([curiosity]).right().right().move([curiosity])
		self.assert_coordinates(perseverance, 5, 1, 'E')

	def test_do_not_fall_off_cliff(self):
		zhurong = MarsRover(2, 2, 'W', 5, 5)
		zhurong.move().move().move()
		self.assert_coordinates(zhurong, 0, 2, 'W')

	def test_do_not_crash(self):
		perseverance = MarsRover(5, 3, 'S', 5, 5)
		zhurong = MarsRover(5, 1, 'N', 5, 5)

		perseverance.move([zhurong]).move([zhurong])
		self.assert_coordinates(perseverance, 5, 2, 'S')
