httpie-gssapi
=============

GSSAPI authentication plug-in for `HTTPie <https://httpie.org/>`_.

This plug-in uses the `requests-gssapi <https://github.com/pythongssapi/requests-gssapi>`_
library, which is a more-modern replacement of the old `requests-kerberos <https://github
.com/requests/requests-kerberos>`_ library.


Installation
------------

.. code-block:: bash

    $ pip install httpie-gssapi

This will add the ``gssapi`` authentication method under ``--auth-type`` in the ``$ http --help``
output.


Usage
-----

Ensure you have a valid Kerberos token by running ``kinit``.

.. code-block:: bash

    $ http --auth-type=gssapi https://example.org

Note that supplying authentication credentials is not necessary, meaning the following two
commands are equivalent:

.. code-block:: bash

    $ http --auth-type=gssapi https://example.org
    $ http --auth-type=gssapi --auth : https://example.org


Configuration Options
---------------------

The following environment variables can be set to modify the GSSAPI authentication behavior:

* ``HTTPIE_GSSAPI_MUTUAL_AUTH`` (default: ``required``): determines whether mutual authentication
  from the server should be required. For more information, see `Mutual Authentication
  <https://github.com/pythongssapi/requests-gssapi#mutual-authentication>`_. Possible values are:
  ``required``, ``optional``, ``disabled``.

* ``HTTPIE_GSSAPI_OPPORTUNISTIC_AUTH`` (default: ``no``): enables or disables preemptively
  initiating the GSSAPI exchange. For more information, see `Opportunistic Authentication
  <https://github.com/pythongssapi/requests-gssapi#opportunistic-authentication>`_. Possible
  values are: ``yes``, ``true``, ``1``; all other values default to ``no``.

* ``HTTPIE_GSSAPI_DELEGATE`` (default: ``no``): enables or disables credential delegation. For
  more information, see `Delegation <https://github.com/pythongssapi/requests-gssapi#delegation>`_.
  Possible values are: ``yes``, ``true``, ``1``; all other values default to ``no``.
