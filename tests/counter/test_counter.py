from src.pre_built.counter import count_ocurrences


def test_counter():
    jobs_path = "data/jobs.csv"
    mock_word = "SalArY"
    result = count_ocurrences(jobs_path, mock_word)
    assert result == 598
