# LocalAPIKeys
This package provides the class LAKReader.

## Motivation
This is not necessarily better than using a .env file with load_dotenv().
This began when wondering how I could keep my API keys in one common location, keeping them out of the code, prevent loading them into the environment, and have a way to remove them from memory when done using them.
This was just an experiment.

## LAKReader
LAKReader is a simple way to provide access to API keys without exposing the
API keys in source code.
API keys are assumed to be stored in a private secure file.
LAKReader will read the file and store the keys and associated name in a dictionary.
Users of LAKReader can then request an API key by name.

Please note that this is not intended to be a secure method of preventing users
from descovering API keys.  The intent is to allow a simple way of accessing
my locally stored API keys without putting them directly in source code.

