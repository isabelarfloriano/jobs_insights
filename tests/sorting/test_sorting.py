import pytest
from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {
            "title": "Job A",
            "min_salary": 3000,
            "max_salary": 5000,
            "date_posted": "2022-01-01",
        },
        {
            "title": "Job B",
            "min_salary": 2000,
            "max_salary": None,
            "date_posted": "2022-01-02",
        },
        {
            "title": "Job C",
            "min_salary": 4000,
            "max_salary": 7000,
            "date_posted": None,
        },
        {
            "title": "Job D",
            "min_salary": None,
            "max_salary": 6000,
            "date_posted": "2022-01-04",
        },
    ]

    with pytest.raises(ValueError):
        sort_by(jobs, "invalid_criteria")

    sort_by(jobs, "min_salary")
    assert [j["title"] for j in jobs] == ["Job B", "Job A", "Job C", "Job D"]
    assert jobs[-2:] == [
        {
            "title": "Job C",
            "min_salary": 4000,
            "max_salary": 7000,
            "date_posted": None,
        },
        {
            "title": "Job D",
            "min_salary": None,
            "max_salary": 6000,
            "date_posted": "2022-01-04",
        },
    ]

    sort_by(jobs, "max_salary")
    assert [j["title"] for j in jobs] == ["Job C", "Job D", "Job A", "Job B"]
    assert jobs[-2:] == [
        {
            "title": "Job A",
            "min_salary": 3000,
            "max_salary": 5000,
            "date_posted": "2022-01-01",
        },
        {
            "title": "Job B",
            "min_salary": 2000,
            "max_salary": None,
            "date_posted": "2022-01-02",
        },
    ]

    sort_by(jobs, "date_posted")
    assert [j["title"] for j in jobs] == ["Job D", "Job C", "Job B", "Job A"]
    assert jobs[-2:] == [
        {
            "title": "Job B",
            "min_salary": 2000,
            "max_salary": None,
            "date_posted": "2022-01-02",
        },
        {
            "title": "Job A",
            "min_salary": 3000,
            "max_salary": 5000,
            "date_posted": "2022-01-01",
        },
    ]
