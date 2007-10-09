%define		module	pyOpenSSL
Summary:	Binding of OpenSSL for Python
Summary(pl.UTF-8):	Interfejs OpenSSL dla Pythona
Name:		python-%{module}
Version:	0.6
Release:	4
License:	LGPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/pyopenssl/%{module}-%{version}.tar.gz
# Source0-md5:	6200b71d3eb294a312d52c4825fc71c5
Patch0:		%{module}-%{version}-pkcs12.patch
Patch1:		%{module}-%{version}-crl.patch
Patch2:         %{module}-%{version}-pkcs12_cafile.patch
URL:		http://pyopenssl.sourceforge.net/
BuildRequires:	lynx
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	tetex-latex
BuildRequires:	tetex-metafont
%pyrequires_eq	python-modules
Obsoletes:	python-OpenSSL
Obsoletes:	python-pyOpenSSL-doc
Obsoletes:	python-pyOpenSSL-doc-html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python interface to the OpenSSL library.

%description -l pl.UTF-8
Interfejs Pythona do biblioteki OpenSSL.

%package examples
Summary:	Examples for pyOpenSSL module
Summary(pl.UTF-8):	Przykłady do modułu pyOpenSSL
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example files for pyOpenSSL Python module.

%description examples -l pl.UTF-8
Pakiet zawierający przykładowe skrypty dla modułu Pythona pyOpenSSL.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitedir},%{_examplesdir}/%{name}-%{version}}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--install-lib=%{py_sitedir} \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitedir} -name \*.py -exec rm {} \;

cp -ra examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog TODO doc/pyOpenSSL.{ps,txt}
%dir %{py_sitedir}/OpenSSL
%attr(755,root,root) %{py_sitedir}/OpenSSL/*.so
%{py_sitedir}/OpenSSL/*.py[oc]
%{py_sitedir}/*.egg-info

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
