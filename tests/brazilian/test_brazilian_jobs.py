from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    result_list = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    result_dict_keys = [
        result.keys()
        for result in result_list
        ]
    for dict in result_dict_keys:
        # print(dict == "dict_keys(['title', 'salary', 'type'])")
        assert str(dict) == "dict_keys(['title', 'salary', 'type'])"
