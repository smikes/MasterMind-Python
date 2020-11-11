import unittest
import mastermind

class TestStringMethods(unittest.TestCase):

    def test_nothing(self):
        self.assertEqual(1,1)

    def test_generate(self):
        example = mastermind.generate_num([0,0,0])
        self.assertEqual(len(example), 3)

    def test_analyze(self):
        """
Test Evaluations (Answer is 123):

  Guess		Evaluation			          Attempts
  134		  green, yellow			        1 		//notice no red
  213		  green, yellow, yellow	    2			//notice the green is first, always
  312		  yellow, yellow, yellow		3
  143		  green, green			        4
  300		  yellow				            5
  555		  red				                6			//red will only appear here
  114		  green				              7			//notice that there is no yellow for the second 1
  123 		green,green,green		      7     //correct answer
        
        """
        self.assertEqual( mastermind.analyze_guess([1,2,3], [1,3,4]), "green, yellow")
        self.assertEqual( mastermind.analyze_guess([1,2,3], [2,1,3]), "green, yellow, yellow")
        self.assertEqual( mastermind.analyze_guess([1,2,3], [3,0,0]), "yellow")

        self.assertEqual( mastermind.analyze_guess([2,4,2], [2,1,3]), "green")

        self.assertEqual( mastermind.analyze_guess([2,4,2], [4,4,3]), "green")

        # this is a bug
        self.assertEqual( mastermind.analyze_guess([2,4,2], [2,2,0]), "green, yellow")
        


if __name__ == '__main__':
    unittest.main()
