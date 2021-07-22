@REM Save the commands for running line profiler
@REM Have the profile decorator in prof.py file

kernprof -l prof.py
python -m line_profiler prof.py.lprof 