%define name pymorph
%define version 0.96
%define unmangled_version 0.96
%define unmangled_version 0.96
%define release 1

Summary: Image Morphology Toolbox
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Luis Pedro Coelho <lpc@cmu.edu>
Url: http://luispedro.org/software/pymorph/

%description
========
PYMORPH
========


Summary
-------

This image morphology toolbox implements the basic binary and greyscale
morphology operations, working with numpy arrays representing images.

This is a pure Python package which is the companion package
to the book "Hands-on Morphological Image Processing." It has been
updated to work with numpy and the names and interfaces have been
Pythonised.


Includes basic operations such as
- erode
- dilate
- open
- tophat opening
- watershed
- ...

Links
-----

*Website*: `http://luispedro.org/software/pymorph
<http://luispedro.org/software/pymorph>`_

*API Documentation*: `http://packages.python.org/pymorph/
<http://packages.python.org/pymorph/>`__

*Mailing List*: Use the `pythonvision mailing list
<http://groups.google.com/group/pythonvision>`_ for questions, bug
submissions, etc.

Install
-------

One of

::

    pip install pymorph
    easy_install pymorph

or download and run

::

    python setup.py install

See Also
--------

The package `mahotas <http://luispedro.org/software/mahotas>`_ implements some
of the same functions in C++ and, so, it is much faster (even if it is not as
feature-full).

Status & Future Plans
---------------------

The package is actively maintained and any reported bug will be fixed fast.

Currently there are *no known bugs* (although testing coverage is not complete).

When all functions have a corresponding unit test and the whole of the
API documentation has been re-written into numpy rst format, I will release
version 1.0.

Authors, Copyright & License
----------------------------

Copyright 2003, Roberto A. Lotufo, UNICAMP-University of Campinas;
CenPRA-Renato Archer Research Center, Rubens C. Machado.

Copyright 2008-2010, Luis Pedro Coelho <lpc@cmu.edu>

The original package was written by RAF and RCM. Starting June 2008 (with
release 0.88), LPC updated the code to run on the more modern numpy base and
started fixing bugs and maintaining the package.

Pymorph is ruled by the **BSD License Terms**:


%prep
%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
