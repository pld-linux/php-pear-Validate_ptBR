%include	/usr/lib/rpm/macros.php
%define		_class		Validate
%define		_subclass	ptBR
%define		_status		alpha
%define		_pearname	Validate_ptBR

Summary:	%{_pearname} - Validation class for Brazil
Summary(pl.UTF-8):	%{_pearname} - Klasa sprawdzająca poprawność dla Brazylii
Name:		php-pear-%{_pearname}
Version:	0.5.5
Release:	1
Epoch:		0
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	5e745946f1d4fb2c4969c0b6bc812d5f
URL:		http://pear.php.net/package/Validate_ptBR/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
Obsoletes:	php-pear-Validate_ptBR-tests
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

%description -l pl.UTF-8
Pakiet do sprawdzania poprawności dla Brazylii danych takich jak:
- kod pocztowy
- CNPJ
- CPF
- region (stan brazylijski)
- numer telefnu
- numer rejestracyjny pojazdu

Ta klasa ma w PEAR status: %{_status}.

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
