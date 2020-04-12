# add_vhost_4

Automatically adds a virtual host for local development machine.

1. Writes in the `hosts` file, whatever the host system.
2. Add a virtual host entry to the host system.
3. Writes basic folders to make the just created virtual host works.
4. Tries to restart the virtualhost server.

Then, a final message will instruct how to test your brand new local virtual host created.

Important observation: by now, in Windows, the applications works only when the folder for wamp have the following path: `C:\wamp64\bin\apache\apache2.4.41`. Other folder configuration will needs changes in the `Windows_Guesser.py` file.

## Usage

```
python3 __main__.py <your_vhost_name>
```
