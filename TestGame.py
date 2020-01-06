#unit tests

from unittest import main, TestCase
from io import StringIO

from Game import disp, solve


class TestGame(TestCase):

	#disp

	def test_disp_1(self):
		w=StringIO()
		board=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
		ans='[0, 0, 0]\n[0, 0, 0]\n[0, 0, 0]\n'
		run=disp(w, board)
		self.assertEqual(ans, w.getvalue())


if __name__=='__main__':
	main()