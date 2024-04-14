class EosRequest:
    endpoint = None
    headers = None
    payload = None
    user = None
    password = None

    def __init__(self, config, headers, payload):
        if config is not None:
            self.endpoint = config['DEFAULT']['EOS_COMMAND_API_ENDPOINT']
            self.user = config['DEFAULT']['EOS_COMMAND_API_USER']
            self.password = config['DEFAULT']['EOS_COMMAND_API_PASSWORD']
        if headers is None:
            self.headers = {'Content-Type': 'application/json'}
        if payload is None:
            self.payload = {"jsonrpc": "2.0", "method": "runCmds", "id": "1"}

    def update_cmd_params(self, cmds):
        self.payload["params"] = cmds
