# Knowing where are the sites physical paths

There are two ways: *Guesser* and *host variable*.
The *Guesser* must be the primary way to detect the physical paths. And the *host variable* must be the fallback, in case if Guesser failure.

## First way: Guesser

Think as an object solelly responsible to *guess* where the are the physical paths.

The Guesser intent is to facilitate the users work. No matter how its own system is configured, the Guesser shall find the the physycal paths.

There are a folder just to holds the Guessers, which actually are two: **Posix_Guesser.py** and **Windows_Guesser** . As you can wonders, *Windows Guesser* is responsible just to guess the paths for Windows Hosts, while the *Posix_Guesser* is responsible for posix based systems, like Linux and Mac OS.

## Second way: system variable WWW_HOME

Guess the physical paths for any kind of system is a rather ambitious task just to facilitate the usage. It can be rather complicated and high level of failures are expected.

So, an alternative way is provided: a host variable called WWW_HOME. In this situation, the user must set a host variable called WWW_HOST that must be a real system path that will holds all the sites home paths.
