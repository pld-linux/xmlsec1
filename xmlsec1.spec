Summary:	XML Security Library
Summary(pl.UTF-8):	Biblioteka bezpieczeństwa XML
Name:		xmlsec1
Version:	1.2.15
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://www.aleksey.com/xmlsec/download/%{name}-%{version}.tar.gz
# Source0-md5:	43bc8011a33ef9fba862eca4573034c4
Patch0:		%{name}-nss.patch
URL:		http://www.aleksey.com/xmlsec/
BuildRequires:	autoconf >= 2.2
BuildRequires:	automake
BuildRequires:	gnutls-devel >= 1.2.5
BuildRequires:	libltdl-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.7.4
BuildRequires:	libxslt-devel >= 1.0.20
BuildRequires:	nspr-devel >= 4.0
BuildRequires:	nss-devel >= 3.2
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	pkgconfig
Requires:	libxml2 >= 1:2.7.4
Requires:	libxslt >= 1.0.20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XMLSec library provides C based implementation for major XML Security
standards:
 - XML Signature Syntax and Processing
   <http://www.w3.org/TR/xmldsig-core/>
 - XML Encryption Syntax and Processing
   <http://www.w3.org/TR/xmlenc-core/>
XMLSec is based on well known LibXML <http://xmlsoft.org/>, LibXSLT
<http://xmlsoft.org/XSLT/> and OpenSSL <http://www.openssl.org/>
libraries.

This package contains core library, which provides implementation of
all the engines as well as support for all the non crypto transforms
(XML parser, c14n transforms, XPath and XSLT transforms...).
For cryptographic transforms, keys data and key data stores look at
one of the separate XML Security Crypto libraries (GnuTLS, NSS or
OpenSSL based).

%description -l pl.UTF-8
Biblioteka XMLSec dostarcza implementację w C głównych standardów
bezpieczeństwa XML:
 - XML Signature Syntax and Processing (składnia i przetwarzanie
   sygnatur XML)
   <http://www.w3.org/TR/xmldsig-core/>
 - XML Encryption Syntax and Processing (składnia i przetwarzanie
   szyfrowania XML).
XMLSec jest oparta na dobrze znanych bibliotekach LibXML
<http://xmlsoft.org/>, LibXSLT <http://xmlsoft.org/XSLT/> oraz OpenSSL
<http://www.openssl.org/>.

Ten pakiet zawiera główną bibliotekę, zawierającą implementację
wszystkich silników oraz obsługę wszystkich przekształceń
niekryptograficznych (analizator XML, przekształcenia c14n,
przekształcenia XPath i XSLT...). Przekształcenia kryptograficzne,
dane kluczy oraz metody przechowywania kluczy można znaleźć w jednej
z wydzielonych bibliotek XML Security Crypto (opartych na GnuTLS,
NSS lub OpenSSL).

%package devel
Summary:	Header files for XMLSec library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki XMLSec
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libxml2-devel >= 1:2.7.4
Requires:	libxslt-devel >= 1.0.20

%description devel
Header files for XMLSec library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki XMLSec.

%package static
Summary:	Static XMLSec library
Summary(pl.UTF-8):	Statyczna biblioteka XMLSec
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static XMLSec library.

%description static -l pl.UTF-8
Statyczna biblioteka XMLSec.

%package apidocs
Summary:	XMLSec library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki XMLSec
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
XMLSec library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki XMLSec.

%package gnutls
Summary:	GnuTLS Crypto library for XML Security Library
Summary(pl.UTF-8):	Biblioteka kryptograficzna GnuTLS dla biblioteki XMLSec
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gnutls >= 1.0.0

%description gnutls
GnuTLS Crypto library for XML Security Library provides GnuTLS based
crypto services for the XMLSec library.

%description gnutls -l pl.UTF-8
Biblioteka kryptograficzna GnuTLS dla biblioteki XMLSec dostarcza
usługi kryptograficzne oparte na bibliotece GnuTLS.

%package gnutls-devel
Summary:	Header files for XMLSec GnuTLS API
Summary(pl.UTF-8):	Pliki nagłówkowe API GnuTLS XMLSec
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gnutls = %{version}-%{release}
Requires:	gnutls-devel >= 1.0.0

%description gnutls-devel
Header files for developing XML Security applications with GnuTLS.

%description gnutls-devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia aplikacji związanych z bezpieczeństwem
XML przy użyciu GnuTLS.

%package gnutls-static
Summary:	Static GnuTLS Crypto library for XML Security Library
Summary(pl.UTF-8):	Statyczna biblioteka kryptograficzna GnuTLS dla biblioteki XMLSec
Group:		Development/Libraries
Requires:	%{name}-gnutls-devel = %{version}-%{release}

%description gnutls-static
Static GnuTLS Crypto library for XML Security Library.

%description gnutls-static -l pl.UTF-8
Statyczna biblioteka kryptograficzna GnuTLS dla biblioteki XMLSec.

%package nss
Summary:	NSS Crypto library for XML Security Library
Summary(pl.UTF-8):	Biblioteka kryptograficzna NSS dla biblioteki XMLSec
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	nspr >= 4.0
Requires:	nss >= 3.2

%description nss
NSS Crypto library for XML Security Library provides NSS based crypto
services for the XMLSec library.

%description nss -l pl.UTF-8
Biblioteka kryptograficzna NSS dla biblioteki XMLSec dostarcza usługi
kryptograficzne oparte na bibliotece NSS.

%package nss-devel
Summary:	Header files for XMLSec NSS API
Summary(pl.UTF-8):	Pliki nagłówkowe API NSS XMLSec
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-nss = %{version}-%{release}
Requires:	nspr-devel >= 4.0
Requires:	nss-devel >= 3.2

%description nss-devel
Header files for developing XML Security applications with NSS.

%description nss-devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia aplikacji związanych z bezpieczeństwem
XML przy użyciu NSS.

%package nss-static
Summary:	Static NSS Crypto library for XML Security Library
Summary(pl.UTF-8):	Statyczna biblioteka kryptograficzna NSS dla biblioteki XMLSec
Group:		Development/Libraries
Requires:	%{name}-nss-devel = %{version}-%{release}

%description nss-static
Static NSS Crypto library for XML Security Library.

%description nss-static -l pl.UTF-8
Statyczna biblioteka kryptograficzna NSS dla biblioteki XMLSec.

%package openssl
Summary:	OpenSSL Crypto library for XML Security Library
Summary(pl.UTF-8):	Biblioteka kryptograficzna OpenSSL dla biblioteki XMLSec
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	openssl >= 0.9.7

%description openssl
OpenSSL Crypto library for XML Security Library provides OpenSSL based
crypto services for the XMLSec library.

%description openssl -l pl.UTF-8
Biblioteka kryptograficzna OpenSSL dla biblioteki XMLSec dostarcza
usługi kryptograficzne oparte na bibliotece OpenSSL.

%package openssl-devel
Summary:	Header files for XMLSec OpenSSL API
Summary(pl.UTF-8):	Pliki nagłówkowe API OpenSSL XMLSec
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-openssl = %{version}-%{release}
Requires:	openssl-devel >= 0.9.7

%description openssl-devel
Header files for developing XML Security applications with OpenSSL.

%description openssl-devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia aplikacji związanych z bezpieczeństwem
XML przy użyciu OpenSSL.

%package openssl-static
Summary:	Static OpenSSL Crypto library for XML Security Library
Summary(pl.UTF-8):	Statyczna biblioteka kryptograficzna OpenSSL dla biblioteki XMLSec
Group:		Development/Libraries
Requires:	%{name}-nss-devel = %{version}-%{release}

%description openssl-static
Static OpenSSL Crypto library for XML Security Library.

%description openssl-static -l pl.UTF-8
Statyczna biblioteka kryptograficzna OpenSSL dla biblioteki XMLSec.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	CPPFLAGS='%{rpmcppflags} -DLTDL_OBJDIR=\".libs\" -DLTDL_SHLIB_EXT=\".so\"' \
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
%attr(755,root,root) %ghost %{_libdir}/libxmlsec1.so.1
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
%{_aclocaldir}/xmlsec1.m4
%{_mandir}/man1/xmlsec1-config.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/libxmlsec1.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/xmlsec1

%files gnutls
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxmlsec1-gnutls.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxmlsec1-gnutls.so.1
%attr(755,root,root) %{_libdir}/libxmlsec1-gnutls.so

%files gnutls-devel
%defattr(644,root,root,755)
%{_libdir}/libxmlsec1-gnutls.la
%{_includedir}/xmlsec1/xmlsec/gnutls
%{_pkgconfigdir}/xmlsec1-gnutls.pc

%files gnutls-static
%defattr(644,root,root,755)
%{_libdir}/libxmlsec1-gnutls.a

%files nss
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxmlsec1-nss.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxmlsec1-nss.so.1
%attr(755,root,root) %{_libdir}/libxmlsec1-nss.so

%files nss-devel
%defattr(644,root,root,755)
%{_libdir}/libxmlsec1-nss.la
%{_includedir}/xmlsec1/xmlsec/nss
%{_pkgconfigdir}/xmlsec1-nss.pc

%files nss-static
%defattr(644,root,root,755)
%{_libdir}/libxmlsec1-nss.a

%files openssl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxmlsec1-openssl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxmlsec1-openssl.so.1
%attr(755,root,root) %{_libdir}/libxmlsec1-openssl.so

%files openssl-devel
%defattr(644,root,root,755)
%{_libdir}/libxmlsec1-openssl.la
%{_includedir}/xmlsec1/xmlsec/openssl
%{_pkgconfigdir}/xmlsec1-openssl.pc

%files openssl-static
%defattr(644,root,root,755)
%{_libdir}/libxmlsec1-openssl.a
