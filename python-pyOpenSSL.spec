# TODO: check why disabled tests fail and reenable them
#
# Conditional build:
%bcond_with	tests	# unit tests (seem not ready for openssl 3)
%bcond_without	python2	# CPython 2.x module
%bcond_with	python3	# CPython 3.x module (built from python3-pyOpenSSL.spec)
%bcond_without	doc	# HTML documentation (sphinx-based)

%define		module	pyOpenSSL
Summary:	Python 2 interface to the OpenSSL library
Summary(pl.UTF-8):	Interfejs Pythona 2 do biblioteki OpenSSL
Name:		python-%{module}
# keep 21.x here for python2 support
Version:	21.0.0
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pyopenssl/
Source0:	https://files.pythonhosted.org/packages/source/p/pyOpenSSL/%{module}-%{version}.tar.gz
# Source0-md5:	2ec707d15b4e92f5ca5e46e5aab2f4ca
URL:		https://github.com/pyca/pyopenssl
%if %(locale -a | grep -q '^C\.utf8$'; echo $?)
BuildRequires:	glibc-localedb-all
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-cryptography >= 2.8
BuildRequires:	python-flaky
BuildRequires:	python-pretend
BuildRequires:	python-pytest >= 3.0.1
BuildRequires:	python-six >= 1.5.2
%endif
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-cryptography >= 2.8
BuildRequires:	python3-flaky
BuildRequires:	python3-pretend
BuildRequires:	python3-pytest >= 3.0.1
BuildRequires:	python3-six >= 1.5.2
%endif
%endif
%if %{with doc}
BuildRequires:	python-sphinx_rtd_theme
BuildRequires:	sphinx-pdg-2
%endif
Obsoletes:	python-OpenSSL < 0.6
Obsoletes:	python-pyOpenSSL-examples < 19.1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
High-level wrapper around a subset of the OpenSSL library, includes:
 - SSL.Connection objects, wrapping the methods of Python's portable
   sockets
 - Callbacks written in Python
 - Extensive error-handling mechanism, mirroring OpenSSL's error codes
...and much more.

This package contains Python 2 modules.

%description -l pl.UTF-8
Wysokopoziomowe obudowanie podzbioru biblioteki OpenSSL, zawierające:
 - obiekty SSL.Connection, obudowujący metody przenośnych gniazd
   Pythona
 - wywołania zwrotne napisane w Pythonie
 - obszerny mechanizm obsługi błędów odzwierciedlający kody błędów
   OpenSSL-a
...i wiele więcej.

Ten pakiet zawiera moduły Pythona 2.

%package -n python3-pyOpenSSL
Summary:	Python 3 interface to the OpenSSL library
Summary(pl.UTF-8):	Interfejs Pythona 3 do biblioteki OpenSSL
Group:		Libraries/Python

%description -n python3-pyOpenSSL
High-level wrapper around a subset of the OpenSSL library, includes:
 - SSL.Connection objects, wrapping the methods of Python's portable
   sockets
 - Callbacks written in Python
 - Extensive error-handling mechanism, mirroring OpenSSL's error codes
...and much more.

This package contains Python 3 modules.

%description -n python3-pyOpenSSL -l pl.UTF-8
Wysokopoziomowe obudowanie podzbioru biblioteki OpenSSL, zawierające:
 - obiekty SSL.Connection, obudowujący metody przenośnych gniazd
   Pythona
 - wywołania zwrotne napisane w Pythonie
 - obszerny mechanizm obsługi błędów odzwierciedlający kody błędów
   OpenSSL-a
...i wiele więcej.

Ten pakiet zawiera moduły Pythona 3.

%package apidocs
Summary:	%{module} API documentation
Summary(pl.UTF-8):	Dokumentacja API modułu %{module}
Group:		Documentation
Obsoletes:	python-pyOpenSSL-doc < 0.6-3
Obsoletes:	python-pyOpenSSL-doc-html < 0.6-3

%description apidocs
API documentation for %{module}.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu %{module}.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
LC_ALL=C.UTF-8 \
%py_build

%if %{with tests}
PYTHONPATH=$(pwd)/build-2/lib \
%{__python} -m pytest -v tests  -k 'not test_verify_with_time and not test_alpn_call_failure'
%endif
%endif

%if %{with python3}
LC_ALL=C.UTF-8 \
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/build-3/lib \
%{__python3} -m pytest -v tests  -k 'not test_verify_with_time not test_alpn_call_failure'
%endif
%endif

%if %{with doc}
%{__make} -C doc html \
	SPHINXBUILD=sphinx-build-2
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGELOG.rst README.rst
%dir %{py_sitescriptdir}/OpenSSL
%{py_sitescriptdir}/OpenSSL/*.py[co]
%{py_sitescriptdir}/pyOpenSSL-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pyOpenSSL
%defattr(644,root,root,755)
%doc CHANGELOG.rst README.rst
%dir %{py3_sitescriptdir}/OpenSSL
%{py3_sitescriptdir}/OpenSSL/*.py
%{py3_sitescriptdir}/OpenSSL/__pycache__
%{py3_sitescriptdir}/pyOpenSSL-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/_build/html/{*.html,_static,api}
%endif
