%include	/usr/lib/rpm/macros.python
%define		module	pyOpenSSL
Summary:	Binding of OpenSSL for Python
Summary(pl):	Interfejs OpenSSL dla Pythona
Name:		python-%{module}
Version:	0.5.1
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/pyopenssl/%{module}-%{version}.tar.gz
# Source0-md5:	4b27570a24eb21664e8c033394496a0e
Patch0:		%{name}-license-warning.patch
URL:		http://pyopenssl.sourceforge.net/
BuildRequires:	latex2html
BuildRequires:	lynx
BuildRequires:	openssl-devel
BuildRequires:	python-devel
BuildRequires:	tetex-latex
BuildRequires:	tetex-metafont
Requires:	python >= 2.2
Requires:	openssl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Binding of OpenSSL for Python.

%description -l pl
Interfejs OpenSSL dla Pythona.

%package doc
Summary:	Documentation for pyOpenSSL module
Summary(pl):	Dokumentacja do modu³u pyOpenSSL
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description doc
This package contains documentation files for pyOpenSSL Python module.

%description doc -l pl
Pakiet zawieraj±cy dokumentacjê dla modu³u Pythona pyOpenSSL.

%package doc-html
Summary:	HMTL documentation for pyOpenSSL module
Summary(pl):	Dokumentacja do modu³u pyOpenSSL w formacie HTML
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description doc-html
This package contains HTML documentation files for pyOpenSSL Python
module.

%description doc-html -l pl
Pakiet zawieraj±cy dokumentacjê dla modu³u Pythona pyOpenSSL w
formacie HTML.

%package examples
Summary:	Examples for pyOpenSSL module
Summary(pl):	Przyk³ady do modu³u pyOpenSSL
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example files for pyOpenSSL Python module.

%description examples -l pl
Pakiet zawieraj±cy przyk³adowe skrypty dla modu³u Pythona pyOpenSSL.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitedir},%{_examplesdir}/%{name}-%{version}}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--install-lib=%{py_sitedir} \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitedir} -name \*.py -exec rm {} \;

cp -ra examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

cd doc
%{__make} all

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog TODO
%dir %{py_sitedir}/OpenSSL
%attr(755,root,root) %{py_sitedir}/OpenSSL/*.so
%{py_sitedir}/OpenSSL/*.py[oc]

%files doc
%defattr(644,root,root,755)
%doc doc/pyOpenSSL.{dvi,ps,txt}

%files doc-html
%defattr(644,root,root,755)
%doc doc/html/*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
