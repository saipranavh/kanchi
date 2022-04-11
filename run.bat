pytest -v -s -m "sanity and regression" --html=./Reports/report.html testCases/ --browser chrome
pytest -v -s -m "sanity " --html=./Reports/report.html testCases/ --browser edge