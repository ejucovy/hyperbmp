Hyperbmp is a web tool for "hyperbitmap" files: grids of colors with hyperlinks.

The hyperbitmap (.hbmp) format is a simple csv-based format::

  blue,blue,white,white,red,red
  blue,blue,white,white,red,red
  blue,blue,white>http://google.fr,white>http://google.fr,red,red
  blue,blue,white>http://google.fr,white>http://google.fr,red,red
  blue,blue,white,white,red,red
  blue,blue,white,white,red,red

Each grid entry in the CSV contains a valid HTML color and, optionally, a hyperlink.
If there is a hyperlink, the ">" character is used as a separator.

The CSV can then be rendered as an HTML table, with each cell colored
accordingly, and hyperlinks rendered where they should appear.

The hyperbmp software will render .hbmp files into HTML for browser display.

The software also provides a simple editing environment for .hbmp files using
Javascript. It is built as a plugin to `Svenweb <http://pypi.python.org/pypi/svenweb>`_
though a standalone version wouldn't be hard to build either.
