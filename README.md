# Gather Content API Tools

## Purpose:
Allow users to quickly run api calls to and from GatherContent. There are few options on exporting. So the aim is to be able to export data in multiple formats.

### Current Goals:
- [x] Begin project! 
- [ ] Build core api calls already supported by GatherContent



### Requirements
* `Python Version: 3.9+`

* `certifi==2022.6.15`

* `charset-normalizer==2.1.1`

* `coverage==6.4.4`

* `idna==3.3`

* `requests==2.28.1`

* `urllib3==1.26.12`

You can install these packages by running:
`pip install -r requirements.txt`

### Configuration
You must create the following files:
* `credentials.py` under `private/`. This will ensure that the program can grab your unique information. **Keep this out of public files**.

Additionally, there's a default `config.py` under `includes/`. This is also used by the program by default, but feel free to override by using the appropriate methods such as:
`set_mime(YOUR_CUSTOM_STUFF_HERE)`.


### Testing
under `tests/` there is unit testing that will be updated as the project grows.
coverage tests will always be aimed at >80%. 

