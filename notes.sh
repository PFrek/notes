PROJECT_PATH="$(dirname "$0")"
cd $PROJECT_PATH
pipenv run python src/notes.py "$@"
