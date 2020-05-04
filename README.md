django-compress-staticfiles
===========================
A Django static files storage backend inheriting from [ManifestFilesMixin][16]
and [StaticFilesStorage][12]. Compresses, using GZip and/or Brotli, and minifies
static files when running the Django [collectstatic][5] command.

### What this package does:
- Compresses static files using [Brotli][1] and/or GZip. See the [included
  filetypes][100] heading to see which filetypes are compressed.
- Minifies JS using [rJSMin][19].
- Minifies CSS using [csscompressor][6].

### What this package does *not* do:
- Does not support concatenation/bundling of JS or CSS.
- Does not support transpiling from any transpiling Javascript language.
- Does not support [SASS][13], [LESS][14] or any other CSS preprocessor.
- This package is not a linter or tester. The collectstatic command is not the
  place to be linting or testing your code. The primary purpose of this package
  is compressing staticfiles for use in staging or production environments —
  minification is optional but does so by default.
- Does not delete stale files from your `STATIC_ROOT` directory. If changes were
  made to some of your static files; old files will remain there. Use the
  `--clear` flag when running `collectstatic` to delete the entire `STATIC_ROOT`
  and recreate it — check out the Django docs for more info.

### Some important things to take note of:
- If `DEBUG = True` in your Django settings.py file; only the normal file
  is used in templates. Templates will only use the hashed and minified
  version of the file when `DEBUG = False`. This is the behaviour of the Django
  [staticfiles][15] app in the `url` method of the `ManifestFilesMixin`.
- The compressed version of the file is never used in the template. Your
  webserver can decide which version of the file to serve depending on the
  Accept-Encoding header in the request.
- This package updates the manifest JSON file created by ManifestFilesMixin
  with a path pointing to the hashed *and* minified version of each processed
  file where applicable.
- If there is a `.min` file to be copied to STATIC_ROOT; that file will be
  compressed but not re-minified. If that `.min` file has a corresponding
  non-minified counterpart, that non-minified file *will* be minified and
  that minified file is the one that will be used to map `regular.css` to
  `regular.min.{hash}.css` in the manifest file.
- This package does not yet deal with the @import rule and url() function in
  CSS; therefore the value is not updated after ManifestFilesMixin handles those
  things — the minified file will not be referenced, only the hashed version as
  substituted by ManifestFilesMixin.
- The original files, for example, `somefile.css` won't be compressed
  to `somefile.css.gz` because we will likely never use it.
- Files smaller than 200 bytes will not be compressed.

### Usage with cloud storage like Google Cloud Storage or Amazon S3:
Even though the CompressStaticFilesStorage inherits from StaticFilesStorage,
which inherits from FileSystemStorage, the CompressStaticFilesMixin and
MinifyFilesMixin can be used with your own storage.


Quickstart
----------
Install the app and it's dependencies using:
```
pip install django-compress-staticfiles
```

Set the [STATICFILES_STORAGE][4] setting in your project settings.py as follows:
```python
STATICFILES_STORAGE = 'compress_staticfiles.storage.CompressStaticFilesStorage'
```
You don't need to set any other settings for everything to work but for some
mild customisation see the settings heading for more info.

Run the [collectstatic][5] command as you usually would:
```
python manage.py collectstatic
```


Settings
--------
There's no need to set these settings as they have defaults — they're there
if you want them. All are `True` by default.
```python
# All are True by default.
MINIFY_STATIC = True
BROTLI_STATIC_COMPRESSION = True
GZIP_STATIC_COMPRESSION = True
```


Included filetypes for compression
----------------------------------
Only files ending with these extensions will be compressed:
- css
- js
- txt
- xml
- json
- svg
- md
- rst


Included filetypes for minification
-----------------------------------
- css
- js


JS Minification
---------------
The [rJSMin Python package][19] is used for JavaScript minification. See
rJSMin's Github repo for docs and more information. JS is not obfuscated.
Exclamation/bang comments will be retained.


CSS Minification
----------------
Exclamation/bang comments will be retained.


There might be some questions
-----------------------------
#### Why not just use [django-compressor][10] or [django-pipeline][11] instead?
Though I haven't used django-compressor or django-pipeline myself; I have gone
through their respective documentation. I'm sure django-compressor and
django-pipeline are excellent tools and I'm sure there's a time and place to be
using them.

However, this package aims to be something smaller and simpler with
absolutely no configuration needed; no template tags and no extra management
commands. It aims to be unobtrusive; to slide straight into the regular Django
`collectstatic' management command.

#### Why no bundling/concatenation of JS or CSS?
Bundling is so HTTP/1.1. Join us in HTTP/2 where things are multiplexed. :)
Jokes aside... If you really need bundling: it's probably best to look at
something like Webpack, [django-compressor][10] or [django-pipeline][11].

#### Why does this package use the `ManifestFilesMixin`?
For those who are unfamiliar with the ManifestFilesMixin please read the
Django docs for [ManifestFilesMixin][16] and [ManifestStaticFilesStorage][3].


Compatiblity
------------
- Compatible with Python 3.5 and above.
- Compatible with Django 1.10 and above. Do remember that, at the time of
  writing, Django 2.2 and below is deprecated and therefore there is only
  official support for Django 2.2 and above.
- Check rJSMin's Github [repo][19] / docs for more info regarding ES6
  compatibility.


Versioning
----------
This project follows [semantic versioning][20] (SemVer).


License, code of conduct and requirements
-----------------------------------------
Check the root of the repo for these files.



[//]: # (Links)

[1]: https://github.com/google/brotli
[2]: https://developers.google.com/closure/compiler
[3]: https://docs.djangoproject.com/en/stable/ref/contrib/staticfiles/#manifeststaticfilesstorage
[4]: https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-STATICFILES_STORAGE
[5]: https://docs.djangoproject.com/en/stable/ref/contrib/staticfiles/#collectstatic
[6]: https://github.com/sprymix/csscompressor
[7]: https://terser.org/
[8]: https://github.com/douglascrockford/JSMin
[9]: https://github.com/yui/yuicompressor
[10]: https://github.com/django-compressor/django-compressor
[11]: https://github.com/jazzband/django-pipeline
[12]: https://docs.djangoproject.com/en/stable/ref/contrib/staticfiles/#staticfilesstorage
[13]: https://sass-lang.com/
[14]: http://lesscss.org/
[15]: https://docs.djangoproject.com/en/stable/ref/contrib/staticfiles/#static-file-development-view
[16]: https://docs.djangoproject.com/en/stable/ref/contrib/staticfiles/#manifestfilesmixin
[17]: https://github.com/google/closure-compiler
[18]: https://developers.google.com/closure/compiler/docs/limitations
[19]: https://github.com/ndparker/rjsmin
[20]: https://semver.org/

[100]: /#included-filetypes-for-compression
