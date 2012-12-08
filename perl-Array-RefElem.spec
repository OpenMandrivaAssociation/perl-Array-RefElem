%define	upstream_name	 Array-RefElem
%define	upstream_version 1.00

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 14

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
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorarch}/Array
%{perl_vendorarch}/auto/Array


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-14mdv2012.0
+ Revision: 765065
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-13
+ Revision: 763481
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-12
+ Revision: 667030
- mass rebuild

* Mon Aug 02 2010 Funda Wang <fwang@mandriva.org> 1.0.0-11mdv2011.0
+ Revision: 564956
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.0.0-10mdv2011.0
+ Revision: 555421
- rebuild

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1.0.0-9mdv2010.1
+ Revision: 504573
- rebuild using %%perl_convert_version

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.00-8mdv2010.0
+ Revision: 426416
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.00-7mdv2009.0
+ Revision: 223541
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 1.00-6mdv2008.1
+ Revision: 151396
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 17 2007 Thierry Vignaud <tv@mandriva.org> 1.00-5mdv2008.0
+ Revision: 64783
- rebuild


* Sun Jan 14 2007 Olivier Thauvin <nanardon@mandriva.org> 1.00-4mdv2007.0
+ Revision: 108764
- rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-Array-RefElem

* Fri Jan 13 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.00-3mdk
- Rebuild, cleanup

* Mon Nov 15 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.00-2mdk
- Rebuild for new perl

* Thu Apr 22 2004 Per �yvind Karlsen <peroyvind@linux-mandrake.com> 1.00-1mdk
- 1.00
- add url
- cosmetics
- drop distribution tag

* Wed Feb 25 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.02-11mdk
- rebuild
- own dir

