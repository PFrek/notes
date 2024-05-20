@echo off
cd %~dp0
pipenv run python src\notes.py %*
