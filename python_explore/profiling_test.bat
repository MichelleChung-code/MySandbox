@REM Save the commands for running line_profiler
@REM Have the profile decorator in prof.py file

kernprof -l prof.py
python -m line_profiler prof.py.lprof 

@REM For using memory_profiler (prof.py also needs to have the profile decorator here)
python -m memory_profiler prof.py