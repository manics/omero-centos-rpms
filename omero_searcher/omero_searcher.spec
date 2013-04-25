Summary: OMERO.searcher
Name: omero-searcher
Version: 0.0.1
Release: 1
Source0: omero-searcher.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildArch: noarch
Url: http://murphylab.web.cmu.edu/software/

%global omerodir /opt/omero44

Requires:       omero-server >= 4.4.7
Requires:       python-pyslid
Requires:       python-ricerca

%description
Image search for OMERO.

Built from
https://github.com/manics/omero_searcher/commit/05de4c65838ddc80eae9ea2d7c0c1b0da80afd6f
Source archive created using
git archive --prefix=omero_searcher/ -o omero-searcher.tar.gz 05de4c65838ddc80eae9ea2d7c0c1b0da80afd6f


%prep
%setup -n omero_searcher

%build

%install
mkdir -p %{buildroot}%{omerodir}/server/lib/python/omeroweb/omero_searcher
cp -a *.py templates \
    %{buildroot}%{omerodir}/server/lib/python/omeroweb/omero_searcher
mkdir -p %{buildroot}%{omerodir}/server/lib/scripts/searcher
cp -a scripts/*.py %{buildroot}%{omerodir}/server/lib/scripts/searcher
mkdir -p %{buildroot}/OMERO/pyslid.data

%files
%{omerodir}/server/lib/python/omeroweb/omero_searcher
%{omerodir}/server/lib/scripts/searcher
%attr(-,omero,omero) /OMERO/pyslid.data

%changelog
* Wed Apr 24 2013 Simon Li<spli@dundee.ac.uk> - 6-1
- Initial package