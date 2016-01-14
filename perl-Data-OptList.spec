%{?scl:%scl_package perl-Data-OptList}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Data-OptList
Summary:        Parse and validate simple name/value option pairs
Version:        0.108
Release:        4%{?dist}
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Data-OptList/
Source0:        http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/Data-OptList-%{version}.tar.gz 
BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  %{?scl_prefix}perl(File::Find)
BuildRequires:  %{?scl_prefix}perl(File::Temp)
BuildRequires:  %{?scl_prefix}perl(List::Util)
BuildRequires:  %{?scl_prefix}perl(Params::Util)
BuildRequires:  %{?scl_prefix}perl(Sub::Install) >= 0.921
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.88
BuildRequires:  %{?scl_prefix}perl(Test::Pod)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})

%description
Hashes are great for storing named data, but if you want more than one entry
for a name, you have to use a list of pairs. Even then, this is really boring
to write:

$values = [
    foo => undef,
    bar => undef,
    baz => undef,
    xyz => { ... },
];

With Data::OptList, you can do this instead:

$values = Data::OptList::mkopt([
    qw(foo bar baz),
    xyz => { ... },
]);

This works by assuming that any defined scalar is a name and any reference
following a name is its value.

%prep
%setup -q -n Data-OptList-%{version}

%{?scl:scl enable %{scl} "}
perl -pi -e 's|^#!perl|#!/usr/bin/perl|' t/*
%{?scl:"}


%build
%{?scl:scl enable %{scl} "}
perl Makefile.PL INSTALLDIRS=vendor
%{?scl:"}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
%{?scl:scl enable %{scl} "}
make pure_install DESTDIR=%{buildroot}
%{?scl:"}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
%{_fixperms} %{buildroot}

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}
%{?scl:scl enable %{scl} - << \EOF}
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))"
%{?scl:EOF}

%files
%doc Changes LICENSE README t/
%{perl_vendorlib}/Data/
%{_mandir}/man3/Data::OptList.3pm*

%changelog
* Thu Nov 21 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.108-4
- Rebuilt for SCL

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.108-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Petr Pisar <ppisar@redhat.com> - 0.108-2
- Perl 5.18 rebuild

* Sat Jul  6 2013 Paul Howarth <paul@city-fan.org> - 0.108-1
- Update to 0.108:
  - Repackage, new bug tracker
- Explicitly run the extra tests
- Don't need to remove empty directories from the buildroot
- Drop obsoletes/provides for old -tests sub-package

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.107-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 13 2012 Jitka Plesnikova <jplesnik@redhat.com> - 0.107-8
- Fix wrong script interpreter

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.107-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.107-6
- Perl 5.16 rebuild

* Sat Jan 21 2012 Paul Howarth <paul@city-fan.org> - 0.107-5
- obsolete/provide old -tests subpackage to support upgrades

* Fri Jan 20 2012 Paul Howarth <paul@city-fan.org> - 0.107-4
- drop -tests subpackage (general lack of interest in this), but include
  them as documentation for the main package
- drop redundant %%{?perl_default_filter}
- don't use macros for commands
- can't find any dependency cycle so drop %%{?perl_bootstrap} usage
- drop ExtUtils::MakeMaker version requirement to 6.30, actual working minimum

* Wed Jan 11 2012 Paul Howarth <paul@city-fan.org> - 0.107-3
- package LICENSE file
- run test suite even when bootstrapping, as it should still pass
- run release tests too
- enhance %%description so it makes sense
- BR: perl(Test::More)

* Tue Jun 28 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.107-2
- Perl mass rebuild
- add perl_bootstrap macro

* Wed May 11 2011 Iain Arnell <iarnell@gmail.com> 0.107-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.106-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.106-3
- rebuild to fix problems with vendorarch/lib (#661697)

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.106-2
- Mass rebuild with perl-5.12.0

* Mon Mar 08 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.106-1
- update by Fedora::App::MaintainerTools 0.004
- PERL_INSTALL_ROOT => DESTDIR
- updating to latest GA CPAN version (0.106)
- added a new br on perl(ExtUtils::MakeMaker) (version 6.42)
- added a new br on perl(List::Util) (version 0)
- altered br on perl(Sub::Install) (0.92 => 0.921)
- added a new req on perl(List::Util) (version 0)
- added a new req on perl(Params::Util) (version 0.14)
- added a new req on perl(Sub::Install) (version 0.921)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.104-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.104-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.104-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 11 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.104-1
- update to 0.104

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.103-2
- Rebuild for perl 5.10 (again)

* Thu Jan 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.103-1
- rebuild for new perl
- bump to 0.103
- fix license tag

* Thu Sep 07 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.101-2
- bump

* Sat Sep 02 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.101-1
- Specfile autogenerated by cpanspec 1.69.1.
