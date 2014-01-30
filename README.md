Riseup Help Pages
==================================

This is the repository for the riseup help pages at http://help.riseup.net.

It is entirely static, but relies on a bunch of apache tricks for things like
language negotiation.

To submit changes, please fork this repo and issue pull requests on github.

The static content files in ./public/ are rendered from the content in
./pages/ using the command `amber rebuild`.

To install amber:

    sudo gem install amber

See https://github.com/elijh/amber for more information.

After you have made changes, run this command in this repo directory to
completely re-render the entire site:

    amber rebuild

When you are making changes, it is easiest to see a preview of these changes
by running the amber server:

    amber server

Then browse to http://localhost:8000. Any page you view this way gets re-
rendered when it is loaded. Because the links and css paths are absolute,
loading the rendered pages directly in the browser will create ugly results.
For this reason, it is best to use the `amber server`.

File structure
------------------------------

There are two ways to create pages:

A page might be represented by files with different language suffixes:

    email.en.text
    email.pt.text

Alternately, a page might be represented by a folder. This method allows you
to have sub-pages

    email/
      en.text
      pt.text
      client/
        en.text

Notes on markup
------------------------------

You can create pages in three different markup languages:

* textile (suffix .text)
* markdown (suffix .md)
* haml (suffix .haml)

Most of the riseup help pages are written using textile. It is best to keep to
textile for consistency. Some pages are in haml, because there are still some
bugs when inserting the contents of another page into textile or markdown
pages.

Here is a brief overview of textile markup:

    h1. heading 1
    h2. heading 2

    this is a paragraph

    * this is a list
    * another item in the list

    "this is a link":http://tothissite.org

    here is some *bold text*

For a complete reference, see http://redcloth.org/textile/

For external links, use `"this":http://format.org`. However, in order to link to
other help pages, it is best to use some special markup:

    <%= link 'label' => 'page-name' %>
    or
    <%= link 'page-name' %>
    or
    <%= link 'chat/client' %>

By using this `link` function it will automatically find the right path for
the page with the specified name. Also, it will warn you if the page name is
missing and it will ensure that the link is created with the correct
language prefix.

Setting page properties
---------------------------------

Every file can have a "properties header". It looks like this:

    @title = "A fine page"
    @toc = false

    continue on here with body text.

The properties start with '@' and are stripped out of the source file before
it is rendered. Property header lines are evaluated as ruby. All properties
are optional and they are inherited, including `@title`.

Available properties:

* `@title` -- The title for the page, appearing as in an H1 on the top of the
   page and as the HTML title. Also used for navigation title if `@nav_title`
   is not set.

* `@nav_title` -- The title for the navigation to this page, as well as the
   HTML title if @title is not set.

* `@toc` -- If set to `false`, don't include a table of contents when rendering
   the file. This only applies to .text and .md files.

* `@layout` -- Manually set the layout template to use for rendering this page.

Tracking pages that need translating
--------------------------------------------

We do not yet have the capability to automatically identify which translated
pages need to be updated. However, in the future, I plan to add the command
`amber diff [language-code]`, which will automatically spit out a listing that
shows the changes made to the source English pages since the translation for
each page was made.

Installing on Mac
------------------------------

(I haven't tried this myself)

Ruby 1.9 or greater is required to run amber.

Mac OS 10.9 (Mavericks) or later is running ruby 2.0 and can work with amber
out of the box. For earlier Mac OS releases, you need to upgrade the ruby that
comes with the computer. The easiest way to do this is with homebrew. To
install, open a terminal and type:

    ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"
    brew install ruby

After ruby is at 1.9 or newer, then just run:

    sudo gem install amber

Alternately, if you want different versions of ruby installed, consider:

* https://github.com/sstephenson/rbenv
* http://rvm.io/

Installing on Debian/Ubuntu
----------------------------------

If you have a recent OS, it should come with Ruby 1.9. Then, all you need to do is:

    sudo gem install amber

