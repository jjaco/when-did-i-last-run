# when-did-i-last-run

`when-did-i-last-run` is a daft script which will calculate how long ago you last logged an activity in Strava via its API. Feel free to use this for motivation, bragging rights, self-immolation. 

My personal use case is to invoke this as part of my `.zprofile`, so it provides a value for each new `zsh` prompt. To prevent ludicrous amounts of API calls being made (which would slow down the terminal even more than it already does), the script uses the excellent `requests_cache` to create a local `sqlite`-based cache of the results (default timeout is 3 hours).

## Requirements
* Environment variable `STRAVA_ACCESS_TOKEN` which can be retrieved for your Strava account from the [developer's portal](http://labs.strava.com/developers/).
* Python (2.7+) environment with `requests_cache`, `pandas` (stress-free date arthimetic)

