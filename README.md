# eC Runtime Library

https://ec-lang.org

A stand-alone core runtime library for the [eC programming language](https://ec-lang.org)

(_part of the [Ecere SDK](https://ecere.org)_)

Copyright (c) 1996-2025, Jérôme Jacovella-St-Louis

Copyright (c) 2005-2025, Ecere Corporation

Licensed under the [BSD 3-Clause License](https://opensource.org/license/bsd-3-clause)

Source: https://github.com/ecere/eC

Python packaging: https://github.com/ecere/pyecrt

[Learn more about eC here](https://ec-lang.org/overview/).

[![Ollie-the-sea-otter](https://ec-lang.org/images/eC-256.png)](https://ec-lang.org/)

## eC runtime functionality

The eC runtime library implements:

- management of eC data types, including the various flavors of structs and classes with and without reference counting, runtime type information, virtual method tables, reflection with the ability to register and define classes at runtime (loading/ejecting new dynamic modules), string management, generic field values containing type information, binary (de)serialization,
- various types of containers (dynamic arrays, hash tables, linked lists, AVL Trees, multiple forms of associative arrays),
- files I/O including temporary files, bidirectional processing input/output pipes, creating/decompressing/accessing files from archives (including resources packed directly within the executables), file/directory monitoring, cross-platform file handling functions,
- multithreading support including threads, mutexes, semaphores and conditions,
- internationalization (extensive unicode support with the Unicode data resources embedded within the library), internationalization of text strings compatible with GNU gettext, i18n of libecrt itself currently including Chinese, Brazilian Portuguese, Spanish, partial Russian translation, as well as the start of other languages,
- date and time handling,
- a JSON parser and writer (with support for automatic JSON (de)serialization of any eC types), as well as utilities to manage application settings stored in JSON files.

## Documentation

See https://ecere.org/docs/ecere/ecere.html and https://ecere.org/docs/ecereCOM/ecere.html for the API documentation of this core eC runtime library, which covers the `sys` and `com` namespaces of the Ecere runtime library.

[![Tao](https://ecere.com/images/tao.png)](https://ecere.org/tao.pdf)
The [Ecere Tao of Programming](https://ecere.org/tao.pdf) is a Programmer's Guide (still work in progress)
teaching the foundations of the eC programming language, also including a C primer.

See also the [samples](https://github.com/ecere/ecere-sdk/tree/master/samples) provided with the SDK, and some featured projects as prebuilt binaries at https://ecere.org/software.

Reach out on [IRC](https://web.libera.chat/?theme=cli#ecere) - **#ecere** on irc.libera.chat<br>
