Summary:	XML Security Library
Summary(pl):	Biblioteka bezpieczeñstwa XML
Name:		xmlsec1
Version:	1.2.8
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://www.aleksey.com/xmlsec/download/%{name}-%{version}.tar.gz
# Source0-md5:	9f86c77c2ca317d03fbd8fe2e685ea67
Patch0:		%{name}-nss.patch
URL:		http://www.aleksey.com/xmlsec/
BuildRequires:	autoconf >= 2.2
BuildRequires:	automake
BuildRequires:	gnutls-devel >= 1.0.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.12
BuildRequires:	libxslt-devel >= 1.0.20
BuildRequires:	nspr-devel >= 4.0
BuildRequires:	nss-devel >= 3.2
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	pkgconfig
Requires:	libxml2 >= 1:2.6.12
Requires:	libxslt >= 1.0.20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XMLSec library provides C based implementation for major XML Security
standards:
 - XML Signature Syntax and Processing
   http://www.w3.org/TR/xmldsig-core/
 - XML Encryption Syntax and Processing
   http://www.w3.org/TR/xmlenc-core/
XMLSec is based on well known LibXML (http://xmlsoft.org/), LibXSLT
(http://xmlsoft.org/XSLT/) and OpenSSL (http://www.openssl.org/)
libraries.

%description -l pl
Biblioteka XMLSec dostarcza implementacjê w C g³ównych standardów
bezpieczeñstwa XML:
 - XML Signature Syntax and Processing (sk³adnia i przetwarzanie
   sygnatur XML)
   http://www.w3.org/TR/xmldsig-core/
 - XML Encryption Syntax and Processing (sk³adnia i przetwarzanie
   szyfrowania XML).
XMLSec jest oparta na dobrze znanych bibliotekach LibXML
(http://xmlsoft.org/), LibXSLT (http://xmlsoft.org/XSLT/) oraz OpenSSL
(http://www.openssl.org/).

%package devel
Summary:	Header files for XMLSec library
Summary(pl):	Pliki nag³ówkowe biblioteki XMLSec
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk-doc-common
Requires:	libxml2-devel >= 1:2.6.12
Requires:	libxslt-devel >= 1.0.20

%description devel
Header files for XMLSec library.

%description devel -l pl
Pliki nag³ówkowe biblioteki XMLSec.

%package static
Summary:	Static XMLSec library
Summary(pl):	Statyczna biblioteka XMLSec
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static XMLSec library.

%description static -l pl
Statyczna biblioteka XMLSec.

%package gnutls
Summary:	GnuTLS crypto plugin for XML Security Library
Summary(pl):	Wtyczka kryptograficzna GnuTLS dla biblioteki XMLSec
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gnutls >= 1.0.0

%description gnutls
GnuTLS plugin for XML Security Library provides GnuTLS based crypto
services for the XMLSec library.

%description gnutls -l pl
Wtyczka GnuTLS dla biblioteki XMLSec dostarcza us³ugi kryptograficzne
oparte na bibliotece GnuTLS.

%package gnutls-devel
Summary:	Header files for XMLSec GnuTLS API
Summary(pl):	Pliki nag³ówkowe API GnuTLS XMLSec
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gnutls = %{version}-%{release}
Requires:	gnutls-devel >= 1.0.0

%description gnutls-devel
Header files for developing XML Security applications with GnuTLS.

%description gnutls-devel -l pl
Pliki nag³ówkowe do tworzenia aplikacji zwi±zanych z bezpieczeñstwem
XML przy u¿yciu GnuTLS.

%package nss
Summary:	NSS crypto plugin for XML Security Library
Summary(pl):	Wtyczka kryptograficzna NSS dla biblioteki XMLSec
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	nspr >= 4.0
Requires:	nss >= 3.2

%description nss
NSS plugin for XML Security Library provides NSS based crypto services
for the XMLSec library.

%description nss -l pl
Wtyczka NSS dla biblioteki XMLSec dostarcza us³ugi kryptograficzne
oparte na bibliotece NSS.

%package nss-devel
Summary:	Header files for XMLSec NSS API
Summary(pl):	Pliki nag³ówkowe API NSS XMLSec
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-nss = %{version}-%{release}
Requires:	nspr-devel >= 4.0
Requires:	nss-devel >= 3.2

%description nss-devel
Header files for developing XML Security applications with NSS.

%description nss-devel -l pl
Pliki nag³ówkowe do tworzenia aplikacji zwi±zanych z bezpieczeñstwem
XML przy u¿yciu NSS.

%package openssl
Summary:	OpenSSL crypto plugin for XML Security Library
Summary(pl):	Wtyczka kryptograficzna OpenSSL dla biblioteki XMLSec
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	openssl >= 0.9.7

%description openssl
OpenSSL plugin for XML Security Library provides OpenSSL based crypto
services for the XMLSec library.

%description openssl -l pl
Wtyczka OpenSSL dla biblioteki XMLSec dostarcza us³ugi
kryptograficzne oparte na bibliotece OpenSSL.

%package openssl-devel
Summary:	Header files for XMLSec OpenSSL API
Summary(pl):	Pliki nag³ówkowe API OpenSSL XMLSec
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-openssl = %{version}-%{release}
Requires:	openssl-devel >= 0.9.7

%description openssl-devel
Header files for developing XML Security applications with OpenSSL.

%description openssl-devel -l pl
Pliki nag³ówkowe do tworzenia aplikacji zwi±zanych z bezpieczeñstwem
XML przy u¿yciu OpenSSL.

%prep
%setup -q
%patch0 -p1

# workaround for variable name (really not macro)
echo 'm4_pattern_allow(PKG_CONFIG_ENABLED)' > acinclude.m4

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir}/xmlsec1 \
	--with-nspr=/usr \
	--with-nss=/usr
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	gnutls -p /sbin/ldconfig
%postun	gnutls -p /sbin/ldconfig

%post	nss -p /sbin/ldconfig
%postun	nss -p /sbin/ldconfig

%post	openssl -p /sbin/ldconfig
%postun	openssl -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog Copyright README TODO
%attr(755,root,root) %{_bindir}/xmlsec1
%attr(755,root,root) %{_libdir}/libxmlsec1.so.*.*.*
%{_mandir}/man1/xmlsec1.1*

%files devel
%defattr(644,root,root,755)
%doc HACKING
%attr(755,root,root) %{_bindir}/xmlsec1-config
%attr(755,root,root) %{_libdir}/libxmlsec1.so
%{_libdir}/libxmlsec1.la
%{_libdir}/xmlsec1Conf.sh
%dir %{_includedir}/xmlsec1
%dir %{_includedir}/xmlsec1/xmlsec
%{_includedir}/xmlsec1/xmlsec/*.h
%{_includedir}/xmlsec1/xmlsec/private
%{_pkgconfigdir}/xmlsec1.pc
%{_mandir}/man1/xmlsec1-config.1*
%{_gtkdocdir}/xmlsec1

%files static
%defattr(644,root,root,755)
%{_libdir}/libxmlsec1.a

%files gnutls
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxmlsec1-gnutls.so.*.*.*
%attr(755,root,root) %{_libdir}/libxmlsec1-gnutls.so

%files gnutls-devel
%defattr(644,root,root,755)
%{_libdir}/libxmlsec1-gnutls.la
%{_includedir}/xmlsec1/xmlsec/gnutls
%{_pkgconfigdir}/xmlsec1-gnutls.pc
# -static useless?
#%{_libdir}/libxmlsec1-gnutls.a

%files nss
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxmlsec1-nss.so.*.*.*
%attr(755,root,root) %{_libdir}/libxmlsec1-nss.so

%files nss-devel
%defattr(644,root,root,755)
%{_libdir}/libxmlsec1-nss.la
%{_includedir}/xmlsec1/xmlsec/nss
%{_pkgconfigdir}/xmlsec1-nss.pc
# -static useless?
#%{_libdir}/libxmlsec1-nss.a

%files openssl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxmlsec1-openssl.so.*.*.*
%attr(755,root,root) %{_libdir}/libxmlsec1-openssl.so

%files openssl-devel
%defattr(644,root,root,755)
%{_libdir}/libxmlsec1-openssl.la
%{_includedir}/xmlsec1/xmlsec/openssl
%{_pkgconfigdir}/xmlsec1-openssl.pc
# -static useless?
#%{_libdir}/libxmlsec1-openssl.a
