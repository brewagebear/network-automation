# FastAPI for Arista EOS Commands
## Project Description
This project uses FastAPI to interface with the Arista EOS Command API, allowing users to manage network configurations without directly executing CLI commands. It provides a RESTful API to execute and retrieve command outputs securely and efficiently.

## Why FastAPI?
FastAPI provides an asynchronous framework that is ideal for I/O-bound tasks like API calls, with automatic interactive API documentation using Swagger.

## Getting Started
### Prerequisites
+ [Arista cEOS](https://containerlab.dev/manual/kinds/ceos/) or On-premise Arista Command API 
+ Python 3.8+

### Installation
#### With containerLab
I built a testing environment by referring to [building-containerlab-with-ceos](https://github.com/arista-netdevops-community/building-containerlab-with-ceos).

NOTE : **This will be done on the assumption that the cEOS image has been built into the working environment.**

To install the necessary Arista Topology, run:
```bash 
git clone https://github.com/arista-netdevops-community/building-containerlab-with-ceos.git \ 
&& cd building-containerlab-with-ceos/

sudo containerlab deploy --debug --topo default_cfg.clab.yml
```

Change the settings to the actual environment value and add config.ini.
```
; config.ini
[DEFAULT]
EOS_COMMAND_API_ENDPOINT = https://arista-command-api-host:443/command-api
EOS_COMMAND_API_USER = user
EOS_COMMAND_API_PASSWORD = user
```

To install the necessary dependencies, run:
```bash
pip install -r requirements.txt
```

#### With containerLab
### Running the Application 

```bash
uvicorn main:app --reload  # The app will reload itself on file changes
```

### API Endpoints
+ `GET /api/v1/commands/?command={query}`

#### Example 

+ `GET /api/v1/commands/?command=enable, show ip routes`

#### Result

```json
{
  "jsonrpc": "2.0",
  "id": "1",
  "result": [
    {},
    {
      "vrfs": {
        "default": {
          "routingDisabled": true,
          "allRoutesProgrammedHardware": true,
          "allRoutesProgrammedKernel": true,
          "defaultRouteState": "reachable",
          "routes": {
            "0.0.0.0/0": {
              "hardwareProgrammed": true,
              "routeType": "static",
              "routeLeaked": false,
              "kernelProgrammed": true,
              "preference": 1,
              "metric": 0,
              "routeAction": "forward",
              "directlyConnected": false,
              "vias": [
                {
                  "nexthopAddr": "192.168.123.1",
                  "interface": "Management0"
                }
              ]
            },
            "192.168.123.0/24": {
              "hardwareProgrammed": true,
              "routeType": "connected",
              "routeLeaked": false,
              "kernelProgrammed": true,
              "routeAction": "forward",
              "vias": [
                {
                  "interface": "Management0"
                }
              ],
              "directlyConnected": true
            }
          }
        }
      }
    }
  ]
}
```

