%define		module	pyOpenSSL
Summary:	Binding of OpenSSL for Python
Summary(pl.UTF-8):	Interfejs OpenSSL dla Pythona
Name:		python-%{module}
Version:	0.9
Release:	2
License:	LGPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/pyopenssl/%{module}-%{version}.tar.gz
# Source0-md5:	5bf282b2d6a03af921920c34079580f2
Patch0:		%{module}-0.8-pkcs12.patch
Patch1:		%{module}-0.8-crl.patch
Patch2:         %{module}-0.8-pkcs12_cafile.patch
URL:		http://pyopenssl.sourceforge.net/
BuildRequires:	lynx
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
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

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitedir},%{_examplesdir}/%{name}-%{version}}

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--install-lib=%{py_sitedir} \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitedir} -name \*.py -exec rm -f {} \;

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog TODO 
%dir %{py_sitedir}/OpenSSL
%dir %{py_sitedir}/OpenSSL/test
%attr(755,root,root) %{py_sitedir}/OpenSSL/*.so
%{py_sitedir}/OpenSSL/*.py[oc]
%{py_sitedir}/OpenSSL/test/*.py[oc]
%{py_sitedir}/*.egg-info

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
