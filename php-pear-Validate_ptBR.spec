%include	/usr/lib/rpm/macros.php
%define		_class		Validate
%define		_subclass	ptBR
%define		_status		alpha
%define		_pearname	Validate_ptBR

Summary:	%{_pearname} - Validation class for Brazil
Summary(pl):	%{_pearname} - Klasa sprawdzaj�ca poprawno�� dla Brazylii
Name:		php-pear-%{_pearname}
Version:	0.5.2
Release:	1
Epoch:		0
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	ca92b59ae9c6e1e3f287493ff7d0c31e
URL:		http://pear.php.net/package/Validate_ptBR/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
Obsoletes:	%{name}-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package contains locale validation for Brazil such as:
- Postal Code
- CNPJ
- CPF
- Region (brazilian states)
- Phone Number
- Vehicle's plate

In PEAR status of this package is: %{_status}.

%description -l pl
Pakiet do sprawdzania poprawno�ci dla Brazylii danych takich jak:
- kod pocztowy
- CNPJ
- CPF
- region (stan brazylijski)
- numer telefnu
- numer rejestracyjny pojazdu

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Validate/ptBR.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Validate_ptBR
