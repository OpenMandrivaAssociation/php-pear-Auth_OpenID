%define		_requires_exceptions 'pear(config.php)'

%define		_class		Auth
%define		_pearname	%{_class}_OpenID

Summary:	PHP OpenID
Name:		php-pear-%{_pearname}
Version:	2.1.2
Release:	%mkrel 3
Group:		Development/PHP
License:	Apache License
URL:		http://www.openidenabled.com/openid/libraries/php
Source0:	http://openidenabled.com/files/php-openid/packages/php-openid-%{version}.tar.bz2
Patch0:		php-openid-yubico-0.diff
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
Requires:	php-pgsql
Requires:	php-mysql
Requires:	php-bcmath
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
An implementation of the OpenID single sign-on authentication protocol.

This package also supports yubico:
http://code.google.com/p/yubico-openid-server/

%prep

%setup -q -n php-openid-%{version}
%patch0 -p1

# strip away annoying ^M
find -type f | grep -v ".gif" | grep -v ".png" | grep -v ".jpg" | xargs dos2unix -U

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/%{_class}/OpenID
install -d %{buildroot}%{_datadir}/pear/%{_class}/Yadis

install -m0644 Auth/OpenID.php %{buildroot}%{_datadir}/pear/%{_class}/
install -m0644 Auth/OpenID/*.php %{buildroot}%{_datadir}/pear/%{_class}/OpenID/
install -m0644 Auth/Yadis/*.php %{buildroot}%{_datadir}/pear/%{_class}/Yadis/

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc NEWS COPYING README CHANGELOG doc examples
%dir %{_datadir}/pear/%{_class}/OpenID
%dir %{_datadir}/pear/%{_class}/Yadis
%{_datadir}/pear/%{_class}/OpenID.php
%{_datadir}/pear/%{_class}/OpenID/*.php
%{_datadir}/pear/%{_class}/Yadis/*.php

