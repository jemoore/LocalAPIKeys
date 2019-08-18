
class LAKReader:
    """
    Reads a text file expected to contain key/value pairs representing Names
    and API keys of services. Users can then use this class to query for
    API keys by name.

    Unless specified otherwise, the default file that is read is:
    ~/.safe/api-keys.txt
    The expectation is that each name and API key will be on one line separated
    by whitespace.  Any line that starts with a '#' is considered a comment
    and will be ignored. Also any line containing all whitespace is ignored.
    e.g.
    # Start of file

    some-service  1234567890
    another-service 9876543210

    # End of file
    """
    def __init__(self):
        self.lakDict = {}

    def read(self, api_key_file = '/home/jeff/.safe/api-keys.txt'):
        """ Opens api_key_file and stores name/key pairs internally
        for later retrival."""

        api_key_file = api_key_file.strip()
        if len(api_key_file) == 0:
            return

        with open(api_key_file) as fp:
            line = fp.readline()
            while line:
                line = line.strip()
                if len(line) > 0:
                    if line[0] != '#':
                        name_key = line.split()
                        if len(name_key) == 2:
                            self.lakDict[name_key[0]] = name_key[1]
                line = fp.readline()

    def getAPIKey(self, service):
        """Query internal storage for an API key associated to service."""
        if len(self.lakDict) == 0:
            return ""

        service = service.strip()
        if len(service) == 0:
            return ""

        if service in self.lakDict.keys():
            return self.lakDict[service]

        return ""

    def clear(self):
        """Removes all name/API key values stored by this object."""
        self.lakDict = {}


