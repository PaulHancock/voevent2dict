.. VOEvent2Dict documentation master file, created by
   sphinx-quickstart on Thu Jan 23 14:25:39 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

VOEvent2Dict documentation
==========================

VOEvents are a standard for representing transient astronomical events in XML.
They are used by many observatories and telescopes to communicate the detection
of transient events. This package provides a simple way to convert these XML
files into Python dictionaries.

There are existing packages that can parse VOEvents, such as `voevent-parse`_
or `xmltodict`_, but the dictionaries they produce are not always easy to work
with. This package aims to solve that problem by providing dictionaries that
are easier to work with.

Long gripe which motivates the need for this package:
-----------------------------------------------------

Here is an example of a VOEvent file:

.. literalinclude:: ../tests/test_events/gcn.classic.voevent.FERMI_POINTDIR.xml
   :language: xml
   :caption: Example VOEvent XML file

When this is parsed by `voevent-parse`_, the resulting structure is not a dict,
but a custom object that requires users to understand how xml files are built.
For example any time there is a Group or Param in the xml file the user has to 
manually navigate the structure to get the data they want. See 
`this tutorial <https://voevent-parse.readthedocs.io/en/stable/tutorial/01-parsing.html#'Sibling'-elements-and-list-style-access>`_

When the above file is parsed by `xmltodict`_, the resulting dictionary looks like this:


.. code-block:: javascript

   {
   'voe:VOEvent': {'@ivorn': 'ivo://nasa.gsfc.gcn/Fermi#Point_Dir_2025-01-22T08:08:00.00_000000-0-581',
   '@role': 'utility',
   '@version': '2.0',
   '@xmlns:voe': 'http://www.ivoa.net/xml/VOEvent/v2.0',
   '@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
   '@xsi:schemaLocation': 'http://www.ivoa.net/xml/VOEvent/v2.0  http://www.ivoa.net/xml/VOEvent/VOEvent-v2.0.xsd',
   'Who': {'AuthorIVORN': 'ivo://nasa.gsfc.tan/gcn',
      'Author': {'shortName': 'Fermi (via VO-GCN)',
      'contactName': 'Julie McEnery',
      'contactPhone': '+1-301-286-1632',
      'contactEmail': 'Julie.E.McEnery@nasa.gov'},
      'Date': '2025-01-22T08:07:45',
      'Description': 'This VOEvent message was created with GCN VOE version: 15.08 17jun22'},
   'What': {'Param': [{'@name': 'Packet_Type', '@value': '129'},
      {'@name': 'Pkt_Ser_Num', '@value': '113'},
      {'@name': 'Start_TJD', '@value': '20697', '@unit': 'days', '@ucd': 'time'},
      {'@name': 'Start_SOD',
      '@value': '29280.00',
      '@unit': 'sec',
      '@ucd': 'time'},
      {'@name': 'Start_RA',
      '@value': '316.2710',
      '@unit': 'deg',
      '@ucd': 'pos.eq.ra'},
      {'@name': 'Start_Dec',
      '@value': '-56.1458',
      '@unit': 'deg',
      '@ucd': 'pos.eq.dec'},
      {'@name': 'Delta_T', '@value': '120', '@unit': 'sec', '@ucd': 'time'},
      {'@name': 'RA_1dt',
      '@value': '323.0',
      '@unit': 'deg',
      '@ucd': 'pos.eq.ra'},
      {'@name': 'Dec_1dt',
      '@value': '-59.4',
      '@unit': 'deg',
      '@ucd': 'pos.eq.dec'},
      ...
      {'@name': 'SAA_29dt', '@value': '0'},
      {'@name': 'Coords_Type', '@value': '2', '@unit': 'dn'},
      {'@name': 'Coords_String', '@value': 'pointing_direction'}],
      'Group': {'@name': 'Obs_Support_Info',
      'Description': 'The Sun and Moon values are valid at the time the VOEvent XML message was created.',
      'Param': [{'@name': 'Sun_RA',
         '@value': '304.83',
         '@unit': 'deg',
         '@ucd': 'pos.eq.ra'},
      {'@name': 'Sun_Dec',
         '@value': '-19.59',
         '@unit': 'deg',
         '@ucd': 'pos.eq.dec'},
      {'@name': 'Sun_Distance',
         '@value': '37.54',
         '@unit': 'deg',
         '@ucd': 'pos.angDistance'},
      {'@name': 'Sun_Hr_Angle', '@value': '-0.79', '@unit': 'hr'},
      ...
      ]},
      'Description': 'The current and soon-to-be pointing directions for the Fermi spacecraft.'},
   'WhereWhen': {'ObsDataLocation': {'ObservatoryLocation': {'@id': 'GEOLUN'},
      'ObservationLocation': {'AstroCoordSystem': {'@id': 'UTC-FK5-GEO'},
      'AstroCoords': {'@coord_system_id': 'UTC-FK5-GEO',
         'Time': {'@unit': 's',
         'TimeInstant': {'ISOTime': '2025-01-22T08:08:00.00'}},
         'Position2D': {'@unit': 'deg',
         'Name1': 'RA',
         'Name2': 'Dec',
         'Value2': {'C1': '316.2710', 'C2': '-56.1458'},
         'Error2Radius': '0.0000'}}}},
      'Description': 'The RA,Dec coordinates are of the type: pointing_direction.'},
   'How': {'Description': 'Fermi Satellite, Spacecraft',
      'Reference': {'@uri': 'http://gcn.gsfc.nasa.gov/fermi.html',
      '@type': 'url'}},
   'Why': {'Inference': {'@probability': '1.00',
      'Concept': 'Fermi spacecraft is currently looking in this direction.'}},
   'Description': None}
   }

If a user wants to access the Packet_Type, they would have to do something like this:

.. code-block:: python

   packet_type = voevent['voe:VOEvent']['What']['Param'][0]['@value']

Which is very annoying because it's unclear that ['Param'] is a list and that
the [0] element is the Packet_Type. Instead I want users to be able to do this:

.. code-block:: python

   packet_type = voevent['What']['Packet_Type']

.. toctree::
   :maxdepth: 2
   :caption: Contents:

.. _voevent-parse: https://voevent-parse.readthedocs.io/en/stable/
.. _xmltodict: https://github.com/martinblech/xmltodict