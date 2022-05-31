# Pronounce

Pronounce is a simple, configurable and easily accessible pronoun / general info page.

### How does it work?

It's simple!

It reads a url (as defined as `user-url` in `./conf.yml`) as a plaintext YAML file, and replaces the string `{username}` in `user-url` with the url path, e.g. a path of https://pronounce.url/michal would replace `{username}` with michal.

This allows for you to set something public like the github raw file access url as `user-url`, which theoretically makes it infinitely expandable!

If set up right, you can run a single session that grants any user of github a Pronounce page! Isn't that neat

### Surely there are security considerations with this

There probably are! I'm not skilled enough to fix any if they do arise, so be sure to create an Issue, or even better, fork it and create a Merge Request to fix my terrible code for me!

### Dependencies

- flask
- pyyaml
- urllib3

:) That's it!
