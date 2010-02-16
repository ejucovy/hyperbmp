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

When rendering a hyperbitmap in the browser, you can configure the height and width
of the grid elements using query string parameters `pw` and `ph`. For example,

  /foo.hbmp?pw=10&ph=50

will render foo.hbmp as a table where each TD has height=10 and width=10.

Run the software using a paste.deploy configuration for svenweb, but replace

  paste.app_factory = svenweb.factory:factory

with

  use = egg:hyperbmp

to enable the hyperbmp extensions for svenweb.  To tell the system to treat files
as hyperbitmaps, you can save files with the mimetype "text/csv+hbmp". A mimetype
mapper is set up for the .hbmp extension, so if you visit an addform for a new file
that ends in .hbmp, the hyperbmp editing environment will be loaded. You can disable
it and drop into the plaintext editor by appending the querystring parameter ?raw.
