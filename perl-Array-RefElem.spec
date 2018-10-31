%define	upstream_name	 Array-RefElem
%define	upstream_version 1.00

Summary:	Direct access to the internal perl routines for arrays & hashes
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	26
License:	GPLv2
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/authors/id/GAAS/%{upstream_name}-%{upstream_version}.tar.bz2
BuildRequires:	perl-devel

%description
This module gives direct access to the internal perl routines that let
you store reference to things in arrays and hashes.

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="$RPM_OPT_FLAGS"

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorarch}/Array
%{perl_vendorarch}/auto/Array
%{_mandir}/man3/*

