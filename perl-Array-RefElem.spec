%define	upstream_name	 Array-RefElem
%define	upstream_version 1.00

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 12

Summary: 	Direct access to the internal perl routines for arrays & hashes
License: 	GPL
Group: 		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/authors/id/GAAS/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel

BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module gives direct access to the internal perl routines that let
you store reference to things in arrays and hashes.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
