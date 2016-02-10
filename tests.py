import unittest
from rolling import comeoutroll
from rolling import pointroll

gamesettings = {
"starting": 100,
"pass": 5,
"dontpass": 0,
"passodds": 10,
"dontpassodds": 0
}

class TestCrapsSim(unittest.TestCase):
  def testStartRollBankrupt(self):
    result = comeoutroll(gamesettings)
    self.assertEqual(result, result)

  def testPointRoll(self):
    result = pointroll(4, gamesettings)
    self.assertEqual(result, result)

  def testStartRollBankrupts(self):
    result = comeoutroll(gamesettings)
    self.assertEqual(result, result)

if __name__ == '__main__':
      unittest.main()
