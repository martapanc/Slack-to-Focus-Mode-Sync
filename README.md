# Sync Slack status with Focus Mode on MacOS

## Set up
- Create "Focus Mode ON" and "Focus Mode OFF" scripts using Apple Shortcuts
- Create new Slack App using the "Event Subscriptions" functionality
- [Ngrok](https://ngrok.com/) can be used to expose the local server to the internet: the url that gets generated can be used as Request URL (e.g. https://xx-xx-xx.ngrok.io/)
- Create a simple POST endpoint using FastAPI (or Flask, etc.)
  - The first time only, Slack will send a request with a Body containing a 'challenge' parameter. The endpoint needs to return the challenge value so that the URL can be verified (https://api.slack.com/events/url_verification).
- Add User Token Scopes: `users:read` [Scopes that access user data and act on behalf of users that authorize them.]
