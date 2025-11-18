from src.main import flatten_list


class TestFlattenList:
    def test_no_nest(self):
        test_val = [1, 2, 3]
        assert flatten_list(test_val) == [1, 2, 3]

    def test_double_nest(self):
        test_val = [1, [2, 3], [4, [5]]]
        assert flatten_list(test_val) == [1, 2, 3, 4, 5]

    def test_empty(self):
        test_val = []
        assert flatten_list(test_val) == []

    def test_single_triple_nest(self):
        test_val = [[[1]]]
        assert flatten_list(test_val) == [1]

    def test_no_idea_how_to_call_it(self):
        test_val = [[[1]]]
        assert flatten_list(test_val) == [1]
