%if %{_use_internal_dependency_generator}
%define __noautoreq 'pear(config.php)'
%else
%define		_requires_exceptions 'pear(config.php)'
%endif

%define		_class		Auth
%define		_pearname	%{_class}_OpenID

Summary:	PHP OpenID
Name:		php-pear-%{_pearname}
Version:	2.1.2
Release:	7
Group:		Development/PHP
License:	Apache License
URL:		https://www.openidenabled.com/openid/libraries/php
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

%description
An implementation of the OpenID single sign-on authentication protocol.

This package also supports yubico:
http://code.google.com/p/yubico-openid-server/

%prep

%setup -q -n php-openid-%{version}
%patch0 -p1

# strip away annoying ^M
find -type f | grep -v ".gif" | grep -v ".png" | grep -v ".jpg" | xargs dos2unix

%build

%install
install -d %{buildroot}%{_datadir}/pear/%{_class}/OpenID
install -d %{buildroot}%{_datadir}/pear/%{_class}/Yadis

install -m0644 Auth/OpenID.php %{buildroot}%{_datadir}/pear/%{_class}/
install -m0644 Auth/OpenID/*.php %{buildroot}%{_datadir}/pear/%{_class}/OpenID/
install -m0644 Auth/Yadis/*.php %{buildroot}%{_datadir}/pear/%{_class}/Yadis/

%files
%defattr(644,root,root,755)
%doc NEWS COPYING README CHANGELOG doc examples
%dir %{_datadir}/pear/%{_class}/OpenID
%dir %{_datadir}/pear/%{_class}/Yadis
%{_datadir}/pear/%{_class}/OpenID.php
%{_datadir}/pear/%{_class}/OpenID/*.php
%{_datadir}/pear/%{_class}/Yadis/*.php



%changelog
* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 2.1.2-4mdv2011.0
+ Revision: 679262
- mass rebuild

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 2.1.2-3mdv2010.0
+ Revision: 440932
- rebuild

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 2.1.2-2mdv2009.1
+ Revision: 321894
- rebuild

* Tue Sep 16 2008 Oden Eriksson <oeriksson@mandriva.com> 2.1.2-1mdv2009.0
+ Revision: 285169
- import php-pear-Auth_OpenID


* Tue Sep 16 2008 Oden Eriksson <oeriksson@mandriva.com> 2.1.2-1mdv2009.0
- initial Mandriva package (ATrpms import)
