#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Authen
%define		pnam	NTLM
Summary:	Authen::NTLM - Perl extension for NTLM related computations
Summary(pl):	Authen::NTLM - rozszerzenie Perla o obliczenia oparte na NTLM
Name:		perl-Authen-NTLM
Version:	0.31
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7271a3a482cc19de23d683ad8b969ffd
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-Crypt-DES >= 2.03
BuildRequires:	perl-Digest-MD4 >= 1.1
%if %{with tests}
# this or perl(Digest::Perl::MD4) is required
BuildRequires:	perl-Crypt-DES_PP
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(Crypt::DES_PP)' 'perl(Digest::Perl::MD4)'

%description
The NTLM (Windows NT LAN Manager) authentication scheme is the
authentication algorithm used by Microsoft.

NTLM authentication scheme is used in DCOM and HTTP environment. It is
used to authenticate DCE RPC packets in DCOM. It is also used to
authenticate HTTP packets to MS Web Proxy or MS Web Server.

As of this version, NTLM module only provides the client side
functions to calculate NT response and LM response.

%description -l pl
Schemat autentykacji NTLM (Windows NT LAN Manager) jest algorytmem
autentykacji u¿ywanym przez Microsoft.

Schemat autentykacji NTLM jest wykorzystywany w ¶rodowiskach DCOM i
HTTP. W DCOM s³u¿y do autentykacji pakietów DCE RPC. W HTTP jest
wykorzystywany do autentykacji pakietów HTTP przez MS Web Proxy i MS
Web Server.

Aktualna wersja modu³u NTLM zawiera jedynie wsparcie dla funkcji
obliczaj±cych odpowiedzi NT i LM po stronie klienta.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Authen/NTLM.pm
%{perl_vendorlib}/Authen/NTLM
%{_mandir}/man3/*
