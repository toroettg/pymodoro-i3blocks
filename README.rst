#####
About
#####

The tool pymodoro-i3blocks lets you easily manage your `Pymodoro`_
sessions from within your status bar via `i3blocks`_.

pymodoro-i3blocks is licensed under the Apache License version 2.0.

#####################
Get pymodoro-i3blocks
#####################

Released snapshots of the software are available for `Download`_ from
GitHub, and are also distributed through the `Python Package Index`_.

As free software, you can get a copy of the `Source Code`_ as well if you prefer.

############
Installation
############

To fetch the source files, build, and install it on your machine,
the usage of `pip`_ is recommended:

.. code-block:: bash

    pip install pymodoro-i3blocks --process-dependency-links

==========
Arch Linux
==========

A pymodoro-i3blocks `Package`_ can be found in the `Arch User Repository (AUR)`_.
The `AUR Helper`_ `Yaourt`_ provides an easy way to install the application
from the package:

.. code-block:: bash

    yaourt -S pymodoro-i3blocks


#############
Configuration
#############

To get the application up and running, only few settings are required.
The following instructions assume, that you have installed and properly
configured `i3blocks`_ as well as `Pymodoro`_.

#.  Add Pymodoro as a blocklet to i3blocks, which displays
    the progress of your Pymodoro session. When no session is active,
    the blocklet will be hidden. An example is given below.

    .. code-block:: bash

        [pymodoro]
        command=/usr/bin/pymodoro-i3blocks --daemon
        interval=persist
        format=json

#.  Add another blocklet that allows you to control your Pymodoro
    sessions. The instance property of the blocklet should match with
    the one of your Pymodoro configuration.

    .. code-block:: bash

        [pymodoro-control]
        command=/usr/bin/pymodoro-i3blocks
        instance=/run/user/1000/pymodoro_session
        interval=once
        format=json

#.  Optionally modify the examples above, to match them to your
    preferred style. The usual i3blocks `properties`_ apply.

    Please note that some of them may be overridden by pymodoro-i3blocks,
    e.g., the color of the session blocklet. At this time,
    this behavior cannot be changed without altering the program code.
    Feel free to request additional configuration options when needed.

#.  Restart i3blocks. You should see the control blocklet afterwards.

##############
Blocklet Usage
##############

Click with your left mouse button on the pymodoro-control blocklet to
start a new Pymodoro session. A right click ends the session.


################
Help and Support
################

If you have found a problem with the software, please check the `Issue Tracker`_
and file a report. Feedback and contributions are appreciated as well.

#######
Contact
#######

You can contact me by email at dev@roettger-it.de.

.. _Pymodoro: https://github.com/dattanchu/pymodoro
.. _i3blocks: https://github.com/vivien/i3blocks
.. _properties: https://vivien.github.io/i3blocks/#BLOCK
.. _Source Code: https://github.com/toroettg/pymodoro-i3blocks
.. _Issue Tracker: https://github.com/toroettg/pymodoro-i3blocks/issues
.. _Download: https://github.com/toroettg/pymodoro-i3blocks/releases

.. _Python Package Index: https://pypi.python.org/pypi/pymodoro-i3blocks
.. _pip: https://pip.pypa.io

.. _Arch User Repository (AUR): https://wiki.archlinux.org/index.php/AUR
.. _AUR Helper: https://wiki.archlinux.org/index.php/AUR_helper
.. _Yaourt: https://wiki.archlinux.org/index.php/Yaourt
.. _Package: https://aur.archlinux.org/packages/pymodoro-i3blocks

.. |nbsp| unicode:: 0xA0
   :trim:

