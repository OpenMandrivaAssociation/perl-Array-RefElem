%define	module	Array-RefElem
%define	name	perl-%{module}
%define	version	1.00
%define	release	%mkrel 5

Summary: 	Direct access to the internal perl routines for arrays & hashes
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	GPL
Group: 		Development/Perl
Source0:	http://www.cpan.org/authors/id/GAAS/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
BuildRequires:	perl-devel
Requires: 	perl

%description
This module gives direct access to the internal perl routines that let
you store reference to things in arrays and hashes.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="$RPM_OPT_FLAGS"

%check
%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorarch}/Array
%{perl_vendorarch}/auto/Array


